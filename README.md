# Clickjacking — material didático

Exemplos de aula sobre **clickjacking** (UI redressing) e suas **defesas**, produzidos para a disciplina de Cibersegurança.

> ⚠️ **Uso exclusivamente educacional.** Rode os exemplos apenas em `localhost` ou em sites que sejam seus. Não use este material contra sites de terceiros.

## Conteúdo

| Arquivo | O que mostra |
|---|---|
| `exemplo.html` | Uma página embutida em `<iframe>` — base do ataque |
| `exemplo2.html` + `design.css` | Botão invisível (`opacity: 0`) sobreposto ao iframe |
| `sandbox.html` | Atributo `sandbox` do iframe |
| `exemplo.js` | Frame-busting em JavaScript (defesa frágil) |
| `headers_flask.py` | Defesa recomendada: `X-Frame-Options` e `CSP frame-ancestors` no Flask |
| `kit-defensivo/` | Roteiro completo da aula com vítima sem/com proteção e checklist |

## Como rodar

Os exemplos da raiz embutem a página-vítima do kit, servida em `http://127.0.0.1:8001`.
Siga o roteiro em [`kit-defensivo/README.md`](kit-defensivo/README.md) para subir os servidores e depois abra os `exemplo*.html` no navegador.

Para o kit em Flask:

```bash
cd kit-defensivo/flask
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Defesa em resumo

O site-alvo deve impedir que seja embutido por terceiros enviando o header:

```
Content-Security-Policy: frame-ancestors 'none'
X-Frame-Options: DENY
```

Frame-busting em JS (`exemplo.js`) pode ser contornado e não deve ser a única defesa.

## Referências

- OWASP — Clickjacking Defense Cheat Sheet
- MDN — `Content-Security-Policy: frame-ancestors`

## Licença

MIT — veja [LICENSE](LICENSE).
