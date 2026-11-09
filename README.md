# Time de SEO e GEO

**[Baixe o guia grátis em PDF](https://fabiowill.github.io/time-de-seo-geo/)** e use no Claude ou no ChatGPT.

Três agentes fazendo um trabalho real de marketing: medir a página de um produto, reescrever para
o Google (SEO) e para os assistentes de IA (GEO: ChatGPT, Gemini, AI Overviews, Perplexity) e
conferir cada fato antes de alguém publicar.

- O **Auditor** mede a página com uma régua pública, por código.
- O **Redator** reescreve sem inventar nada.
- O **Revisor** confere cada fato e devolve se algo não bater.
- **Você** aprova.

Testado em quatro lojas reais (Stanley, Fast Shop, Decathlon e KaBuM), em Shopify, VTEX e
plataforma própria, com modelos fortes e fracos, com e sem ferramenta de código. Não precisa saber programar: escolha um
dos dois caminhos.

| Caminho | Para quem | O que precisa |
|---|---|---|
| **1. No seu chat** | qualquer pessoa | o PDF e uma conta no Claude ou no ChatGPT |
| **2. No OpenBot** | quem quer ver três agentes trabalhando no próprio computador | Mac ou PC, 30 minutos e uma assinatura do Claude ou do ChatGPT |

## O que tem aqui

| Arquivo ou pasta | O que é |
|---|---|
| [`pdf/Time de SEO e GEO no seu chat.pdf`](pdf/) | o guia para usar no Claude ou no ChatGPT |
| [`preparar.html`](https://fabiowill.github.io/time-de-seo-geo/preparar.html) | deixa a página salva pronta para anexar no chat (roda no seu navegador, nada é enviado) |
| [`regua/regua.md`](regua/regua.md) | os critérios de SEO e GEO, com a fonte de cada regra |
| [`pesquisa/`](pesquisa/boas-praticas-seo-geo.md) | o levantamento de boas práticas: documentação do Google, do Bing, da OpenAI e da Perplexity, e os estudos sobre GEO |
| [`agentes/`](agentes/) | as instruções dos três agentes, prontas para colar |
| [`conferir/`](conferir/) | o conferidor (mede a página sem chute) e os testes dele |
| [`casos/`](casos/) | os quatro casos reais, com prints e notas |
| [`exemplo/`](exemplo/) | uma página de treino (marca e loja fictícias) com a ficha técnica |

## Caminho 1: no seu chat (5 minutos)

1. **Salve a página do produto.** No Chrome, aperte `Cmd + S` (Mac) ou `Ctrl + S` (Windows) e
   escolha "Página da Web, completa".
2. **Prepare o arquivo.** Abra o [preparador](https://fabiowill.github.io/time-de-seo-geo/preparar.html)
   e arraste o `.html` salvo. Página de loja costuma ter de 0,5 a 3 MB de código; preparada, fica
   umas dez vezes menor e cabe no chat. Testado nas lojas reais: a nota não muda.
3. **Abra um chat novo** no Claude ou no ChatGPT e anexe o PDF e a página preparada.
4. **Cole a frase** da página 8 do PDF, com a sua palavra-chave e os fatos do produto (ou "use só
   a página").

Para treinar antes, use `exemplo/pagina-antes.html` e `exemplo/ficha-tecnica.md`.

## Caminho 2: no OpenBot

O [OpenBot](https://openbot.run) é um aplicativo que roda um time de agentes no seu computador. Ele
usa a assinatura que você já tem (Claude Code, Codex, Gemini e outros). Cada agente tem nome,
instruções e pasta própria, e os agentes passam tarefas uns para os outros.

### Antes de instalar, leia isto

**Segurança.** Por padrão, os agentes do OpenBot rodam com acesso total ao computador
(`danger-full-access`) e sem pedir aprovação a cada ação (`approvalPolicy: never`): abrem e alteram
arquivos, rodam comandos, usam a internet e controlam o navegador. A própria documentação deles diz
isso e recomenda dar só tarefas confiáveis e manter backup.

Por isso, **não instale no seu usuário do dia a dia**, onde ficam e-mail, senhas salvas, documentos
e chaves de acesso. Crie um usuário só para o teste:

1. Abra **Ajustes do Sistema > Usuários e Grupos > Adicionar usuário**.
2. Escolha o tipo **Padrão** (não Administrador), dê um nome como "Laboratório" e uma senha.
3. Saia da sua conta e entre na conta nova. Tudo daqui para frente acontece lá.

No Windows, o caminho equivalente é **Configurações > Contas > Outros usuários**.

**Licença.** O OpenBot é grátis para uso pessoal, estudo e teste (PolyForm Noncommercial 1.0.0).
Para usar numa empresa, é preciso licença comercial (licenses@openbot.run).

### Passo a passo

1. **Baixe este repositório** sem precisar de git: no topo desta página, botão verde **Code** e
   depois **Download ZIP**. Abra o ZIP e guarde a pasta.
2. **Instale o OpenBot** em [openbot.run](https://openbot.run). Em Mac com chip Apple, o arquivo
   termina em `arm64.dmg`.
3. **Conecte a sua assinatura.** Na primeira tela, o OpenBot pede para conectar um provedor
   (Claude Code ou Codex). Siga o login que ele abre.
4. **Crie os três agentes.** Para cada um, crie um agente novo, use como pasta de trabalho a pasta
   deste repositório e cole nas instruções o texto do arquivo correspondente em `agentes/`.
5. **Crie um canal com os três** e mande para o Auditor:

   > Audite a página exemplo/pagina-antes.html. Palavra-chave: garrafa térmica inox 500 ml.
   > Endereço: https://www.exemplo.com/produto.php?id=8812. Os fatos do produto estão em
   > exemplo/ficha-tecnica.md. Quando terminar, passe para o Redator, que passa para o Revisor.

6. **Leia o `resumo-para-aprovar.md`** que o Revisor deixa na pasta. Nada é publicado sem você.

O Auditor roda o conferidor com Python. No Mac, se aparecer um aviso pedindo para instalar as
"ferramentas de linha de comando", aceite: é o pacote da Apple que traz o Python.

## Como ler o resultado

São duas notas, cada uma de 0 a 100, como uma prova:

- **SEO**: o quanto o Google consegue entender e mostrar a página (título, dados do produto,
  preço, imagens, frete e devolução). 16 critérios.
- **GEO**: o quanto um assistente de IA (ChatGPT, a IA do Google, Perplexity) consegue usar a
  página para responder e citar você (frase de abertura, especificações, preço em texto, fatos
  que não se contradizem). 10 critérios.

Cada critério tem um peso: o schema do produto vale 14 pontos, o endereço legível vale 3. **Passa**
vale o peso inteiro, **metade** vale metade, **falha** vale zero. Somando tudo, cada nota chega no
máximo a 100.

| Faixa | Leitura |
|---|---|
| 0 a 49 | falta o básico |
| 50 a 79 | boa base, com pontos a melhorar |
| 80 a 100 | página bem preparada |

As faixas são uma leitura deste guia, para orientar. A nota mede o que está na página, que é a
parte que você controla; não é posição no Google. Cinco critérios de GEO dependem de ler o texto:
neles o agente decide e copia a frase que justifica. Página bloqueada não recebe nota: o relatório
diz "não foi possível ler".

## Casos reais

Lidos em 09/11/2026 com o mesmo conferidor. Detalhes, prints e achados em [`casos/`](casos/).

| Loja | Plataforma | SEO | O que mais dá para melhorar |
|---|---|---|---|
| Stanley, loja oficial | Shopify | 66 | a página diz 28 horas e 24 horas para a mesma coisa |
| Fast Shop | VTEX | 78 | especificações num parágrafo só |
| Decathlon | VTEX | 84 | nota de 3.671 avaliações visível, mas fora do schema |
| KaBuM | própria | 64 | o título da página é de promoção, não do produto |

Na página da Stanley, o time levou o SEO de 66 para 94 e o GEO de 71 para 100, numa simulação
feita a partir da página pública, sem inventar nenhum dado.

## O conferidor (para quem é técnico)

```bash
python3 conferir/conferir.py pagina.html \
  --palavra-chave "garrafa térmica stanley classic" \
  --url "https://loja.com.br/produto" \
  --descricao ".classe-da-descricao" \
  --renderizado pagina-depois-do-js.html
```

- Só biblioteca padrão do Python, sem internet.
- `--renderizado` mostra o que só aparece depois do JavaScript (na medição publicada pela Vercel,
  os robôs de IA do ChatGPT, do Claude e do Perplexity não executavam JavaScript).
- `--julgamento arquivo.json` recebe a decisão do agente nos critérios de leitura e fecha as notas.
- `--json` devolve o resultado para outro programa.
- Testes: `python3 conferir/test_conferir.py`. Cada teste é uma armadilha achada numa loja real.

## A régua

Parte dos critérios do Absoluto SEO, revista em novembro de 2026 com a
documentação oficial e os estudos publicados. Saíram as regras sem fonte (tamanho fixo de título e
meta, 300 palavras, densidade de palavra-chave, `FAQPage` e "schema para IA"). Entraram as que o
Google, o Bing e os estudos pedem (conteúdo no HTML inicial, schema igual ao texto, identificadores,
frete e devolução, preço em texto, especificações em pares, fatos sem contradição). Cada regra tem a
fonte em [`regua/regua.md`](regua/regua.md).

## Precisa de ajuda na sua loja?

Faço diagnóstico, plano e mentoria de SEO e GEO para lojas e sites em Shopify, VTEX, Nuvemshop,
Loja Integrada, WooCommerce e Magento. Além do conteúdo, olho a parte técnica que este guia não
mede: desempenho (Lighthouse e Core Web Vitals), segurança do site e robôs de IA no robots.txt.
Fale comigo pelo [WhatsApp](https://absoluto.ai/whats) ou pelo
[contato da Absoluto](https://absoluto.ai/contato).

## Licença

Textos, PDF, régua e pesquisa: [CC BY 4.0](LICENSE-CONTEUDO.md) (pode usar e adaptar, citando a
fonte). Código: [MIT](LICENSE). Marcas e páginas citadas pertencem aos donos; os prints
são de páginas públicas, usados para estudo.

**Fábio Will** · A Absoluto é a empresa que eu fundei.
