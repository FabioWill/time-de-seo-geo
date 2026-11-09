# Boas práticas de SEO e GEO para página de produto

Pesquisa feita em 09/11/2026 para o post 14 e para o repositório público. A pergunta: o que, numa
página de produto de e-commerce, ajuda a aparecer no Google (SEO) e a ser encontrado, citado e
recomendado por buscadores com IA (GEO: Google AI Overviews e AI Mode, ChatGPT, Perplexity,
Gemini, Copilot). E, a partir disso, o que manter, mudar e acrescentar na régua de 23 critérios
(C01 a C23, em `repo/regua/regua.md`).

## Como ler

- **Data de leitura.** Todas as fontes foram abertas em 09/11/2026. Quando a página informa a
  data da última atualização, ela aparece como "atualizada em".
- **Nível de evidência.**
  - **doc oficial:** documentação ou blog da própria plataforma (Google, Microsoft, OpenAI,
    Perplexity, schema.org). Diz o que a plataforma afirma fazer. Não é medição independente.
  - **estudo:** pesquisa com método e dados descritos. Marco **acadêmico** (revisado por pares
    ou preprint) ou **fornecedor** (empresa que vende ferramenta de SEO e tem interesse no tema).
  - **opinião de mercado:** recomendação que circula sem dado publicado que a sustente.
- **Medível no HTML.** **sim**: um script decide sozinho lendo o HTML (cru ou renderizado).
  **parcial**: o código acha o sinal, mas precisa de julgamento, de outra requisição ou de dado
  de fora da página. **não**: o sinal vive fora da página (feed, painel, reputação).
- Citações ficam no idioma original, entre aspas, copiadas do texto lido. Os códigos entre
  colchetes ([G1], [R2] etc.) apontam para a lista de fontes no fim.

## Resumo

1. Google e Microsoft dizem, por escrito, que aparecer nas respostas com IA depende das mesmas
   bases do SEO. O Google: "There are no additional requirements to appear in AI Overviews or
   AI Mode, nor other special optimizations necessary" [G1]. O Bing: "SEO Fundamentals Still
   Apply to Grounding and AI Experiences" [M1].
2. O pré-requisito no Google é a página estar indexada **e elegível a trecho** (snippet). Um
   `nosnippet` tira a página dos recursos de IA [G1].
3. O rich result de FAQ acabou para todos os sites em 07/05/2026, e a documentação foi removida
   em 15/06/2026 [G3]. O C18 e o C23 da régua premiam um markup que o Google não exibe mais.
4. O Google diz que não existe schema "para IA" e que `llms.txt` não ajuda nem atrapalha [G2].
   O único estudo controlado encontrado (fornecedor) não viu ganho de citação ao adicionar JSON-LD [V1].
5. Título de 50 a 60 e meta de 120 a 158 caracteres não são regra do Google: "there's no limit",
   o texto é cortado pela largura da tela [G11] [G12]. Contagem de palavras também não: "(No, we
   don't.)" [G13].
6. O que as fontes oficiais pedem e a régua ainda não mede: conteúdo no HTML inicial (sem depender
   de JavaScript), schema igual ao texto visível, identificadores (GTIN, MPN, marca), políticas de
   frete e devolução, variantes com `ProductGroup`, imagens de boa resolução [G4] [G6] [G10] [M1].
7. O artigo do GEO (KDD 2024) mediu até 40% mais visibilidade com citações, falas e estatísticas,
   mas num motor simulado e em consultas genéricas [R1]. O C-SEO Bench (NeurIPS 2025) testou os
   mesmos métodos em recomendação de produto e achou efeito nulo ou negativo; o que funcionou foi
   melhorar a posição do documento, ou seja, SEO [R2].
8. Em e-commerce, os dois estudos controlados mais recentes apontam na mesma direção: relevância
   para a busca, preço explícito, especificações completas, resumo de abertura, casos de uso e
   factualidade pesam; formatação sozinha quase não pesa [R3] [R4].
9. Para ChatGPT e Copilot, o caminho oficial de produto é o **feed** (no ChatGPT ele é opcional,
   porque o robô também lê o site), e o shopping do ChatGPT está no ar só nos EUA [O2] [M5]. No
   Google, o feed do Merchant Center é citado como caminho para produtos em respostas de IA [G2].
10. No Brasil: AI Mode em português desde 08/09/2025 [G28]; Merchant Center exige frete configurado
    para o Brasil [G24]; o shopping do ChatGPT, o checkout por agente do Google e do Copilot e o
    relatório de IA do Merchant Center não tinham chegado ao país na data desta pesquisa [G26]
    [G27] [O2] [M5].

---

## 1. O que cada plataforma diz, com as palavras dela

### Google Search Central

- Requisito técnico: "To be eligible to be shown as a supporting link in AI Overviews or AI Mode,
  a page must be indexed and eligible to be shown in Google Search with a snippet, fulfilling the
  Search technical requirements. There are no additional technical requirements." [G1]
- Nada de arquivo ou schema especial: "You don't need to create new machine readable files, AI
  text files, or markup to appear in these features. There's also no special schema.org structured
  data that you need to add." [G1]
- Lista de fundamentos que o próprio Google repete para IA: "Ensuring that crawling is allowed in
  robots.txt, and by any CDN or hosting infrastructure", "Making sure that important content is
  available in textual form", "Making sure your structured data matches the visible text on the
  page", "Checking that your Merchant Center and Business Profile information is up-to-date" [G1].
- Guia de otimização para IA (criado em 15/05/2026, atualizado em 10/07/2026): "From Google
  Search's perspective, optimizing for generative AI search is optimizing for the search
  experience, and thus still SEO." [G2]
- No mesmo guia, um requisito novo: "a site must be included in Search generative AI features in
  Search Console to be eligible for display in generative AI features on Google Search." [G2] O
  controle é de exclusão: o padrão é incluído, e excluir "isn't used as a ranking or inclusion
  signal affecting other parts of Search" (lido pela ferramenta de leitura da página de ajuda,
  liberado para todos os sites em 31/08/2026) [G21].
- Para e-commerce: "Using products like Merchant Center (such as Merchant Center feeds) and Google
  Business Profiles can help your products and services to be visible in both AI responses and
  other Google Search results." [G2]
- Sobre conteúdo: "Creating content that people find unique, compelling, and useful will likely
  influence your website's presence in generative AI search in the long run more than any of the
  other suggestions in this guide." e "Don't just recycle what others on the internet have already
  said, or could easily be produced by a generative AI model." [G2]
- Sobre dados estruturados em produto: "If you're a merchant optimizing for all types of shopping
  results, we recommend putting Product structured data in the initial HTML for best results." e
  "dynamically-generated markup can make Shopping crawls less frequent and less reliable, which
  can be an issue for fast-changing content like product availability and price." [G4]
- Sobre IA escrevendo o conteúdo: "It is critical to manually factcheck and review all
  AI-generated content for accuracy and trustworthiness before publishing. This review also
  applies to metadata like <title> elements, meta description elements, structured data, and
  alternate texts for images" [G17].

### Microsoft Bing e Copilot

A página de diretrizes do Bing (sem data, lida em 09/11/2026) é hoje a fonte oficial mais
explícita sobre conteúdo para respostas com IA, e usa o termo GEO: "Generative Engine Optimization
(GEO) focuses on content eligibility for grounding and reference in AI responses. SEO does not
guarantee rankings or traffic, and GEO does not guarantee grounding or citations in AI
experiences." [M1] Os itens que tocam página de produto:

- Item 15: "URLs are more likely to be selected for grounding queries and citations when content
  stands on its own. Ensure: Facts and definitions are explicit; Key statements do not rely on
  implied content; Important information is visible on the URL itself" [M1].
- Item 16: "Use clear and consistent naming for people, organizations, products, and locations.
  Avoid ambiguous references." [M1]
- Item 18: "Place essential information near the top of the URL. Avoid long introductions before
  addressing the main topic." [M1]
- Item 14: "Structured data may support clearer grounding but does not guarantee visibility or
  grounding traffic. Markup must accurately reflect visible content." [M1]
- Item 8, o que evitar: "Hiding critical content behind client-side rendering" [M1].
- Item 13: "Missing, duplicate, or overly short title tags and meta descriptions may reduce
  indexing reliability, ranking, and eligibility for grounding results and citations." [M1]
- Item 10: "NOARCHIVE prevents content from being used in Copilot responses and grounding
  results. NOCACHE limits Copilot to using only the URL, title, and snippet" [M1].
- Abuso: "Attempts to add content designed to manipulate or interfere with language models used
  by Bing or Copilot may result in reduced visibility or removal from search experiences." [M1]

### OpenAI (ChatGPT)

- Robôs independentes: "Each setting is independent of the others", e o próprio exemplo da
  OpenAI é que "a webmaster can allow OAI-SearchBot in order to appear in search results while
  disallowing GPTBot" [O1].
- "Sites that are opted out of OAI-SearchBot will not be shown in ChatGPT search answers, though
  can still appear as navigational links." Mudança no robots.txt leva "~24 hours" [O1].
- `ChatGPT-User` age a pedido do usuário: "Because these actions are initiated by a user,
  robots.txt rules may not apply." [O1]
- Shopping: "Shopping is currently live for ChatGPT users in the U.S." e "If you sell through
  Shopify or Etsy, your catalog is already integrated" [O2]. Feed precisa de aprovação:
  "Onboarding product feeds in ChatGPT is currently available to approved partners." [O3]
- Feed não é obrigatório: "Do I need a product feed if ChatGPT already crawls my site? No, but
  feeds give you greater control over how your products appear" [O2].
- Checkout: "We're moving away from a standalone Instant Checkout experience in ChatGPT" e "There
  are no fees on purchases that start in ChatGPT." [O2]
- Texto do feed: "Use concise, factual copy that helps users understand products." [O4]

### Perplexity

- "PerplexityBot is designed to surface and link websites in search results on Perplexity. It is
  not used to crawl content for AI foundation models." [P1]
- "Since a user requested the fetch, this fetcher generally ignores robots.txt rules." (sobre o
  `Perplexity-User`) [P1]
- Programa de lojistas: o post de lançamento (18/11/2024) diz "This program is free for
  merchants" e que os varejistas "share their product specs with us" [P2]. Em 09/11/2026 a página
  `perplexity.ai/merchants` não descreve mais esse programa [P3]. Não confirmei o estado atual.

### schema.org

Versão em vigor na leitura: V30.1, de 16/09/2026 [S1]. `Product` e `Offer` aceitam
`hasMerchantReturnPolicy`, `shippingDetails`, `gtin`, `hasCertification` e `hasShippingService`;
`Product` aceita `isVariantOf`, `positiveNotes` e `negativeNotes`; `ProductGroup` define
`productGroupID`, `variesBy` e `hasVariant` [S1] [S2] [S5]. O schema.org define o vocabulário. Quem
decide o que vira resultado é cada buscador.

---

## 2. Tabela de práticas

Todas as fontes desta seção foram lidas em 09/11/2026.

### A. Elegibilidade e rastreamento

| # | Prática | Frente | Evidência | Fonte e data de leitura | Medível no HTML | Como medir por código |
|---|---|---|---|---|---|---|
| A1 | Página indexável e elegível a trecho: HTTP 200, sem `noindex`, sem `nosnippet`, sem `max-snippet:0` | ambos | doc oficial | [G1] https://developers.google.com/search/docs/appearance/ai-features (atualizada em 10/12/2025; lida em 09/11/2026); [M1] item 10 (lida em 09/11/2026) | sim | status HTTP, `<meta name="robots">`, cabeçalho `X-Robots-Tag`, `data-nosnippet` envolvendo a descrição |
| A2 | Não bloquear os robôs de busca no robots.txt nem na CDN ou WAF: Googlebot, Bingbot, OAI-SearchBot, PerplexityBot | ambos | doc oficial | [G1]; [O1] https://developers.openai.com/api/docs/bots (sem data; lida em 09/11/2026); [P1] https://docs.perplexity.ai/docs/resources/perplexity-crawlers (sem data; lida em 09/11/2026) | parcial | ler `/robots.txt` e avaliar as regras para cada user agent no caminho da página; bloqueio de WAF só aparece com o IP do robô, que um script externo não tem |
| A3 | Nome, preço, disponibilidade, descrição e JSON-LD `Product` no HTML inicial, sem depender de JavaScript | ambos | doc oficial; estudo (fornecedor) | [G4] https://developers.google.com/search/docs/appearance/structured-data/merchant-listing (atualizada em 08/09/2026; lida em 09/11/2026); [M1] item 8; [V4] https://vercel.com/blog/the-rise-of-the-ai-crawler (17/12/2024; lida em 09/11/2026) | sim | comparar o HTML cru (GET simples) com o HTML renderizado; reprovar se preço ou descrição só existem depois do JavaScript |
| A4 | Informação importante em texto, visível na própria URL, sem ficar escondida em aba ou acordeão fechado | ambos | doc oficial | [G1]; [G12] https://developers.google.com/search/docs/appearance/snippet (atualizada em 20/04/2026; lida em 09/11/2026), seção "Read more"; [M1] itens 12 e 15 | parcial | texto principal presente no DOM e fora de nós com `hidden`, `display:none` ou `aria-hidden`; texto dentro de imagem exige OCR |
| A5 | Uma URL canônica por produto e uma URL por moeda; variante pré-selecionável por parâmetro | SEO | doc oficial | [G4]; [G6] https://developers.google.com/search/docs/appearance/structured-data/product-variants (atualizada em 08/09/2026; lida em 09/11/2026); [M1] item 6 | sim | `rel=canonical` absoluto e coerente com a URL; em variantes, testar se `?cor=` troca imagem, preço e estoque |
| A6 | Site incluído no controle "Search generative AI" do Search Console (o padrão é incluído) | GEO | doc oficial | [G2] https://developers.google.com/search/docs/fundamentals/ai-optimization-guide (atualizada em 10/07/2026; lida em 09/11/2026); [G21] https://support.google.com/webmasters/answer/16908024 (lida em 09/11/2026) | não | só no Search Console |

### B. Título, meta, cabeçalhos e URL

| # | Prática | Frente | Evidência | Fonte e data de leitura | Medível no HTML | Como medir por código |
|---|---|---|---|---|---|---|
| B1 | `<title>` descritivo e conciso, diferente em cada página, sem palavra repetida; não existe limite de caracteres, existe corte pela largura da tela | SEO | doc oficial | [G11] https://developers.google.com/search/docs/appearance/title-link (atualizada em 10/12/2025; lida em 09/11/2026) | sim | presença; duplicação entre SKUs do catálogo; termo repetido; largura estimada (estimativa, o Google não publica número) |
| B2 | Título no mesmo idioma e alfabeto da página | SEO | doc oficial | [G11] | sim | `lang` do `<html>` e detecção de idioma do título e do corpo |
| B3 | Título principal em `<h1>` visível e destacado | SEO | doc oficial | [G11] ("putting the title text in the first visible <h1> element"); [M1] item 13 | sim | primeiro `<h1>` visível contém o nome do produto |
| B4 | Meta description única que junta os fatos do produto (preço, fabricante, atributo); sem limite oficial de tamanho | SEO | doc oficial | [G12]; [M1] item 13 (ausente, duplicada ou curta demais prejudica) | sim | presença, duplicação no catálogo, presença de fatos da ficha, ausência de lista de palavras |
| B5 | `og:title` e `og:image`: o Google usa `og:title` entre as fontes do título e `og:image` como imagem preferida; não usar logo | SEO | doc oficial | [G11]; [G14] https://developers.google.com/search/docs/appearance/google-images (atualizada em 02/03/2026; lida em 09/11/2026) | sim | as duas tags presentes; URL da imagem absoluta e diferente do logo do site |
| B6 | Subtítulos que organizam a página por seções | ambos | doc oficial | [G2]; [M1] item 13 | sim | contagem e hierarquia de `<h2>`/`<h3>` |
| B7 | URL com palavras legíveis separadas por hífen | SEO | doc oficial | [G15] https://developers.google.com/search/docs/crawling-indexing/url-structure (atualizada em 21/10/2026; lida em 09/11/2026) | sim | slug só com letras, números e hífens; sem ID longo |
| B8 | Links internos rastreáveis (`<a href>`) e trilha de navegação | ambos | doc oficial | [G1]; [M1] item 5; [G29] https://developers.google.com/search/docs/appearance/structured-data/search-gallery (atualizada em 16/10/2026; lida em 09/11/2026), Breadcrumb | sim | `<a href>` para a mesma loja; JSON-LD `BreadcrumbList` |

### C. Dados estruturados de produto

| # | Prática | Frente | Evidência | Fonte e data de leitura | Medível no HTML | Como medir por código |
|---|---|---|---|---|---|---|
| C1 | `Product` com `name`, `image` e `offers` (`price` maior que zero e `priceCurrency`) para merchant listing | SEO | doc oficial | [G4] ("merchant listing experiences require a price greater than zero") | sim | validar campos obrigatórios no JSON-LD |
| C2 | `Offer` com `availability`, `itemCondition` e `priceValidUntil` que não esteja vencido | SEO | doc oficial | [G4] ("Your listing may not display if the priceValidUntil property indicates a past date") | sim | enumeração válida; data no futuro ou ausente |
| C3 | Identificadores: GTIN na forma numérica e o mais específico, MPN, uma só `brand.name`, `sku` sem espaço | ambos | doc oficial | [G4] ("Include all applicable global identifiers"); [G23] https://support.google.com/merchants/answer/7052112 (lida em 09/11/2026); [G24] https://support.google.com/merchants/answer/13889434 (lida em 09/11/2026); [M1] item 16 | sim | presença e dígito verificador do GTIN |
| C4 | Política de devolução e de frete no `Organization` (padrão da loja) ou no `Offer` (exceção), ou configurada no Merchant Center ou no Search Console | SEO | doc oficial | [G4]; [G7] https://developers.google.com/search/docs/appearance/structured-data/shipping-policy (atualizada em 08/09/2026; lida em 09/11/2026); [G8] https://developers.google.com/search/docs/appearance/structured-data/return-policy (atualizada em 08/09/2026; lida em 09/11/2026) | parcial | o HTML mostra o markup e o link para a política; configuração no Merchant Center não aparece na página |
| C5 | Variantes com `ProductGroup` (`productGroupID`, `variesBy`, `hasVariant`) e ID único por variante | SEO | doc oficial | [G6] | sim | quando a página tem seletor de cor ou tamanho, exigir `ProductGroup` ou `isVariantOf` |
| C6 | `category` em texto ou `CategoryCode` da taxonomia do Google | SEO | doc oficial | [G4]; [G3] https://developers.google.com/search/updates (entrada de 07/07/2026; lida em 09/11/2026) | sim | presença e formato |
| C7 | Dados estruturados iguais ao texto visível: nome, preço, moeda, disponibilidade, nota | ambos | doc oficial | [G1]; [G10] https://developers.google.com/search/docs/appearance/structured-data/sd-policies (atualizada em 10/07/2026; lida em 09/11/2026) ("Don't mark up content that is not visible to readers of the page"); [M1] item 14 | sim | normalizar `offers.price` e procurar no texto no formato brasileiro (R$ 1.234,56); comparar disponibilidade e nota |
| C8 | JSON-LD como formato (recomendado pelo Google, não obrigatório) | SEO | doc oficial | [G30] https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data (atualizada em 10/12/2025; lida em 09/11/2026) | sim | `<script type="application/ld+json">` válido |

### D. Conteúdo do produto

| # | Prática | Frente | Evidência | Fonte e data de leitura | Medível no HTML | Como medir por código |
|---|---|---|---|---|---|---|
| D1 | Conteúdo próprio, que não é cópia do fabricante nem de outra página da loja | ambos | doc oficial | [G2]; [G13] https://developers.google.com/search/docs/fundamentals/creating-helpful-content (atualizada em 05/10/2026; lida em 09/11/2026); [M1] (scraped content) | parcial | similaridade entre descrições do catálogo; comparar com o texto do fabricante exige ter esse texto |
| D2 | Informação essencial no topo: a primeira frase diz o que é o produto | ambos | doc oficial; estudo (acadêmico) | [M1] item 18; [R3] https://arxiv.org/abs/2511.20867 (v2 de 14/07/2026; lida em 09/11/2026), "Opening summary" entre os traços que emergiram no prompt otimizado | parcial | julgamento; heurística: primeira frase com categoria, marca ou modelo e um dado |
| D3 | Entidade clara e consistente: marca, linha ou modelo, categoria, material ou capacidade | GEO | doc oficial | [M1] item 16; [G4] (`brand`, `gtin`, `mpn`) | parcial | marca e modelo iguais no H1, no texto e no JSON-LD; categoria exige julgamento |
| D4 | Fatos explícitos e verificáveis na própria página: medidas, capacidade, compatibilidade | GEO | doc oficial; estudo (acadêmico) | [M1] item 15; [R4] https://arxiv.org/abs/2605.25517 (25/05/2026; lida em 09/11/2026), "Missing Specifications" entre os fatores de completude; [R6] https://arxiv.org/abs/2604.25707 (29/04/2026; lida em 09/11/2026), descritivo | parcial | contar números com unidade e pares atributo:valor; "promessa vaga" exige julgamento |
| D5 | Preço explícito no texto | GEO | estudo (acadêmico, autores da indústria) | [R4] (preço entre os quatro fatores dominantes) | sim | preço legível no texto do HTML inicial |
| D6 | Especificações em lista, tabela ou pares atributo:valor | ambos | doc oficial; estudo (acadêmico) | [G23] (atributo `product_detail` do feed); [R3] | sim | contar linhas de `<table>`, itens de `<dl>` e `<li>` com dois-pontos |
| D7 | Para quem é, quando usar e como se compara com alternativas | GEO | estudo (acadêmico) | [R3] ("Use cases"); [R4] ("No Comparisons" é fator de completude) | parcial | julgamento |
| D8 | Perguntas reais de comprador respondidas no texto visível | GEO | estudo (acadêmico), com resultado contrário em [R6]; doc oficial do feed | [R3] ("User questions (FAQ)"); [R6] ("Q&A formatting alone does not improve absorption"); [G23] (atributo `question_and_answer`) | parcial | contar pares pergunta e resposta visíveis; qualidade da resposta exige julgamento |
| D9 | Texto organizado em parágrafos e seções, sem obrigação de picotar | ambos | doc oficial; estudo (acadêmico) | [G2] (organizar por seções; e "There's no requirement to break your content into tiny pieces"); [R4] ("formatting-only edits have little impact") | sim | tamanho dos blocos e presença de subtítulos |
| D10 | Não escrever por contagem de palavras nem por densidade de palavra-chave | ambos | doc oficial; estudo (acadêmico) | [G13] ("(No, we don't.)"); [G2] ("There's no ideal page length"); [G11] (keyword stuffing); [R1] https://arxiv.org/abs/2311.09735 (v3 de 28/06/2024; lida em 09/11/2026) | sim | detectar repetição anormal, não premiar contagem |
| D11 | Texto escrito por IA revisado por pessoa, incluindo title, meta, schema e alt | ambos | doc oficial | [G17] https://developers.google.com/search/docs/fundamentals/using-gen-ai-content (atualizada em 01/10/2026; lida em 09/11/2026) | não | processo editorial |

### E. Imagens

| # | Prática | Frente | Evidência | Fonte e data de leitura | Medível no HTML | Como medir por código |
|---|---|---|---|---|---|---|
| E1 | `alt` descritivo nas fotos do produto | ambos | doc oficial | [G14]; [M1] item 12 | sim | todas as fotos de conteúdo com `alt` não vazio e diferente do nome do arquivo |
| E2 | Várias imagens rastreáveis de alta resolução no schema (mínimo de 50 mil pixels, largura vezes altura), nas proporções 16x9, 4x3 e 1x1 | SEO | doc oficial | [G4] | parcial | exige baixar as imagens para medir |
| E3 | Imagem preferida via `og:image` ou `primaryImageOfPage`, sem logo e sem texto na imagem | SEO | doc oficial | [G14] (atualização de 02/03/2026) | parcial | URL diferente do logo é sim; "imagem com texto" exige visão computacional |

### F. Avaliações

| # | Prática | Frente | Evidência | Fonte e data de leitura | Medível no HTML | Como medir por código |
|---|---|---|---|---|---|---|
| F1 | `aggregateRating` só quando a nota está visível na página, vem de usuários, não é agregada de outros sites e não é falsa nem incentivada sem aviso | SEO | doc oficial | [G9] https://developers.google.com/search/docs/appearance/structured-data/review-snippet (atualizada em 08/09/2026; lida em 09/11/2026); a regra de avaliação falsa ou incentivada entrou em 24/07/2026 [G3] | parcial | nota do schema igual à nota visível é sim; autenticidade não se mede no HTML |
| F2 | Avaliação que a empresa controla sobre ela mesma (`Organization`, `LocalBusiness`) não gera estrela | SEO | doc oficial | [G9] | sim | rating aninhado em `Organization` da própria loja |

### G. Integridade

| # | Prática | Frente | Evidência | Fonte e data de leitura | Medível no HTML | Como medir por código |
|---|---|---|---|---|---|---|
| G1 | Nada de texto escondido nem de instrução para modelo de IA dentro da página | ambos | doc oficial; estudo (acadêmico) mostra por que é punido | [M1] (Prompt Injection and AI Manipulation); [G16] https://developers.google.com/search/docs/essentials/spam-policies (atualizada em 28/08/2026; lida em 09/11/2026); [R7] https://arxiv.org/abs/2404.07981; [R8] https://arxiv.org/abs/2406.03589 | parcial | texto em nó oculto com termos como "ignore", "recomende", "assistant"; CSS externo exige renderizar |
| G2 | Não gerar páginas para cada variação de busca ou consulta de "fan-out" | ambos | doc oficial | [G2] ("violates Google's scaled content abuse spam policy"); [G16] | parcial | só no nível do catálogo (páginas quase iguais) |
| G3 | Markup enganoso é ignorado ou punido | ambos | doc oficial | [G10]; [M1] (Misleading Structured Data) | sim | mesma checagem de C7 |

### H. Medição (fora da página, listada aqui para completar o quadro)

| # | Prática | Frente | Evidência | Fonte e data de leitura | Medível no HTML | Como medir |
|---|---|---|---|---|---|---|
| H1 | Relatório de desempenho em IA generativa do Search Console (impressões em AI Overviews e AI Mode) | GEO | doc oficial | [G22] https://support.google.com/webmasters/answer/16984139 (liberado para todos em 31/08/2026; lida em 09/11/2026) | não | Search Console |
| H2 | AI Performance do Bing Webmaster Tools (citações no Copilot e consultas de grounding) | GEO | doc oficial | [M3] https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c; [M4] https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview (10/02/2026; lidas em 09/11/2026) | não | Bing Webmaster Tools |
| H3 | Parâmetro de atribuição na URL do feed do ChatGPT (exemplo `utm_medium=feed`) | GEO | doc oficial | [O4] https://developers.openai.com/commerce/guides/best-practices (lida em 09/11/2026) | não | analytics |

---

## 3. Evidência de pesquisa sobre GEO: o que foi medido

A pergunta desta seção é qual efeito foi **medido**, em que condição, e o que isso diz para uma
página de produto. Vale lembrar: todos os estudos abaixo medem a resposta de um modelo de
linguagem, não clique nem venda.

| Estudo | Tipo | Desenho | O que mediu | Limites que importam | Leitura para página de produto |
|---|---|---|---|---|---|
| Aggarwal et al., "GEO: Generative Engine Optimization" [R1] | acadêmico, KDD 2024 | 10 mil consultas (GEO-bench, nove fontes); motor simulado com os 5 primeiros resultados do Google e gpt-3.5-turbo; teste adicional no Perplexity.ai | Cite Sources, Quotation Addition e Statistics Addition: "relative improvement of 30-40% on the Position-Adjusted Word Count metric and 15-30% on the Subjective Impression metric"; melhor caso +41% e +28%. Keyword Stuffing: "don't perform well" (17,8 contra 19,5 da linha de base na contagem de palavras). Tom autoritário: "we find no significant improvement". No Perplexity.ai: até 37%. Site na 5ª posição: +115,1% com Cite Sources, enquanto o 1º caiu 30,3% em média | consultas genéricas, não de compra; modelo de 2023; um site otimizado por vez; mede palavras do site na resposta | é a origem do "acrescente estatística e citação". Em produto, o equivalente defensável é ficha técnica real, nunca número inventado |
| Puerto et al., "C-SEO Bench" [R2] | acadêmico, NeurIPS 2025 (Datasets and Benchmarks) | 2 tarefas (resposta a perguntas e recomendação de produto), 6 domínios, 16,3 mil documentos, vários modelos, de um a dez concorrentes otimizando | "most current C-SEO methods are not only largely ineffective but also frequently have a negative impact on document ranking"; "traditional SEO strategies, those aiming to improve the ranking of the source in the LLM context, are significantly more effective". No GPT-4o-mini, domínio Retail: Statistics -0,07, Citations -0,01, Quotes +0,06 posição (sem significância), contra +2,77 do "Best SEO". No Haiku 3.5, Retail: -0,82, -0,49 e -0,50. Mais adotantes, menos ganho | ambiente controlado, documentos injetados; só métodos de "chapéu branco" | é o teste mais direto dos métodos do GEO em recomendação de produto, e eles não funcionaram. Posição na busca continua sendo o que mais pesa |
| Bagga et al., "E-GEO" [R3] | acadêmico (MIT e Columbia), preprint, v2 de 14/07/2026 | 13.747 consultas de compra realistas (montadas a partir do fórum r/BuyItForLife), cada uma com 10 anúncios da Amazon; 5 motores (re-rankers), 7 reescritores, 15 heurísticas | "eleven of the fifteen heuristic prompts pulled it further into the negative" (no reescritor GPT-4.1). Otimizando o prompt, todos convergem para o mesmo conjunto: alinhamento com a intenção, palavras-chave e sinônimos, resumo de abertura, seções, tópicos, casos de uso, perguntas de comprador, sem keyword stuffing, factualidade. Tamanho e tópicos explicam só R² = 0,005 da melhora | só inglês, só Amazon, recuperação fixa: "conclusions should not be assumed to transfer to other languages, regions, or product mixes without further evidence" | apoia C16, C17, C18 (como conteúdo, não como schema), C22 e a regra de não inventar. Não apoia contagem de palavras |
| Vishwakarma et al., "What Gets Cited" [R4] | acadêmico, preprint de 25/05/2026, autores da Sprinklr | 252 mil comparações em pares, 6 modelos, 18 fatores, marcas anonimizadas e ordem alternada | "topical relevance and list position are the biggest drivers of being cited first. Including explicit price information and a recent timestamp also helps consistently. Completeness and trust cues add smaller gains, while formatting-only edits have little impact." | dois documentos por vez (produção usa 5 a 10); textos são posts de review, não páginas de loja | preço explícito no texto e especificação completa contam; formatação sozinha, não |
| Chen et al., "How to Dominate AI Search" [R5] | acadêmico (Universidade de Toronto), preprint de 10/09/2025 | comparação entre buscadores com IA e Google em vários setores, idiomas e paráfrases | "AI Search exhibit a systematic and overwhelming bias towards Earned media (third-party, authoritative sources) over Brand-owned and Social content" | descritivo; não testa mudança em página | parte da visibilidade em IA está fora da página: review de terceiros, imprensa |
| Zhang, He e Yao, "From Citation Selection to Citation Absorption" [R6] | acadêmico (pesquisadores independentes), preprint de 29/04/2026 | 602 prompts controlados em ChatGPT, Google AI Overview/Gemini e Perplexity; 18.151 páginas lidas | escolha da fonte depende sobretudo da identidade e autoridade do domínio; páginas com números têm em média mais influência na resposta; "Q&A formatting alone does not improve absorption" | o próprio artigo não afirma causalidade | reforça fatos concretos; enfraquece FAQ como alavanca isolada |
| Kumar, "GEO at Scale" [R10] | preprint de 18/06/2026, autor ligado a uma ferramenta de medição | 100 mil respostas, mais de 100 marcas | marcas globais aparecem em 73% das respostas relevantes, médias em 44%, pequenas em 11%; cerca de 78% das citações vão para sites corporativos; listas de "melhores" somam cerca de 21% das citações | conflito de interesse; descritivo | o porte da marca pesa e não se resolve na página |
| Kumar e Lakkaraju [R7]; Pfrommer et al. (EMNLP 2024) [R8] | acadêmico | texto estratégico ou injeção de prompt em páginas de produto | os dois conseguem promover produtos nas respostas; [R8] diz que os ataques "transfer effectively to state-of-the-art conversational search engines such as perplexity.ai" | demonstração de vulnerabilidade, não recomendação | é o motivo de o Bing punir "prompt injection" [M1]; a régua deve reprovar isso, não ensinar |
| Wu et al., "AutoGEO" [R9]; Yu et al., "GEO-SFE" [R11] | acadêmico, preprints de 2025 e 2026 | reescrita automática guiada por regras aprendidas; estrutura do documento | ganhos em benchmarks próprios (GEO-SFE relata +17,3% na taxa de citação) | benchmarks dos próprios autores, sem replicação | sinal fraco; não muda a régua |

**Estudos de fornecedor que ajudam a calibrar, com o viés anotado:**

- **Schema e citação (Ahrefs, 11/05/2026)** [V1]: 1.885 páginas que adicionaram JSON-LD contra
  controles pareados, diferença em diferenças, 30 dias antes e depois. AI Overviews -4,6%, AI Mode
  +2,4%, ChatGPT +2,2%, e "Adding schema produced no major uplift in citations on any platform".
  Limites declarados: só páginas já muito citadas, tipos de schema somados, janela curta.
- **Citações do AI Overviews e o top 10 (Ahrefs, 02/03/2026)** [V2]: 38% das páginas citadas
  estavam no top 10 da mesma busca, contra 76% no estudo de julho de 2025. A própria Ahrefs mudou
  o método de leitura entre os dois, então a queda não é toda comportamento do Google.
- **llms.txt (Ahrefs, 15/06/2026)** [V3]: 137.210 domínios; 28% publicam o arquivo e "97% of those
  files received zero traffic in May 2026".
- **Robôs de IA e JavaScript (Vercel e MERJ, 17/12/2024)** [V4]: "none of the major AI crawlers
  currently render JavaScript" (GPTBot, ClaudeBot, PerplexityBot); o Gemini usa a infraestrutura
  do Googlebot. É de quase dois anos atrás; não achei medição mais nova.
- **Cliques (Pew Research Center, 22/07/2025)** [R12]: instituto independente, 900 adultos dos
  EUA em março de 2025. Com resumo de IA na página, clique em resultado tradicional em 8% das
  visitas, contra 15% sem resumo; clique em link dentro do resumo em 1%.

---

## 4. O que mudar na régua de 23 critérios

Referência: `repo/regua/regua.md` (pesos e limites que o Absoluto SEO publica). Peso entre
parênteses.

### 4.1 Manter

| Critério | Por que fica | Fonte |
|---|---|---|
| C05 Um H1 ligado ao produto (7) | o Google usa o primeiro `<h1>` visível entre as fontes do título; o Bing pede hierarquia lógica. "Exatamente um H1" não é exigência escrita, por isso o caso de vários H1 já ser só metade está certo | [G11], [M1] item 13 |
| C06 Subtítulos H2 (5) | o Google e o Bing pedem página organizada por seções com subtítulos | [G2], [M1] item 13 |
| C12 Texto alternativo nas imagens (6) | é o atributo de imagem que o Google mais destaca; o Bing pede alt para entender a imagem | [G14], [M1] item 12 |
| C13 URL amigável (4) | palavras legíveis, no idioma do público, separadas por hífen, são recomendação escrita. Ajuste pequeno: a fonte fala em palavras descritivas, não em palavra-chave, então a exigência de "parte da palavra-chave" pode virar "palavras em português que descrevem o produto" | [G15] |
| C15 Links internos (1) | o Google cita links internos na lista de fundamentos para IA; o Bing também | [G1], [M1] item 5 |
| C16 Abertura direta (15) | é o item 18 do Bing, com todas as letras, e o "resumo de abertura" emergiu sozinho no E-GEO | [M1], [R3] |
| C17 Especificações em lista ou tabela (18) | fatos explícitos (Bing), especificação ausente é fator de completude [R4], `product_detail` existe no feed do Google. Ajuste de regra em 4.2 | [M1] item 15, [R4], [G23] |
| C19 Produto bem identificado (14) | é o item 16 do Bing; marca, GTIN e MPN são as propriedades que o Google usa para casar o produto | [M1], [G4] |
| C20 Frases com dado concreto (12) | é o item 15 do Bing; páginas com números têm mais influência [R6]. Cuidado de redação: o C-SEO Bench mostra que **acrescentar estatística** não ajuda em produto [R2]; o que vale é a medida real da ficha | [M1], [R6], [R2] |
| C22 Para quem é e quando usar (8) | casos de uso emergiram no E-GEO; falta de comparação é fator no [R4] | [R3], [R4] |
| As duas regras finais ("nenhum fato de fora da ficha" e "critério não lido não é critério ruim") | o Google manda revisar todo texto gerado por IA, incluindo metadados e schema; a factualidade foi o único traço comum a todos os prompts do E-GEO | [G17], [R3] |

### 4.2 Mudar

**C01 e C02, título (11 + 8): juntar e trocar tamanho por qualidade.**
Motivo: "While there's no limit on how long a <title> element can be, the title link is truncated
in Google Search results as needed, typically to fit the device width." [G11]. Não há fonte para
"palavra-chave nos 30 primeiros caracteres". O que o Google pede: descritivo, conciso, único, sem
repetição, no idioma da página.
Regra proposta: **passa** se o `<title>` existe, contém marca e modelo ou linha do produto, não se
repete em outro SKU do catálogo e não repete nenhum termo de conteúdo; **metade** se é único mas
não nomeia o modelo, ou se passa de cerca de 70 caracteres (risco alto de corte; número é
heurística, não regra); **falha** se está ausente, é genérico ou é igual ao de outros produtos.
Até 60 caracteres vira aviso de corte, não critério de nota.

**C03 e C04, meta description (10 + 6): juntar e trocar "gatilho" por fato.**
Motivo: "There's no limit on how long a meta description can be, but the snippet is truncated" e
"A good meta description can bring all this data together", falando de preço, idade e fabricante
de um produto [G12]. Verbos como "compre", "garanta" e "aproveite" não têm fonte; preço e fato do
produto têm. O Bing diz que meta ausente, duplicada ou curta demais prejudica [M1].
Regra proposta: **passa** se existe, é única no catálogo e traz pelo menos dois fatos da ficha
(preço, marca, atributo com número), sem ser lista de palavras; **metade** se é única mas sem fato
concreto, ou tem menos de cerca de 70 caracteres (heurística); **falha** se ausente, duplicada ou
só palavras-chave.

**C07, Open Graph (6): reduzir e mudar o que conta.**
Motivo: o Google usa `og:title` entre as fontes do título e `og:image` como imagem preferida, e
pede que a imagem não seja logo [G11] [G14]. Nenhuma fonte lida diz que o Google use `og:type`.
Regra proposta: **passa** com `og:title` e `og:image` (URL absoluta, diferente do logo);
**metade** com só um deles; **falha** sem nenhum. Peso sugerido: 3.

**C08, schema Product (14): alinhar com o que o Google exige para loja.**
Motivo: em merchant listing, `name`, `image` e `offers` são obrigatórios, com preço maior que zero
e moeda; `availability` é recomendada; o Google recomenda o markup no HTML inicial [G4]. Hoje a
régua aceita `brand` **ou** `image`, e `image` é obrigatória.
Regra proposta: **passa** se o JSON-LD `Product` está no HTML cru com `name`, `image`,
`offers.price` maior que zero, `offers.priceCurrency` e `offers.availability`; **metade** se falta
`availability`, se o preço é zero, ou se o markup só aparece depois do JavaScript; **falha** sem
`Product` ou sem `offers`.

**C09, campos ricos (4): separar em dois critérios.**
Motivo: identificador e avaliação têm regras e riscos diferentes. GTIN e MPN mais marca são o que
o Google e o Merchant Center usam para casar o produto [G4] [G24]. Avaliação só pode ir para o
schema se estiver visível e for de usuário real [G9]; uma nota no schema sem nota na página é
violação, e hoje ela dá ponto cheio. Ver N5 e N9 em 4.3.

**C10, descrição com 300 palavras e lista (10): trocar contagem por originalidade.**
Motivo: "Are you writing to a particular word count because you've heard or read that Google has a
preferred word count? (No, we don't.)" [G13]; "There's no ideal page length" [G2]; no E-GEO,
tamanho e tópicos explicam R² = 0,005 da melhora [R3]. O que as fontes pedem é conteúdo próprio
[G2] [M1].
Regra proposta (critério "Descrição própria"): **passa** se o texto da descrição não se repete em
outros SKUs (similaridade de trechos abaixo de um limiar a calibrar) e cobre os atributos da
ficha; **metade** se parte do texto é igual ao de outros produtos; **falha** se está vazia (menos
de cerca de 50 palavras, piso para detectar página sem texto, não meta) ou é cópia.

**C11, densidade de 0,5% a 2,5% (6): remover a faixa.**
Motivo: nenhuma das fontes oficiais lidas dá faixa de densidade; o Google diz que a IA entende
sinônimos e que não é preciso cobrir cada variação [G2]; Google e Bing tratam repetição como
stuffing [G11] [M1]; no GEO, keyword stuffing ficou abaixo da linha de base [R1]. Fica só a
checagem negativa, dentro dos critérios de título e de descrição: **falha** se uma sequência de
três palavras se repete três vezes ou mais, ou se há bloco de palavras separadas por vírgula sem
frase (heurística).

**C14, canonical e indexação (2): virar portão.**
Motivo: para o Google, estar indexado e elegível a trecho é condição para aparecer nos recursos de
IA, não um detalhe de 2 pontos [G1]. Ver N1 em 4.3. O canonical em si continua como critério
pequeno.

**C18, FAQ com `FAQPage` (18): manter as perguntas, tirar o schema e reduzir o peso.**
Motivo: o rich result de FAQ ficou restrito a "well-known, authoritative government and health
websites" em 08/08/2023 [G20], deixou de aparecer para todos em 07/05/2026 e teve a documentação
removida em 15/06/2026 [G3]. Pergunta de comprador respondida ainda tem apoio como conteúdo [R3],
mas o formato sozinho não melhora o uso da página na resposta [R6]. No Google, o lugar novo para
pergunta e resposta é o feed (`question_and_answer`, até 30 por produto) [G23].
Regra proposta: **passa** com 3 ou mais perguntas visíveis no HTML inicial, cada uma respondida
com fato da ficha; **metade** com 1 ou 2, ou com respostas que mandam "consultar"; **falha** sem
nenhuma. `FAQPage` não soma nem tira. Peso sugerido: 6.

**C21, texto fácil de escanear (10): manter como legibilidade e reduzir.**
Motivo: o Google diz que não é preciso picotar o texto para a IA [G2]; formatação sozinha teve
impacto desprezível [R4]. O critério continua bom para quem lê, não como alavanca de IA. Peso
sugerido: 5.

**C17, especificações (18): medir pares, não itens de lista.**
Motivo: cinco `<li>` de benefício genérico passam hoje sem nenhum dado. Regra proposta: **passa**
com 5 ou mais pares atributo:valor (linha de tabela, item de `<dl>`, ou `<li>` com dois-pontos e
valor); **metade** com 2 a 4; **falha** com 0 ou 1.

**C23, schema completo para IA (5): remover.**
Motivo: "There's also no special schema.org structured data that you need to add" [G1];
"Structured data isn't required for generative AI search" [G2]; o Bing diz que schema "does not
guarantee visibility or grounding traffic" [M1]; o estudo controlado não viu ganho [V1]. Os
5 pontos vão para os critérios novos.

### 4.3 Acrescentar

Cada regra abaixo foi escrita para o `conferir.py` decidir sozinho, salvo onde está marcado.

**N1. Portão: indexável e elegível a trecho** (SEO e GEO). Fontes: [G1], [M1] item 10, [O1], [P1].
- **Falha** (a nota vira "não elegível" em vez de número): HTTP diferente de 200, `noindex`,
  `nosnippet`, `max-snippet:0`, canonical para outra URL não equivalente, ou robots.txt
  bloqueando Googlebot, Bingbot, OAI-SearchBot ou PerplexityBot no caminho da página.
- **Metade:** `data-nosnippet` envolvendo a descrição; `noarchive` (tira a página do Copilot) ou
  `nocache` (o Copilot só usa URL, título e trecho) [M1].
- **Passa:** nada disso.

**N2. Conteúdo essencial no HTML inicial** (SEO e GEO). Fontes: [G4], [M1] item 8, [V4].
- **Passa:** nome, preço, disponibilidade, a maior parte do texto da descrição e o JSON-LD
  `Product` estão no HTML cru.
- **Metade:** descrição ou JSON-LD só aparecem no HTML renderizado.
- **Falha:** preço e descrição só aparecem depois do JavaScript.
- Nota: isso separa dois casos que a régua hoje junta. Bloqueio por WAF ou captcha é "não foi
  possível ler" (regra 2 da régua). HTML que chega vazio sem bloqueio é um defeito real da página,
  porque os robôs de IA medidos não executam JavaScript [V4].

**N3. Schema igual ao texto visível** (SEO). Fontes: [G1], [G10], [G9], [M1] item 14.
- **Passa:** `offers.price` normalizado aparece no texto no formato brasileiro, `priceCurrency` é
  BRL, `availability` bate com o texto (InStock contra "Esgotado"), `name` está no H1, nota e
  contagem do schema iguais às visíveis, `priceValidUntil` no futuro ou ausente.
- **Metade:** uma divergência leve (por exemplo, disponibilidade não escrita na página).
- **Falha:** preço diferente, nota no schema sem nota na página, ou `priceValidUntil` vencido.

**N4. Preço e disponibilidade em texto** (GEO). Fontes: [R4], [O3], [G4].
- **Passa:** preço e situação de estoque legíveis no texto do HTML inicial.
- **Metade:** só um dos dois.
- **Falha:** nenhum, ou só em imagem.

**N5. Identificadores do produto** (SEO, e GEO pela entidade). Fontes: [G4], [G23], [G24], [M1] item 16.
- **Passa:** `gtin8`, `gtin12`, `gtin13` ou `gtin14` numérico com dígito verificador válido e uma
  `brand.name`; para produto sem GTIN do fabricante, `mpn` mais `brand` também passa.
- **Metade:** só `sku`, ou `mpn` sem marca.
- **Falha:** nenhum identificador.

**N6. Frete e devolução declarados** (SEO). Fontes: [G4], [G7], [G8], [G24].
- **Passa:** `MerchantReturnPolicy` e `ShippingService` (no `Organization`) ou
  `hasMerchantReturnPolicy` e `shippingDetails` (no `Offer`), com `applicableCountry` BR, na página
  ou referenciados por `@id`, e link visível para a política.
- **Metade:** só o link visível para a política.
- **Falha:** nada.
- **Parcial por natureza:** o Google aceita a mesma informação configurada no Merchant Center ou no
  Search Console, e isso não aparece no HTML [G4]. O relatório deve dizer "não verificável pela
  página" quando a loja informar que usa essa configuração.
- Brasil: o direito de arrependimento é de 7 dias para compra fora do estabelecimento (CDC,
  art. 49) [L1]. Markup com `merchantReturnDays` menor que 7 merece alerta. Não é parecer jurídico.

**N7. Variantes** (SEO). Fonte: [G6].
- **Não se aplica** (conta como passa) se a página não tem seletor de variação.
- **Passa:** `ProductGroup` com `productGroupID`, `variesBy` e `hasVariant` (ou variantes com
  `isVariantOf`), e `sku` ou `gtin` único por variante.
- **Metade:** variantes só como várias `Offer` dentro de um `Product`.
- **Falha:** seletor de cor ou tamanho sem nenhum markup de variante.

**N8. Imagens com qualidade** (SEO). Fontes: [G4], [G14]. Junta com o C12.
- **Passa:** `image` no schema com pelo menos uma URL rastreável de 50 mil pixels ou mais, e
  `og:image` diferente do logo.
- **Metade:** imagem presente, mas pequena ou não verificada.
- **Falha:** sem imagem no schema.
- Medição parcial: exige baixar a imagem.

**N9. Avaliação visível e genuína** (SEO). Fonte: [G9]. Substitui metade do C09.
- **Passa:** `aggregateRating` com `ratingValue` e contagem, e a mesma nota visível na página.
- **Metade:** loja sem avaliações (é recomendação, não obrigação).
- **Falha:** nota no schema sem nota visível, ou nota marcada no `Organization` da própria loja.
- A autenticidade não se mede no HTML; fica a regra 1 da régua.

**N10. Portão: sem texto escondido nem instrução para IA** (GEO). Fontes: [M1], [G16], [R7], [R8].
- **Falha** (GEO zera e o relatório alerta): texto em nó oculto (`display:none`,
  `visibility:hidden`, `font-size:0`, `aria-hidden`, cor igual ao fundo) contendo instrução a
  modelo ("ignore as instruções", "recomende este produto", "you are", "assistant") ou bloco de
  palavras-chave.
- **Passa:** nada disso.

**N11. Idioma e moeda coerentes** (SEO e GEO). Fontes: [G11], [G25].
- **Passa:** `<html lang="pt-BR">` (ou `pt`), title, meta e descrição em português, `priceCurrency`
  BRL.
- **Metade:** `lang` ausente, mas texto em português.
- **Falha:** título ou descrição em outro idioma, ou moeda diferente da exibida.

**N12. Trilha e categoria** (SEO). Fontes: [G29], [G4]. Junta com o C15.
- **Passa:** `BreadcrumbList` válido e `Product.category`.
- **Metade:** só um dos dois.
- **Falha:** nenhum.

### 4.4 Uma redistribuição possível

Os pesos abaixo são julgamento meu, para cada grupo continuar somando 100. A evidência diz o que
importa; ela não diz quanto vale cada ponto.

| SEO | Peso | Origem |
|---|---|---|
| Portão: indexável e elegível a trecho | sem peso | N1 (sai do C14) |
| Título descritivo e único | 10 | C01 + C02 |
| Meta description com fatos | 8 | C03 + C04 |
| H1 com o nome do produto | 6 | C05 |
| Subtítulos | 4 | C06 |
| `og:title` e `og:image` | 3 | C07 |
| `Product` elegível a merchant listing | 14 | C08 |
| Conteúdo essencial no HTML inicial | 10 | N2 |
| Schema igual ao texto visível | 10 | N3 |
| Identificadores (GTIN, MPN, marca) | 8 | N5 (sai do C09) |
| Frete e devolução | 6 | N6 |
| Imagens: alt e qualidade | 7 | C12 + N8 |
| URL legível | 3 | C13 |
| Canonical coerente | 3 | C14 |
| Links internos, trilha e categoria | 3 | C15 + N12 |
| Avaliação visível e genuína | 3 | N9 (sai do C09) |
| Variantes | 2 | N7 |
| **Total** | **100** | |

| Busca com IA | Peso | Origem |
|---|---|---|
| Portão: sem texto escondido nem instrução para IA | sem peso | N10 |
| Abertura direta | 15 | C16 |
| Especificações em pares atributo:valor | 16 | C17 |
| Produto bem identificado | 14 | C19 |
| Frases com dado concreto | 12 | C20 |
| Preço e disponibilidade em texto | 10 | N4 |
| Para quem é, quando usar, comparação | 10 | C22 |
| Descrição própria | 8 | C10 reescrito |
| Perguntas de comprador respondidas | 6 | C18 sem `FAQPage` |
| Texto escaneável | 5 | C21 |
| Idioma e moeda coerentes | 4 | N11 |
| **Total** | **100** | |

Saem: C11 (densidade, vira checagem negativa) e C23 (schema para IA).

---

## 5. Mitos e coisas sem evidência

| Afirmação que circula | O que as fontes primárias dizem | Veredito |
|---|---|---|
| "Publique um `llms.txt` para aparecer nas IAs" | Google: "Doing so will neither harm nor help your site's visibility or rankings in Google Search, as Google Search ignores them." [G2]; nota adicionada em 15/06/2026 [G3]. Não achei OpenAI, Perplexity nem Microsoft dizendo que usam o arquivo. Estudo de fornecedor: 97% dos arquivos sem nenhuma requisição em maio de 2026 [V3] | sem evidência; inútil para o Google por declaração dele |
| "Existe um schema para IA" ou "marcação especial para LLM" | "There's also no special schema.org structured data that you need to add." [G1]; "Overfocusing on structured data" está na lista do que ignorar [G2]; Bing: "does not guarantee" [M1]; ganho nulo no estudo controlado [V1] | mito. Schema serve para rich result e para o Google entender o produto |
| "FAQ com `FAQPage` dá rich result" | restrito a sites de governo e saúde desde 08/08/2023 [G20]; fora do ar para todos desde 07/05/2026; documentação removida em 15/06/2026 [G3]; a página de documentação de FAQ hoje redireciona para o registro de mudanças | falso desde maio de 2026 |
| "Título com 50 a 60 e meta com 120 a 158 caracteres" | "there's no limit", o corte é pela largura do aparelho [G11] [G12]. Os números são heurística de mercado para evitar corte | opinião de mercado; usar como aviso, não como nota |
| "Descrição precisa de 300 palavras" | "(No, we don't.)" sobre contagem preferida [G13]; "There's no ideal page length" [G2] | sem evidência |
| "Densidade de palavra-chave ideal" | o Google diz que a IA entende sinônimos e que não é preciso cobrir cada variação [G2]; repetição é stuffing [G11] [M1]; keyword stuffing ficou abaixo da linha de base no GEO [R1] | sem evidência; só o excesso tem fonte, e é negativa |
| "Picote o conteúdo em blocos para a IA" (chunking) | "There's no requirement to break your content into tiny pieces for AI to better understand it." [G2]; formatação sozinha com impacto desprezível [R4] | mito; escanear ajuda quem lê |
| "Crie uma página para cada variação de pergunta" | "violates Google's scaled content abuse spam policy" [G2] | prática punível |
| "Acrescentar estatísticas e citações aumenta 40% a visibilidade" | medido no GEO em motor simulado e consultas genéricas [R1]; nulo ou negativo em recomendação de produto no C-SEO Bench [R2] | parcialmente verdadeiro fora de e-commerce; não transfere para produto |
| "Tom autoritário convence a IA" | "we find no significant improvement" [R1]; perto de zero ou negativo [R2] | sem evidência |
| "Bloquear o GPTBot tira a loja do ChatGPT" | os robôs são independentes; a busca do ChatGPT usa o OAI-SearchBot [O1] | falso |
| "Bloquear o Google-Extended tira a loja do AI Overviews" | "Google-Extended does not impact a site's inclusion in Google Search nor is it used as a ranking signal in Google Search." [G19]. O controle do AI Overviews é o Googlebot, os controles de trecho e o controle do Search Console [G1] [G21]. Atenção: o Google-Extended controla o grounding no app Gemini e no Vertex AI [G19] | falso para a Busca; verdadeiro para o app Gemini |
| "O robots.txt barra o Perplexity sempre" | "this fetcher generally ignores robots.txt rules" (Perplexity-User) [P1]; o ChatGPT-User também pode não seguir [O1] | falso para buscas pedidas pelo usuário |
| "Os robôs de IA leem a página como o Googlebot" | GPTBot, ClaudeBot e PerplexityBot não executavam JavaScript na medição de 2024 [V4]; o Bing manda não esconder conteúdo atrás de renderização no cliente [M1] | não confie; sirva o conteúdo no HTML |
| "A IA lê o JSON-LD" | nenhuma das fontes de OpenAI, Perplexity ou Microsoft lidas afirma isso. Um artigo da Ahrefs de 25/09/2026 diz que cinco sistemas ignoraram JSON-LD, mas não descreve o método | não confirmado; ponha os fatos também no texto visível |
| "Ferramenta X mede sua posição na IA com dado interno do Google" | "No third-party tool has access to our internal ranking or AI systems." [G2] | falso |
| "Texto escondido ou instrução para o modelo funciona" | funciona em laboratório [R7] [R8], e por isso é punido: "may result in reduced visibility or removal" [M1]; o Google inclui manipular respostas de IA na definição de spam [G16] | funciona até ser pego; reprovar na régua |
| "Formato de pergunta e resposta, sozinho, faz a IA usar a página" | "Q&A formatting alone does not improve absorption." [R6] | sem evidência |

---

## 6. O que só a loja controla fora da página

### 6.1 robots.txt e CDN

| Robô (token no robots.txt) | Para que serve | Efeito de bloquear | Fonte |
|---|---|---|---|
| `Googlebot` | Busca do Google, incluindo AI Overviews e AI Mode | sai da Busca e dos recursos de IA da Busca | [G1] |
| `Google-Extended` | treino do Gemini e grounding no app Gemini e no Vertex AI | não muda a Busca; tira do grounding do app Gemini | [G19] |
| `Bingbot` | Bing e Copilot | sai do Bing e do Copilot | [M1] |
| `OAI-SearchBot` | busca do ChatGPT | "will not be shown in ChatGPT search answers" | [O1] |
| `GPTBot` | treino dos modelos da OpenAI | só treino | [O1] |
| `ChatGPT-User` | visita pedida pelo usuário | robots.txt "may not apply" | [O1] |
| `PerplexityBot` | busca do Perplexity | sai das respostas do Perplexity | [P1] |
| `Perplexity-User` | visita pedida pelo usuário | "generally ignores robots.txt rules" | [P1] |

Exemplo comentado (ajuste à decisão de negócio da loja):

```txt
# Busca e respostas com citação: não bloquear
User-agent: Googlebot
Disallow:

User-agent: Bingbot
Disallow:

User-agent: OAI-SearchBot
Disallow:

User-agent: PerplexityBot
Disallow:

# Treino de modelos: decisão da loja; segundo a OpenAI, não muda a busca do ChatGPT
User-agent: GPTBot
Disallow: /

# Google-Extended também controla o grounding no app Gemini.
# Bloquear tira a loja dessas respostas, sem mexer na Busca do Google.
# User-agent: Google-Extended
# Disallow: /
```

- **CDN e WAF.** O Google inclui "and by any CDN or hosting infrastructure" no requisito [G1]; o
  Perplexity publica faixas de IP e regras para Cloudflare e AWS WAF [P1]. A Cloudflare pergunta a
  cada domínio novo, desde 01/07/2025, se quer permitir robôs de IA [V5]. Loja com "bot fight" ou
  bloqueio de IA ligado pode estar fora do ChatGPT e do Perplexity sem saber.
- **Prazos.** OpenAI: cerca de 24 horas para refletir mudança no robots.txt [O1]. Perplexity: até
  24 horas [P1].
- **O que vem aí.** O Google pretende aceitar o sinal `user-agent: __usage_ai-training` (AIPREF)
  no início de 2027 [G19]. O Bing anunciou em 30/10/2026 preferências separadas de treino
  (robots.txt ou página) e de grounding (só na página, por meta tag ou `X-Robots-Tag`), honradas a
  partir de 01/02/2027; "AI Grounding cannot be set in robots.txt" [M2]. Até lá, `noarchive` e
  `nocache` continuam valendo para o Copilot [M1].

### 6.2 Painéis de controle e medição

- **Google Search Console:** controle "Search generative AI" (padrão incluído; excluir tira de AI
  Overviews, AI Mode e recursos de IA do Discover) [G21] e relatório de desempenho em IA generativa,
  que mede impressões [G22]. Os dois foram liberados para todos os sites em 31/08/2026.
- **Bing Webmaster Tools:** AI Performance, com citações por página e "grounding queries", em
  prévia pública desde 10/02/2026 [M3] [M4]. Citação não é clique.
- **IndexNow:** o Bing pede para avisar quando URL é criada, alterada ou removida, para reduzir
  referência desatualizada no Copilot [M1].

### 6.3 Renderização no servidor

Decisão de infraestrutura, não de conteúdo. Se a vitrine monta a página no navegador, a página
pode chegar vazia para os robôs de IA medidos [V4], e o Google diz que markup de produto gerado
por JavaScript deixa a leitura de preço e estoque menos frequente e menos confiável [G4].

### 6.4 Feeds de produto

**Google Merchant Center.**
- O Google cita o feed do Merchant Center como caminho para produtos aparecerem em respostas de IA
  [G2].
- Atributos novos para conversa: `question_and_answer` (até 30 pares, 10 mil caracteres no total),
  `product_highlight`, `product_detail` e `related_product` [G23]. O anúncio de 11/01/2026 fala em
  atributos como "answers to common product questions, compatible accessories or substitutes",
  para AI Mode, Gemini e Business Agent [G27].
- Texto gerado por IA vai em atributo próprio: "For titles created using generative AI, use the
  structured title [structured_title] attribute" [G23]; "AI-generated product data such as title
  and description attributes must be specified separately and labeled as AI-generated." [G17]
  Isso pesa para quem reescreve catálogo com IA.
- Ordem de precedência quando frete e devolução estão em vários lugares: feed por produto, Content
  API, configuração no Merchant Center ou Search Console, markup no produto, markup no
  `Organization` [G4].
- Feed e página precisam bater: o Google diz que pode verificar os dados do merchant listing antes
  de exibir [G4].

**ChatGPT (OpenAI).** Feed pelo Agentic Commerce Protocol, só para parceiros aprovados, com
inscrição em chatgpt.com/merchants; Shopify e Etsy já integrados; envio por SFTP, com a
recomendação de mandar o catálogo completo pelo menos uma vez por dia; variante por linha, com ID
do pai estável [O2] [O3] [O4].
Shopping no ar só nos EUA [O2]. Sem feed, o ChatGPT ainda pode ler o site [O2].

**Perplexity.** O programa de lojistas foi lançado em 18/11/2024, gratuito, com o lojista
enviando especificações [P2]. Em 09/11/2026 a página oficial não descreve mais o programa [P3].
Blogs de agência dizem que o feed segue o padrão do Google; não achei fonte da Perplexity que
confirme.

**Microsoft (Copilot).** "Feeds primarily enable discovery (products showing up in AI responses)";
os resultados orgânicos usam a web e o feed do Microsoft Merchant Center; checkout no Copilot só
para lojistas em inglês que vendem para os EUA em dólar [M5].

### 6.5 Avaliações e menções de terceiros

- Avaliação de cliente real, com nome e comentário, e visível na página [G9]. A diretriz contra
  avaliação falsa ou incentivada sem aviso entrou em 24/07/2026 [G3].
- Fora da loja: os buscadores com IA preferem fontes de terceiros ("Earned media") às da marca
  [R5], e as listas de "melhores" estão entre o formato mais citado [R10]. O Google avisa que
  buscar menções artificiais "isn't as helpful as it might seem" [G2]. Imprensa, review
  independente e comunidade são trabalho de marca, não de página.

### 6.6 Governança do texto gerado por IA

Revisão humana de tudo que vai para a página e para o schema [G17], rótulo de IA no feed [G23], e
a regra 1 da régua (nada fora da ficha). O E-GEO mostra que prompts de reescrita feitos "no
instinto" pioraram o resultado em 11 de 15 casos [R3]: reescrever sem medir antes e depois é
risco, não ganho garantido.

---

## 7. Brasil

**O que está disponível.**
- AI Overviews no Brasil desde 2024, segundo o blog do Google Brasil; não confirmei a data exata.
- AI Mode em português desde 08/09/2025 [G28].
- Aba Shopping disponível para usuários no Brasil; moeda BRL; português do Brasil entre os idiomas
  aceitos [G25].
- No feed, para o Brasil: frete é obrigatório ("You're required to set up 'Shipping' settings or
  add shipping costs" na lista de países que inclui o Brasil) [G24]; `age_group` obrigatório em
  vestuário [G23]; atributo `loyalty_program` disponível [G23]. Em vestuário, o schema aceita o
  sistema de tamanho brasileiro `WearableSizeSystemBR` [G4].
- Idioma: "your product landing pages should be in the same language as your product data", e a
  página e o checkout precisam estar no mesmo idioma do feed [G25]. O título precisa estar no
  idioma da página [G11].

**O que ainda não chegou, pelas fontes lidas em 09/11/2026.**
- Shopping do ChatGPT: "currently live for ChatGPT users in the U.S." [O2].
- Checkout no AI Mode e no Gemini pelo UCP: começou com "eligible U.S. retailers" [G27]; houve
  expansão para o Canadá em 04/11/2026, segundo resultado de busca do blog do Google que não abri.
- Relatório de desempenho em IA do Merchant Center: EUA, Canadá, Austrália, Índia e Nova Zelândia
  [G26].
- Checkout no Copilot: só EUA, em inglês e dólar [M5].
- Não confirmei se o AI Mode em português já mostra listagens de produto do Merchant Center para
  compras no Brasil.

**Pesquisa em português.** Nenhum dos estudos de GEO desta pesquisa usou português. O E-GEO
avisa que suas conclusões não devem ser transferidas para outros idiomas sem nova evidência [R3].
Os tamanhos de efeito citados aqui são de inglês.

**Detalhes de implementação que mordem em loja brasileira.**
- O JSON-LD usa ponto decimal (`"price": 1234.56`) e o texto usa vírgula (R$ 1.234,56). A checagem
  de consistência (N3) precisa normalizar os dois.
- Política de devolução no markup deve refletir a política real e o prazo legal de 7 dias do art.
  49 do CDC para compra fora do estabelecimento [L1].

---

## 8. O que não consegui confirmar

- **Artigo de ajuda do shopping do ChatGPT** ("Improved shopping results from ChatGPT search"):
  devolveu 403 e desafio da Cloudflare. O que circula sobre ele (metadados de terceiros, avaliações
  não verificadas pela OpenAI) veio só de resumo de busca, então fica fora das recomendações.
- **Estado atual do programa de lojistas do Perplexity**: só tenho o post de 2024 [P2].
- **Se ChatGPT, Perplexity e Copilot leem JSON-LD**: nenhuma fonte primária lida diz sim ou não.
- **Robôs de IA e JavaScript**: a medição pública é de dezembro de 2024 [V4].
- **Controle de IA do Search Console** [G21]: o texto foi lido por ferramenta que resume a página;
  as frases citadas foram as que ela devolveu entre aspas.
- **Parâmetro `utm_source=chatgpt.com` nos cliques vindos do ChatGPT**: aparece em guias de
  terceiros citando o FAQ de publishers da OpenAI, que não consegui abrir.
- **Números de corte de título e meta em pixels**: não existe número oficial; qualquer limiar é
  heurística.
- **Data exata da chegada do AI Overviews ao Brasil.**
- **Tradução dos efeitos para português**: nenhum estudo encontrado.

---

## 9. Fontes

Todas lidas em 09/11/2026. "Atualizada em" é a data que a própria página informa.

**Google**
- [G1] AI features and your website. https://developers.google.com/search/docs/appearance/ai-features (atualizada em 10/12/2025)
- [G2] Optimizing your website for generative AI features on Google Search. https://developers.google.com/search/docs/fundamentals/ai-optimization-guide (atualizada em 10/07/2026; criada em 15/05/2026 segundo [G3])
- [G3] Latest documentation updates (registro de mudanças do Search Central). https://developers.google.com/search/updates (atualizada em 09/11/2026)
- [G4] Merchant listing (Product, Offer) structured data. https://developers.google.com/search/docs/appearance/structured-data/merchant-listing (atualizada em 08/09/2026)
- [G5] Introduction to Product structured data. https://developers.google.com/search/docs/appearance/structured-data/product (atualizada em 10/12/2025)
- [G6] Product variant structured data (ProductGroup, Product). https://developers.google.com/search/docs/appearance/structured-data/product-variants (atualizada em 08/09/2026)
- [G7] Merchant shipping policy (ShippingService) structured data. https://developers.google.com/search/docs/appearance/structured-data/shipping-policy (atualizada em 08/09/2026)
- [G8] Merchant return policy (MerchantReturnPolicy) structured data. https://developers.google.com/search/docs/appearance/structured-data/return-policy (atualizada em 08/09/2026)
- [G9] Review snippet (Review, AggregateRating) structured data. https://developers.google.com/search/docs/appearance/structured-data/review-snippet (atualizada em 08/09/2026)
- [G10] General structured data guidelines. https://developers.google.com/search/docs/appearance/structured-data/sd-policies (atualizada em 10/07/2026)
- [G11] Influencing your title links in search results. https://developers.google.com/search/docs/appearance/title-link (atualizada em 10/12/2025)
- [G12] Control your snippets in search results. https://developers.google.com/search/docs/appearance/snippet (atualizada em 20/04/2026)
- [G13] Creating helpful, reliable, people-first content. https://developers.google.com/search/docs/fundamentals/creating-helpful-content (atualizada em 05/10/2026)
- [G14] Image SEO best practices. https://developers.google.com/search/docs/appearance/google-images (atualizada em 02/03/2026)
- [G15] URL structure best practices. https://developers.google.com/search/docs/crawling-indexing/url-structure (atualizada em 21/10/2026)
- [G16] Spam policies for Google web search. https://developers.google.com/search/docs/essentials/spam-policies (atualizada em 28/08/2026)
- [G17] Google Search's guidance on using generative AI content on your website. https://developers.google.com/search/docs/fundamentals/using-gen-ai-content (atualizada em 01/10/2026)
- [G18] Control what you share with Google Search. https://developers.google.com/search/docs/crawling-indexing/control-what-you-share (atualizada em 21/10/2026)
- [G19] List of Google's common crawlers (Google-Extended). https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers (atualizada em 30/10/2026)
- [G20] Changes to HowTo and FAQ rich results (blog, 08/08/2023). https://developers.google.com/search/blog/2023/08/howto-faq-changes
- [G21] Search Console Help, Search generative AI control. https://support.google.com/webmasters/answer/16908024
- [G22] Search Console Help, Generative AI performance report. https://support.google.com/webmasters/answer/16984139
- [G23] Merchant Center Help, Product data specification. https://support.google.com/merchants/answer/7052112
- [G24] Merchant Center Help, Free listings for products. https://support.google.com/merchants/answer/13889434
- [G25] Merchant Center Help, Supported languages and currencies. https://support.google.com/merchants/answer/160637
- [G26] Merchant Center Help, Insights for AI-powered shopping experiences (anúncio de 27/05/2026). https://support.google.com/merchants/answer/17117204
- [G27] Google, "New tech and tools for retailers to succeed in an agentic shopping era" (11/01/2026). https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/
- [G28] Google Brasil, "Busca do Google: agora o Brasil já pode usar o Modo IA em português" (08/09/2025). https://blog.google/intl/pt-br/produtos/busca-do-google-agora-o-brasil-ja-pode-usar-o-modo-ia-em-portugues/
- [G29] Structured data markup that Google Search supports (search gallery). https://developers.google.com/search/docs/appearance/structured-data/search-gallery (atualizada em 16/10/2026)
- [G30] Introduction to structured data markup in Google Search. https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data (atualizada em 10/12/2025)
- [G31] web.dev, Build agent-friendly websites. https://web.dev/articles/ai-agent-site-ux (sem data)

**OpenAI**
- [O1] Overview of OpenAI Crawlers. https://developers.openai.com/api/docs/bots (sem data; o endereço antigo platform.openai.com/docs/bots redireciona para cá)
- [O2] Power product discovery in ChatGPT (merchants). https://chatgpt.com/merchants/ (sem data)
- [O3] Agentic Commerce Protocol, Get started. https://developers.openai.com/commerce/guides/get-started (sem data)
- [O4] Agentic Commerce Protocol, Best practices. https://developers.openai.com/commerce/guides/best-practices (sem data)
- [O5] Agentic Commerce Protocol, visão geral. https://developers.openai.com/commerce (sem data)

**Perplexity**
- [P1] Perplexity Crawlers. https://docs.perplexity.ai/docs/resources/perplexity-crawlers (sem data)
- [P2] Shop like a Pro (18/11/2024). https://www.perplexity.ai/hub/blog/shop-like-a-pro
- [P3] Perplexity for Merchants. https://www.perplexity.ai/merchants (em 09/11/2026 não descreve programa de lojistas)

**Microsoft**
- [M1] Bing Webmaster Guidelines. https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a (sem data)
- [M2] Bing Webmaster Tools, New AI Preferences (anúncio de 30/10/2026). https://www.bing.com/webmasters/help/new-ai-preferences-2t1cc16d
- [M3] AI Performance in Bing Webmaster Tools. https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c
- [M4] Introducing AI Performance in Bing Webmaster Tools Public Preview (10/02/2026). https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview
- [M5] Microsoft Advertising, Agentic Commerce. https://about.ads.microsoft.com/en/solutions/technology/agentic-commerce (sem data)

**schema.org** (versão V30.1, 16/09/2026)
- [S1] https://schema.org/Product
- [S2] https://schema.org/Offer
- [S3] https://schema.org/MerchantReturnPolicy
- [S4] https://schema.org/ShippingService
- [S5] https://schema.org/ProductGroup

**Pesquisa**
- [R1] Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan, Deshpande. GEO: Generative Engine Optimization. KDD 2024. https://arxiv.org/abs/2311.09735 (v3, 28/06/2024)
- [R2] Puerto, Gubri, Green, Oh, Yun. C-SEO Bench: Does Conversational SEO Work? NeurIPS 2025 Datasets and Benchmarks. https://arxiv.org/abs/2506.11097 (v3, 20/10/2025)
- [R3] Bagga, Farias, Korkotashvili, Peng, Wu. E-GEO: A Testbed for Generative Engine Optimization in E-Commerce. https://arxiv.org/abs/2511.20867 (v2, 14/07/2026)
- [R4] Vishwakarma, Kumar, Jamidar. What Gets Cited: Competitive GEO in AI Answer Engines. https://arxiv.org/abs/2605.25517 (25/05/2026)
- [R5] Chen, Wang, Chen, Koudas. Generative Engine Optimization: How to Dominate AI Search. https://arxiv.org/abs/2509.08919 (10/09/2025)
- [R6] Zhang, He, Yao. From Citation Selection to Citation Absorption. https://arxiv.org/abs/2604.25707 (v2, 29/04/2026)
- [R7] Kumar, Lakkaraju. Manipulating Large Language Models to Increase Product Visibility. https://arxiv.org/abs/2404.07981 (v2, 02/09/2024)
- [R8] Pfrommer, Bai, Gautam, Sojoudi. Ranking Manipulation for Conversational Search Engines. EMNLP 2024. https://arxiv.org/abs/2406.03589
- [R9] Wu, Zhong, Kim, Xiong. What Generative Search Engines Like and How to Optimize Web Content Cooperatively (AutoGEO). https://arxiv.org/abs/2510.11438 (13/10/2025)
- [R10] Kumar. Generative Engine Optimization at Scale: Measuring Brand Visibility Across AI Search Engines. https://arxiv.org/abs/2606.20065 (18/06/2026)
- [R11] Yu, Yang, Ding, Sato. Structural Feature Engineering for Generative Engine Optimization (GEO-SFE). https://arxiv.org/abs/2603.29979 (31/03/2026)
- [R12] Pew Research Center. Google users are less likely to click on links when an AI summary appears in the results (22/07/2025). https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/

**Fornecedores**
- [V1] Ahrefs. We Tracked 1,885 Pages Adding Schema. AI Citations Barely Moved. (11/05/2026). https://ahrefs.com/blog/schema-ai-citations/
- [V2] Ahrefs. Update: 38% of AI Overview Citations Pull From The Top 10 (02/03/2026). https://ahrefs.com/blog/ai-overview-citations-top-10/
- [V3] Ahrefs. We Analyzed 137K Sites: 97% of llms.txt Files Never Get Read (15/06/2026). https://ahrefs.com/blog/llmstxt-study/
- [V4] Vercel e MERJ. The rise of the AI crawler (17/12/2024). https://vercel.com/blog/the-rise-of-the-ai-crawler
- [V5] Cloudflare, comunicado de imprensa de 01/07/2025. https://www.cloudflare.com/press/press-releases/2025/cloudflare-just-changed-how-ai-crawlers-scrape-the-internet-at-large/

**Legislação**
- [L1] Lei nº 8.078/1990 (Código de Defesa do Consumidor), art. 49. https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm
