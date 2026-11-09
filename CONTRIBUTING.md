# Como contribuir

Achou uma regra sem fonte, uma página onde o conferidor erra ou um caso novo? Abra uma issue com o
endereço da página e o que você esperava.

## Antes de mandar um pull request

- Rode os testes do conferidor: `python3 conferir/test_conferir.py` (só biblioteca padrão).
- Toda armadilha nova achada numa loja real vira um teste em `conferir/test_conferir.py`.
- Regra nova na régua precisa de fonte (documentação oficial ou estudo publicado) em
  `regua/regua.md`.
- Nada de dado pessoal, token ou print com informação de sessão.

## Mensagens de commit

Seguimos [Conventional Commits](https://www.conventionalcommits.org/pt-br/) com escopo
obrigatório. O hook do `commitlint` confere ao commitar (rode `npm install` uma vez para ligá-lo).

```
<tipo>(<escopo>): <o que muda, no imperativo>
```

| Tipo | Quando |
|---|---|
| `feat` | critério novo, caso novo, recurso novo no preparador |
| `fix` | correção de leitura ou de nota |
| `docs` | README, guia, pesquisa |
| `test` | teste novo do conferidor |
| `refactor`, `chore` | o resto |

Escopos: `regua`, `conferir`, `preparar`, `guia`, `casos`, `pesquisa`, `agentes`, `exemplo`,
`repo`.

Exemplo: `fix(conferir): ignorar title dentro de svg ao medir o título`
