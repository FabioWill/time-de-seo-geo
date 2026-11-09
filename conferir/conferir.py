#!/usr/bin/env python3
"""
conferir/conferir.py

Purpose: scores one product page (a saved .html file) against the SEO + GEO ruler in
         regua/regua.md: 16 SEO criteria (what Google reads) and 10 GEO criteria (what an AI answer
         engine needs to cite the product), each group summing 100, plus two gates that stop the
         score. Everything measurable is measured here, by code. Five GEO criteria need reading the
         text; the agent decides them and passes them in with --julgamento.
Exports: none (CLI).
           python3 conferir.py <pagina.html> --palavra-chave "..." [--url URL]
                   [--descricao "#id" | ".classe"] [--renderizado pagina-js.html]
                   [--julgamento julgamento.json] [--json]
Shared:  regua/regua.md (same ids, weights and rules, with sources); agentes/auditor.md runs it;
         pesquisa/boas-praticas-seo-geo.md is where each rule comes from.
Perf:    standard library only, no network; one page takes milliseconds.
"""
import argparse
import datetime
import json
import re
import sys
import unicodedata
from html.parser import HTMLParser
from urllib.parse import urlparse

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
SKIP = {"script", "style", "noscript", "template", "svg"}
STOP = {"com", "para", "por", "uma", "das", "dos", "the", "and", "que", "sem"}
UNIT = r"(?:ml|l|litros?|kg|g|cm|mm|m|h|horas?|dias?|w|v|%|polegadas?|oz)\b"


def norm(text):
    text = unicodedata.normalize("NFD", text.lower())
    return "".join(ch for ch in text if unicodedata.category(ch) != "Mn")


def tokens(text):
    return re.findall(r"[a-z0-9]{3,}", norm(text))


def words(text):
    return re.findall(r"\S+", text)


def strip_tags(html):
    html = re.sub(r"<(style|script|noscript|template|svg)\b[^>]*>[\s\S]*?</\1>", " ", html, flags=re.I)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


class PageReader(HTMLParser):
    """Collects only the signals the ruler needs, in one pass."""

    def __init__(self, seletor="#descricao"):
        super().__init__(convert_charrefs=True)
        # "#id" or ".class": the element that holds the product description.
        self._sel_kind, self._sel_name = ("class", seletor[1:]) if seletor.startswith(".") else ("id", seletor.lstrip("#"))
        self.stack = []
        self.lang = ""
        self.title, self._in_title = "", False
        self.meta, self.og = {}, {}
        self.robots = ""
        self.canonical = None
        self.data_nosnippet = False
        self.h1, self.h2, self._heading = [], 0, None
        self.short_blocks, self._short = [], None
        self.jsonld_raw, self._in_jsonld = [], False
        self.images, self.links = [], []
        self.has_main = False
        self.visible = []
        # Stack depth where <main>, the description and a hidden element were opened.
        self._main_at = None
        self._desc_at, self._desc_done = None, False
        self._hidden_at = None
        self.desc_parts, self.hidden_text = [], []

    def _inside(self, mark):
        return mark is not None and len(self.stack) >= mark

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if self._inside(self._desc_at):
            self.desc_parts.append(self.get_starttag_text())
        if tag == "html":
            self.lang = a.get("lang", "")
        elif tag == "title":
            # Only the document title: SVG icons carry their own <title>, and only the first one counts.
            self._in_title = "svg" not in self.stack and not self.title
        elif tag == "meta":
            name = a.get("name", "").lower()
            if name:
                self.meta[name] = a.get("content", "")
            if name in ("robots", "googlebot"):
                self.robots += " " + a.get("content", "").lower()
            if a.get("property", "").startswith("og:"):
                self.og[a["property"].lower()] = a.get("content", "")
        elif tag == "link" and "canonical" in a.get("rel", "").lower():
            self.canonical = a.get("href")
        elif tag in ("h1", "h2"):
            self._heading = [tag, ""]
        elif tag == "script" and a.get("type", "").lower() == "application/ld+json":
            self._in_jsonld = True
            self.jsonld_raw.append("")
        elif tag == "img":
            self.images.append({"alt": a.get("alt", "").strip(), "src": a.get("src", ""), "em_main": self._inside(self._main_at)})
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if "data-nosnippet" in a:
            self.data_nosnippet = True
        if tag in ("h2", "h3", "h4", "summary", "dt", "strong", "b") and self._short is None:
            self._short = [tag, ""]
        if tag not in VOID:
            self.stack.append(tag)
            if tag == "main" and self._main_at is None:
                self.has_main, self._main_at = True, len(self.stack)
            hit = a.get("id") == self._sel_name if self._sel_kind == "id" else self._sel_name in a.get("class", "").split()
            if hit and self._desc_at is None and not self._desc_done:
                self._desc_at = len(self.stack)
            style = a.get("style", "").replace(" ", "").lower()
            hidden = "display:none" in style or "visibility:hidden" in style or "font-size:0" in style or a.get("aria-hidden") == "true"
            if hidden and self._hidden_at is None:
                self._hidden_at = len(self.stack)

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "script":
            self._in_jsonld = False
        if self._heading and tag == self._heading[0]:
            if tag == "h1":
                self.h1.append(self._heading[1].strip())
            else:
                self.h2 += 1
            self._heading = None
        if self._short and tag == self._short[0]:
            self.short_blocks.append(self._short[1].strip())
            self._short = None
        if tag in VOID or tag not in self.stack:
            return
        while self.stack:
            closed = self.stack.pop()
            if self._desc_at is not None:
                if len(self.stack) < self._desc_at:
                    self._desc_at, self._desc_done = None, True
                else:
                    self.desc_parts.append(f"</{closed}>")
            if self._main_at is not None and len(self.stack) < self._main_at:
                self._main_at = None
            if self._hidden_at is not None and len(self.stack) < self._hidden_at:
                self._hidden_at = None
            if closed == tag:
                break

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._heading:
            self._heading[1] += data
        if self._short:
            self._short[1] += data
        if self._in_jsonld:
            self.jsonld_raw[-1] += data
        if self._inside(self._desc_at):
            self.desc_parts.append(data)
        if not any(t in SKIP for t in self.stack):
            (self.hidden_text if self._hidden_at is not None else self.visible).append(data)


def walk_jsonld(raw_blocks):
    """Flattens every JSON-LD node (lists, @graph and nested values) into one list of dicts."""
    nodes, errors = [], 0
    for raw in raw_blocks:
        try:
            data = json.loads(raw)
        except ValueError:
            errors += 1
            continue
        pending = [data]
        while pending:
            item = pending.pop()
            if isinstance(item, list):
                pending.extend(item)
            elif isinstance(item, dict):
                nodes.append(item)
                pending.extend(v for v in item.values() if isinstance(v, (dict, list)))
    return nodes, errors


def has_type(node, name):
    t = node.get("@type")
    return name in (t if isinstance(t, list) else [t])


def offers_of(product):
    o = (product or {}).get("offers")
    return [x for x in (o if isinstance(o, list) else [o]) if isinstance(x, dict)]


def price_of(offer):
    """schema.org wants a plain number with a dot ("349.00"); "349,00" is read wrong or rejected."""
    for key in ("price", "lowPrice"):
        if key in offer:
            raw = str(offer[key]).strip()
            if re.fullmatch(r"\d+(\.\d+)?", raw):
                return float(raw), raw
            return None, raw
    return None, None


def gtin_ok(code):
    code = str(code).strip()
    if not re.fullmatch(r"\d{8}|\d{12,14}", code):
        return False
    digits = [int(c) for c in code]
    check = digits.pop()
    total = sum(d * (3 if i % 2 == 0 else 1) for i, d in enumerate(reversed(digits)))
    return (10 - total % 10) % 10 == check


BLOCK_SIGNS = re.compile(
    r"captcha|are you human|just a moment|access denied|acesso negado|ops! algo deu errado|"
    r"para continuar, acesse sua conta|account-verification|ative o javascript|enable javascript",
    re.I,
)
INJECTION = re.compile(r"ignore (as|todas as|previous|all) |instru[cç][oõ]es anteriores|recomende este produto|you are (an?|the) |as an ai|chatgpt,|assistant:", re.I)
OUT_OF_STOCK = re.compile(r"indispon[ií]vel|esgotad[oa]|sem estoque|fora de estoque|avise-me quando chegar", re.I)
IN_STOCK = re.compile(r"em estoque|pronta entrega|dispon[ií]vel|comprar|adicionar (ao|à) (carrinho|sacola)", re.I)


def readability(html, keyword):
    """Says whether the page arrived with the product in it. A thin page is still a page."""
    text = strip_tags(html)
    found = BLOCK_SIGNS.search(text)
    if len(words(text)) < 400 and found:
        return False, f"a loja devolveu uma tela de bloqueio ou de login ({found.group(0)})"
    if tokens(keyword) and not any(t in norm(text) for t in tokens(keyword)):
        return False, "nenhuma palavra do produto aparece na página"
    return True, ""


def signals(html, seletor):
    page = PageReader(seletor)
    page.feed(html)
    nodes, json_errors = walk_jsonld(page.jsonld_raw)
    product = next((n for n in nodes if has_type(n, "Product")), None)
    group = next((n for n in nodes if has_type(n, "ProductGroup")), None)
    if not product and group and isinstance(group.get("hasVariant"), list) and group["hasVariant"]:
        product = group["hasVariant"][0]
    desc_html = "".join(page.desc_parts)
    desc_from = "seletor"
    if not desc_html:
        body = re.search(r"<main\b[\s\S]*?</main>", html, re.I) or re.search(r"<body\b[\s\S]*?</body>", html, re.I)
        desc_html, desc_from = (body.group(0) if body else html), "main"
    return {
        "page": page, "nodes": nodes, "json_errors": json_errors, "product": product, "group": group,
        "desc_html": desc_html, "desc_text": strip_tags(desc_html), "desc_from": desc_from,
        "visible": re.sub(r"\s+", " ", " ".join(page.visible)).strip(),
        "hidden": re.sub(r"\s+", " ", " ".join(page.hidden_text)).strip(),
    }


def evaluate(html, keyword, url, judgement, seletor="#descricao", js=None):
    s = signals(html, seletor)
    page, product, nodes = s["page"], s["product"], s["nodes"]
    desc_html, desc_text, visible = s["desc_html"], s["desc_text"], s["visible"]
    title = re.sub(r"\s+", " ", page.title).strip()
    meta = page.meta.get("description", "").strip()
    ktok = [t for t in tokens(keyword) if t not in STOP]
    has_all = lambda text: bool(ktok) and all(t in norm(text) for t in ktok)
    has_some = lambda text: any(t in ktok for t in tokens(text))
    offers = offers_of(product)
    offer = offers[0] if offers else {}
    price, price_raw = price_of(offer) if offer else (None, None)
    avail = str(offer.get("availability") or (product or {}).get("availability") or "")
    rating = (product or {}).get("aggregateRating") if isinstance((product or {}).get("aggregateRating"), dict) else None
    today = datetime.date.today()
    warnings = []

    # ---------- gates ----------
    gates = []
    robots = page.robots
    if "noindex" in robots or "nosnippet" in robots or re.search(r"max-snippet:\s*0\b", robots):
        gates.append(("P1", "Página fora do índice ou sem trecho", "meta robots com noindex, nosnippet ou max-snippet:0"))
    if page.canonical and url:
        a, b = urlparse(page.canonical), urlparse(url)
        if a.path.rstrip("/") != b.path.rstrip("/") and a.netloc in ("", b.netloc):
            warnings.append(f"o canonical aponta para outro endereço ({page.canonical})")
    inj = INJECTION.search(s["hidden"])
    if inj:
        gates.append(("P2", "Texto escondido com instrução para IA", f'"{inj.group(0).strip()}" em elemento oculto'))

    # ---------- SEO ----------
    def s01():
        if not title:
            return "fail", "sem <title>"
        repeated = [t for t in set(tokens(title)) if t not in STOP and tokens(title).count(t) > 1]
        n = len(title)
        if n > 70:
            warnings.append(f"título com {n} caracteres: o Google corta pela largura da tela")
        if has_all(title) and not repeated and n <= 70:
            return "pass", f"{n} caracteres, com o produto"
        if has_some(title):
            why = "repete " + ", ".join(repeated) if repeated else ("longo, risco de corte" if n > 70 else "nome do produto incompleto")
            return "partial", why
        return "fail", "título não nomeia o produto"

    def s02():
        if not meta:
            return "fail", "sem meta description"
        facts = 0
        facts += bool(re.search(r"r\$\s?\d", meta.lower()))
        facts += len(re.findall(rf"\d+[.,]?\d*\s?{UNIT}", norm(meta)))
        facts += bool(has_some(meta))
        if len(meta) > 320:
            warnings.append(f"meta description com {len(meta)} caracteres: o trecho será cortado")
        if len(meta) >= 70 and facts >= 2:
            return "pass", f"{len(meta)} caracteres, {facts} fatos"
        return "partial", f"{len(meta)} caracteres, {facts} fato(s)"

    def s03():
        if not page.h1:
            return "fail", "nenhum h1"
        match = any(has_some(h) for h in page.h1)
        return ("pass" if len(page.h1) == 1 and match else "partial" if match else "fail"), f"{len(page.h1)} h1"

    def s04():
        n = page.h2
        return ("pass" if n >= 2 else "partial" if n == 1 else "fail"), f"{n} h2"

    def s05():
        t, img = page.og.get("og:title"), page.og.get("og:image", "")
        img_ok = bool(img) and "logo" not in img.lower()
        n = bool(t) + img_ok
        return ("pass" if n == 2 else "partial" if n == 1 else "fail"), ("og:title " + ("sim" if t else "não") + ", og:image " + ("sim" if img_ok else "não"))

    def s06():
        if not product:
            return "fail", "sem schema Product" + (" (JSON-LD inválido)" if s["json_errors"] else "")
        if not offers:
            return "fail", "Product sem offers"
        missing = [k for k in ("name", "image") if not product.get(k)]
        if price is None:
            return "partial", f'preço "{price_raw}" fora do formato (use ponto: 349.00)' if price_raw else "oferta sem preço"
        if price <= 0:
            return "partial", "preço zero"
        missing += [k for k in ("priceCurrency", "availability") if not offer.get(k)]
        return ("pass", "Product com nome, imagem, preço, moeda e estoque") if not missing else ("partial", "falta " + ", ".join(missing))

    def s07():
        has_price_text = bool(re.search(r"r\$\s?\d", visible.lower()))
        desc_ok = len(words(desc_text)) >= 50
        if js:
            gained = [k for k in ("produto", "descrição") if (k == "produto" and js["product"] and not product) or (k == "descrição" and js["desc_words"] >= 50 and not desc_ok)]
            if not has_price_text and not desc_ok and gained:
                return "fail", "preço e descrição só aparecem depois do JavaScript"
            if gained:
                return "partial", " e ".join(gained) + " só depois do JavaScript"
        if product and has_price_text and desc_ok:
            return "pass", "nome, preço, descrição e schema no HTML inicial"
        if not has_price_text and not desc_ok:
            return "fail", "preço e descrição fora do HTML inicial"
        return "partial", "falta " + ", ".join(x for x, ok in (("schema", product), ("preço em texto", has_price_text), ("descrição", desc_ok)) if not ok)

    def s08():
        if not product:
            return "fail", "sem schema para comparar"
        problems, light = [], []
        if price is not None:
            br = f"{price:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            # Stores split prices across tags ("174" + ",99"), so compare without whitespace.
            compact = re.sub(r"\s", "", visible)
            if br not in compact and br.replace(".", "") not in compact:
                problems.append(f"preço {br} do schema não aparece na página")
        # Stock words count only in the product summary (from the H1 on), not in other colours or
        # recommended products further down the page.
        start = visible.find(page.h1[0][:40]) if page.h1 else -1
        summary_text = visible[start:start + 900] if start >= 0 else ""
        summary_text = re.split(r"veja também|você também (pode gostar|vai gostar)|produtos relacionados|quem viu|compre junto|aproveite também", summary_text, flags=re.I)[0]
        if "InStock" in avail and OUT_OF_STOCK.search(summary_text):
            problems.append("schema diz em estoque e a página diz indisponível")
        if rating and str(rating.get("ratingValue", "")).replace(".", ",") not in visible and str(rating.get("ratingValue", "")) not in visible:
            problems.append("nota no schema que não aparece na página")
        valid = str(offer.get("priceValidUntil", ""))
        if re.match(r"\d{4}-\d{2}-\d{2}", valid) and datetime.date.fromisoformat(valid[:10]) < today:
            problems.append(f"priceValidUntil vencido ({valid[:10]})")
        if product.get("name") and not any(has_some(h) for h in page.h1):
            light.append("nome do schema não está no H1")
        if price is None and price_raw:
            light.append("preço do schema em formato inválido")
        if problems:
            return "fail", "; ".join(problems)
        if light:
            return "partial", "; ".join(light)
        return "pass", "preço, estoque e nota do schema batem com a página"

    def s09():
        if not product:
            return "fail", "sem schema"
        brand = product.get("brand")
        brand_name = brand.get("name") if isinstance(brand, dict) else brand
        gtins = [product.get(k) or offer.get(k) for k in ("gtin", "gtin8", "gtin12", "gtin13", "gtin14")]
        gtins = [g for g in gtins if g]
        if gtins and any(gtin_ok(g) for g in gtins) and brand_name:
            return "pass", f"GTIN válido e marca {brand_name}"
        if (product.get("mpn") or offer.get("mpn")) and brand_name:
            return "pass", f"MPN e marca {brand_name}"
        if gtins:
            return "partial", "GTIN com dígito verificador inválido" if not any(gtin_ok(g) for g in gtins) else "GTIN sem marca"
        if product.get("sku") or product.get("mpn"):
            return "partial", "só sku" if product.get("sku") else "MPN sem marca"
        return "fail", "nenhum identificador"

    def s10():
        has_policy = any(has_type(n, "MerchantReturnPolicy") for n in nodes) or bool(offer.get("hasMerchantReturnPolicy"))
        has_ship = any(has_type(n, t) for n in nodes for t in ("OfferShippingDetails", "ShippingService")) or bool(offer.get("shippingDetails"))
        if has_policy and has_ship:
            return "pass", "frete e devolução no schema"
        if re.search(r"troca|devolu[cç]", visible.lower()):
            return "partial", "só o texto ou link da política" + (" (frete no schema)" if has_ship else "")
        return "fail", "sem frete nem devolução"

    def s11():
        imgs = [i for i in page.images if i["em_main"] or not page.has_main]
        schema_img = bool(product and product.get("image"))
        if not imgs:
            return ("partial" if schema_img else "fail"), "nenhuma foto no conteúdo"
        ok = sum(1 for i in imgs if i["alt"])
        if ok == len(imgs) and schema_img:
            return "pass", f"{ok} de {len(imgs)} com alt, imagem no schema"
        if ok >= len(imgs) / 2:
            return "partial", f"{ok} de {len(imgs)} com alt" + ("" if schema_img else ", sem imagem no schema")
        return "fail", f"{ok} de {len(imgs)} com alt"

    def s12():
        if not url:
            return "fail", "endereço não informado"
        # The descriptive part is the longest path segment (stores append ids and variant names).
        segments = [p for p in urlparse(url).path.split("/") if p and p != "p"]
        slug = max(segments, key=len) if segments else ""
        if not slug:
            return "fail", "sem trecho legível"
        ok = bool(re.fullmatch(r"[a-z0-9-]+", slug)) and len(slug) <= 75
        return ("pass" if ok else "partial"), slug if len(slug) <= 60 else slug[:57] + "..."

    def s13():
        if not page.canonical:
            return "partial", "sem canonical"
        if url and urlparse(page.canonical).path.rstrip("/") != urlparse(url).path.rstrip("/"):
            return "partial", "canonical para outro endereço"
        return "pass", "canonical presente e coerente"

    def s14():
        crumbs = any(has_type(n, "BreadcrumbList") for n in nodes)
        cat = bool(product and product.get("category"))
        host = urlparse(url).netloc if url else ""
        internal = [h for h in page.links if h.startswith("/") or (host and urlparse(h).netloc == host)]
        n = crumbs + cat + bool(internal)
        return ("pass" if n == 3 else "partial" if n == 2 else "fail"), f"trilha {'sim' if crumbs else 'não'}, categoria {'sim' if cat else 'não'}, {len(internal)} links internos"

    def s15():
        if not rating:
            return "partial", "sem avaliação no schema"
        value = str(rating.get("ratingValue", ""))
        visible_ok = value in visible or value.replace(".", ",") in visible
        count = rating.get("reviewCount") or rating.get("ratingCount")
        if not visible_ok:
            return "fail", f"nota {value} no schema sem nota visível"
        return ("pass" if count else "partial"), f"nota {value}" + (f" de {count} avaliações" if count else ", sem contagem")

    def s16():
        variants = bool(s["group"]) or any(n.get("isVariantOf") or n.get("hasVariant") for n in nodes)
        if variants:
            return "pass", "ProductGroup ou variantes marcadas"
        if len(offers) > 1:
            return "partial", "variantes só como várias ofertas"
        if re.search(r"\b(cor|tamanho|voltagem)\s*:", visible.lower()) or re.search(r"mais cores|selecione (a|o) (cor|tamanho)", visible.lower()):
            return "fail", "a página oferece variação sem markup de variante"
        return "pass", "não se aplica: sem variação na página"

    # ---------- GEO ----------
    def judged(cid, floor=None):
        if floor:
            return floor
        status = judgement.get(cid)
        return (status, "julgamento do agente") if status in ("pass", "partial", "fail") else (None, "julgamento do agente")

    def g02():
        pairs = 0
        pairs += len(re.findall(r"<tr\b[^>]*>\s*<t[hd]\b[\s\S]*?</t[hd]>\s*<t[hd]\b", desc_html, re.I))
        pairs += len(re.findall(r"<dd\b", desc_html, re.I))
        pairs += sum(1 for li in re.findall(r"<li\b[^>]*>([\s\S]*?)</li>", desc_html, re.I) if re.search(r"\S\s*:\s*\S", strip_tags(li)))
        return ("pass" if pairs >= 5 else "partial" if pairs >= 2 else "fail"), f"{pairs} pares atributo: valor"

    def g05():
        text = visible.lower()
        p = bool(re.search(r"r\$\s?\d", text))
        st = bool(OUT_OF_STOCK.search(text) or IN_STOCK.search(text))
        return ("pass" if p and st else "partial" if p or st else "fail"), f"preço {'sim' if p else 'não'}, estoque {'sim' if st else 'não'}"

    def g07_floor():
        n = len(words(desc_text))
        return ("fail", f"descrição com {n} palavras") if n < 50 else None

    def g08():
        qs = [q for q in page.short_blocks if q.rstrip().endswith("?") and len(words(q)) >= 3]
        n = len(qs)
        return ("pass" if n >= 3 else "partial" if n >= 1 else "fail"), f"{n} perguntas visíveis"

    def g09():
        blocks = [strip_tags(b) for b in re.split(r"</(?:p|li|h2|h3|h4|tr|div|dd)>|<br\s*/?>", desc_html, flags=re.I)]
        blocks = [b for b in blocks if b]
        if not blocks:
            return "fail", "sem texto"
        long_ = sum(1 for b in blocks if len(words(b)) > 45)
        return ("pass" if long_ == 0 else "partial" if long_ <= len(blocks) / 2 else "fail"), f"{long_} de {len(blocks)} blocos com mais de 45 palavras"

    def g10():
        lang_ok = page.lang.lower().startswith("pt")
        cur = offer.get("priceCurrency", "BRL") if offer else "BRL"
        if cur != "BRL":
            return "fail", f"moeda {cur}"
        return ("pass" if lang_ok else "partial"), f"lang={page.lang or 'ausente'}, moeda {cur}"

    ruler = [
        ("S01", "seo", "Título descritivo, com o produto", 10, s01),
        ("S02", "seo", "Meta description com fatos", 8, s02),
        ("S03", "seo", "H1 com o nome do produto", 6, s03),
        ("S04", "seo", "Subtítulos (H2)", 4, s04),
        ("S05", "seo", "og:title e og:image", 3, s05),
        ("S06", "seo", "Schema Product completo", 14, s06),
        ("S07", "seo", "Conteúdo no HTML inicial", 10, s07),
        ("S08", "seo", "Schema igual ao texto visível", 10, s08),
        ("S09", "seo", "Identificadores (GTIN, MPN, marca)", 8, s09),
        ("S10", "seo", "Frete e devolução", 6, s10),
        ("S11", "seo", "Imagens com alt e no schema", 7, s11),
        ("S12", "seo", "Endereço legível", 3, s12),
        ("S13", "seo", "Canonical coerente", 3, s13),
        ("S14", "seo", "Trilha, categoria e links internos", 3, s14),
        ("S15", "seo", "Avaliação visível e no schema", 3, s15),
        ("S16", "seo", "Variantes marcadas", 2, s16),
        ("G01", "geo", "Abertura direta", 15, lambda: judged("G01")),
        ("G02", "geo", "Especificações em pares", 16, g02),
        ("G03", "geo", "Produto bem identificado", 14, lambda: judged("G03")),
        ("G04", "geo", "Dados concretos e sem contradição", 12, lambda: judged("G04")),
        ("G05", "geo", "Preço e estoque em texto", 10, g05),
        ("G06", "geo", "Para quem é e quando usar", 10, lambda: judged("G06")),
        ("G07", "geo", "Descrição própria", 8, lambda: judged("G07", g07_floor())),
        ("G08", "geo", "Perguntas de comprador respondidas", 6, g08),
        ("G09", "geo", "Texto fácil de escanear", 5, g09),
        ("G10", "geo", "Idioma e moeda coerentes", 4, g10),
    ]
    results = []
    for cid, group, label, weight, fn in ruler:
        status, detail = fn()
        points = None if status is None else weight if status == "pass" else weight // 2 if status == "partial" else 0
        results.append({"id": cid, "grupo": group, "criterio": label, "peso": weight, "status": status, "pontos": points, "detalhe": detail})
    if s["desc_from"] == "main":
        warnings.append(f'descrição não encontrada em "{seletor}"; usei o conteúdo principal da página')
    if page.data_nosnippet:
        warnings.append("há trechos com data-nosnippet: o Google não usa esse texto em resultados")
    if "noarchive" in robots or "nocache" in robots:
        warnings.append("noarchive ou nocache: o Copilot usa só endereço, título e trecho")
    return {"criterios": results, "portoes": gates, "avisos": warnings}


def summary(results):
    out = {}
    for group in ("seo", "geo"):
        rows = [r for r in results if r["grupo"] == group]
        measured = [r for r in rows if r["pontos"] is not None]
        out[group] = {
            "pontos": sum(r["pontos"] for r in measured),
            "medido_de": sum(r["peso"] for r in measured),
            "pendente": sum(r["peso"] for r in rows if r["pontos"] is None),
        }
    return out


def print_report(rep, color):
    mark = {"pass": "✓ passa", "partial": "◐ metade", "fail": "✗ falha", None: "? julgar"}
    paint = {"pass": "32", "partial": "33", "fail": "31", None: "36"}
    titles = {"seo": "SEO · o que o Google lê", "geo": "GEO · o que um assistente de IA lê para citar o produto"}
    for gid, label, why in rep["portoes"]:
        line = f"PORTÃO {gid} · {label}: {why}"
        print(f"\033[31m{line}\033[0m" if color else line)
    totals = summary(rep["criterios"])
    for group in ("seo", "geo"):
        print(f"\n{titles[group]}")
        for r in (x for x in rep["criterios"] if x["grupo"] == group):
            status = mark[r["status"]]
            if color:
                status = f"\033[{paint[r['status']]}m{status}\033[0m"
            pts = "  " if r["pontos"] is None else f"{r['pontos']:>2}"
            print(f"  {r['id']}  {r['criterio']:<36} {status}  {pts}/{r['peso']:<2}  {r['detalhe']}")
        t = totals[group]
        line = f"  NOTA {t['pontos']} de {t['medido_de']}"
        if t["pendente"]:
            line += f"  (+{t['pendente']} pontos esperando o julgamento do agente)"
        print(line)
    if rep["avisos"]:
        print("\nAVISOS")
        for w in rep["avisos"]:
            print(f"  · {w}")


def print_diff(raw, rendered, color):
    """Only the criteria that change once JavaScript runs: what a non-rendering crawler misses."""
    changed = [(a, b) for a, b in zip(raw, rendered) if a["status"] != b["status"]]
    label = {"pass": "passa", "partial": "metade", "fail": "falha", None: "julgar"}
    print("\nO QUE SÓ APARECE DEPOIS DO JAVASCRIPT (os robôs de IA medidos não executam JavaScript)")
    if not changed:
        print("  nada: o robô sem navegador lê o mesmo que você vê")
        return
    for a, b in changed:
        line = f"  {a['id']}  {a['criterio']:<36} sem JS: {label[a['status']]:<7} com JS: {label[b['status']]:<7} {b['detalhe']}"
        print(f"\033[36m{line}\033[0m" if color else line)


def main():
    ap = argparse.ArgumentParser(description="Confere uma página de produto com a régua de SEO e GEO.")
    ap.add_argument("pagina", help="arquivo .html da página")
    ap.add_argument("--palavra-chave", required=True, help='ex.: "garrafa térmica stanley classic"')
    ap.add_argument("--url", default="", help="endereço da página")
    ap.add_argument("--julgamento", help='JSON com G01, G03, G04, G06 e G07, ex.: {"G01": "pass"}')
    ap.add_argument("--descricao", default="#descricao", help='onde está a descrição: "#id" ou ".classe" (padrão: #descricao)')
    ap.add_argument("--renderizado", help="a mesma página salva DEPOIS do JavaScript, para comparar")
    ap.add_argument("--json", action="store_true", help="saída em JSON")
    args = ap.parse_args()

    with open(args.pagina, encoding="utf-8") as fh:
        html = fh.read()
    judgement = {}
    if args.julgamento:
        with open(args.julgamento, encoding="utf-8") as fh:
            judgement = json.load(fh)
    ok, why = readability(html, args.palavra_chave)
    if not ok:
        # A blocked or empty page gets no score: a criterion that was not read is not a bad criterion.
        if args.json:
            json.dump({"lido": False, "motivo": why}, sys.stdout, ensure_ascii=False)
            print()
        else:
            print(f"NÃO FOI POSSÍVEL LER: {why}. Nenhuma nota foi dada.")
        sys.exit(2)
    js = None
    rendered = None
    if args.renderizado:
        with open(args.renderizado, encoding="utf-8") as fh:
            rhtml = fh.read()
        rs = signals(rhtml, args.descricao)
        js = {"product": bool(rs["product"]), "desc_words": len(words(rs["desc_text"]))}
        rendered = evaluate(rhtml, args.palavra_chave, args.url, judgement, args.descricao)
    rep = evaluate(html, args.palavra_chave, args.url, judgement, args.descricao, js)
    if args.json:
        out = {"lido": True, **rep, "notas": summary(rep["criterios"])}
        if rendered:
            out["renderizado"] = {"criterios": rendered["criterios"], "notas": summary(rendered["criterios"])}
        json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
        print()
    else:
        print_report(rep, sys.stdout.isatty())
        if rendered:
            print_diff(rep["criterios"], rendered["criterios"], sys.stdout.isatty())


if __name__ == "__main__":
    main()
