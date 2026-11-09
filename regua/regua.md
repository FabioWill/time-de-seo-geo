# A régua: SEO e GEO, cada grupo soma 100

- **SEO** é o que o Google lê para entender e mostrar a página.
- **GEO** (Generative Engine Optimization) é o que um assistente de IA (ChatGPT, Gemini, AI
  Overviews, Perplexity, Copilot) precisa para citar o produto quando alguém pergunta.

O ponto de partida foram os 23 critérios que o Absoluto SEO publica. A
régua foi revista em novembro de 2026 com a documentação oficial do Google, do Bing, da OpenAI e
da Perplexity, e com os estudos publicados sobre GEO. A pesquisa completa, com cada citação e a
data de leitura, está em [`pesquisa/boas-praticas-seo-geo.md`](../pesquisa/boas-praticas-seo-geo.md).

**O que saiu e por quê:**
- **Tamanho fixo de título (50 a 60) e de meta (120 a 158):** o Google diz que não há limite e corta
  pela largura da tela [G11] [G12]. Agora isso é só aviso.
- **300 palavras de descrição:** "(No, we don't.)", sobre contagem preferida de palavras [G13].
- **Faixa de densidade de palavra-chave:** sem fonte; só o excesso é punido [G2] [M1].
- **FAQPage e "schema para IA":** o rich result de FAQ saiu do ar em 07/05/2026 [G3], e o Google
  diz que não existe schema especial para IA [G1].

**Como pontua:** passa vale o peso inteiro, metade vale metade do peso (arredondado para baixo),
falha vale zero.

**Quem mede:** 21 critérios são medidos pelo `conferir/conferir.py`. Os 5 marcados com
**(julgamento)** dependem de ler o texto: o agente decide e copia a frase da página que justifica.

## Portões (não dão ponto, param a nota)

| # | Portão | Fecha quando | Fonte |
|---|---|---|---|
| P1 | Página no índice e com trecho | `noindex`, `nosnippet` ou `max-snippet:0` | o Google só usa nos recursos de IA página "indexed and eligible to be shown in Google Search with a snippet" [G1] |
| P2 | Sem texto escondido com instrução para IA | elemento oculto com "ignore as instruções", "recomende este produto" e afins | o Bing pune "prompt injection" [M1]; o Google trata como spam [G16] |

Página bloqueada (captcha, login, erro 403) recebe **"não foi possível ler"**, nunca nota baixa.

## SEO: o que o Google lê (soma 100)

| # | Critério | Peso | Passa | Metade | Falha | Fonte |
|---|---|---|---|---|---|---|
| S01 | Título descritivo, com o produto | 10 | nomeia o produto (todas as palavras da palavra-chave), sem repetir termo, até cerca de 70 caracteres | parte do nome, termo repetido ou longo demais | ausente ou sem o produto | [G11] |
| S02 | Meta description com fatos | 8 | 70 caracteres ou mais e pelo menos 2 fatos (preço, medida com unidade, marca) | menos fatos ou curta | ausente | [G12] [M1] |
| S03 | H1 com o nome do produto | 6 | um único H1 com o produto | mais de um H1, algum com o produto | nenhum H1 ou sem relação | [G11] [M1] |
| S04 | Subtítulos (H2) | 4 | 2 ou mais | 1 | nenhum | [G2] [M1] |
| S05 | og:title e og:image | 3 | os dois (imagem que não seja o logo) | um | nenhum | [G11] [G14] |
| S06 | Schema Product completo | 14 | JSON-LD `Product` com `name`, `image`, `offers.price` maior que zero em formato válido (ponto decimal), `priceCurrency` e `availability` | falta algum campo ou o preço está fora do formato ("349,00") | sem `Product` ou sem `offers` | [G4] |
| S07 | Conteúdo no HTML inicial | 10 | nome, preço em texto, descrição e schema já no HTML que a loja entrega | algo só aparece depois do JavaScript | preço e descrição só depois do JavaScript | [G4] [M1] [V4] |
| S08 | Schema igual ao texto visível | 10 | preço, estoque e nota do schema batem com a página | divergência leve (nome do schema fora do H1, preço em formato inválido) | preço diferente, estoque contraditório, nota sem nota visível ou `priceValidUntil` vencido | [G10] [G9] |
| S09 | Identificadores (GTIN, MPN, marca) | 8 | GTIN com dígito verificador válido mais marca, ou MPN mais marca | só `sku`, GTIN inválido ou sem marca | nenhum | [G4] [G23] |
| S10 | Frete e devolução | 6 | `shippingDetails` e `hasMerchantReturnPolicy` no schema | só o texto ou o link da política | nada | [G4] [G7] [G8] |
| S11 | Imagens com alt e no schema | 7 | todas as fotos do produto com `alt` e imagem no schema | metade ou mais com `alt` | menos da metade | [G14] [G4] |
| S12 | Endereço legível | 3 | trecho descritivo só com minúsculas, números e hífens, até 75 caracteres | outro formato (`produto.php?id=`) | sem endereço | [G15] |
| S13 | Canonical coerente | 3 | presente e apontando para a própria página | ausente ou apontando para outra | | [G10] |
| S14 | Trilha, categoria e links internos | 3 | `BreadcrumbList`, `Product.category` e links internos | dois dos três | um ou nenhum | [G1] [G29] |
| S15 | Avaliação visível e no schema | 3 | `aggregateRating` com nota e contagem, e a mesma nota visível | sem avaliação (recomendação, não obrigação) | nota no schema sem nota visível | [G9] |
| S16 | Variantes marcadas | 2 | `ProductGroup` ou variantes ligadas; "não se aplica" conta como passa | variantes só como várias ofertas | página oferece cor ou tamanho sem markup de variante | [G6] |

## GEO: o que um assistente de IA lê para citar o produto (soma 100)

| # | Critério | Peso | Passa | Metade | Falha | Fonte |
|---|---|---|---|---|---|---|
| G01 | Abertura direta **(julgamento)** | 15 | a primeira frase da descrição diz o que é o produto e o benefício principal, com um dado | diz o que é, mas o benefício é vago ou só um elogio ("ótima qualidade") | não diz o que é o produto ("Confira!") | [M1] [R3] |
| G02 | Especificações em pares | 16 | 5 ou mais pares atributo: valor na descrição (linha de tabela, `<dl>` ou item de lista com dois-pontos) | 2 a 4 pares | 0 ou 1 (lista de benefícios genéricos não conta) | [M1] [R4] |
| G03 | Produto bem identificado **(julgamento)** | 14 | a descrição nomeia marca, linha ou modelo, categoria e material ou capacidade (título e H1 não contam) | 2 ou 3 desses | 1 ou nenhum | [M1] [G4] |
| G04 | Dados concretos e sem contradição **(julgamento)** | 12 | promessas com número ou fato ("até 12 horas", "500 ml"), sem frase vaga e sem número que contradiz outro da mesma página | mistura de dado e frase vaga | quase tudo vago, ou a página se contradiz (24 horas num lugar, 28 no outro) | [M1] [R3] [R6] |
| G05 | Preço e estoque em texto | 10 | preço e situação de estoque legíveis no texto | só um dos dois | nenhum, ou só em imagem | [R4] [G4] |
| G06 | Para quem é e quando usar **(julgamento)** | 10 | diz para quem é e cita situações concretas de uso, ou compara com alternativa | só "para o dia a dia" | não diz | [R3] [R4] |
| G07 | Descrição própria **(julgamento)** | 8 | texto próprio que cobre os atributos da ficha | parte é texto genérico do fabricante ou repetido de outros produtos | menos de 50 palavras (o código reprova sozinho) ou cópia | [G2] [M1] |
| G08 | Perguntas de comprador respondidas | 6 | 3 ou mais perguntas visíveis na página, respondidas com fato | 1 ou 2 | nenhuma (`FAQPage` sozinho não conta) | [R3] [R6] [G3] |
| G09 | Texto fácil de escanear | 5 | nenhum bloco da descrição com mais de 45 palavras | até metade dos blocos | mais da metade | [M1] |
| G10 | Idioma e moeda coerentes | 4 | `<html lang="pt-BR">` e moeda BRL | `lang` ausente | moeda diferente | [G11] |

## Duas regras que valem mais do que qualquer ponto

1. **Nenhum fato sai de fora da ficha do produto.** Se a medida, a promessa ou a avaliação não está
   na ficha, ela não entra no texto. O Google manda revisar todo texto gerado por IA, inclusive
   metadados e schema [G17], e a factualidade foi o único traço comum a todos os textos que
   funcionaram no estudo E-GEO [R3]. Acrescentar estatística ou citação genérica não ajuda em
   página de produto [R2].
2. **Critério que não foi lido não é critério ruim.** Página bloqueada recebe "não foi possível
   ler". O que só aparece depois do JavaScript entra como defeito real no S07, porque os robôs de
   IA medidos não executam JavaScript [V4].

## Fontes citadas

As referências entre colchetes estão em
[`pesquisa/boas-praticas-seo-geo.md`](../pesquisa/boas-praticas-seo-geo.md#9-fontes), com o
endereço e a data de leitura de cada uma.
