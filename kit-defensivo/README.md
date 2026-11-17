# Kit defensivo — Clickjacking (aula)

Material para **explicar o risco** e **demonstrar mitigações**.  
Não inclui PoC de ataque (overlay, isca, botão transparente).

## Objetivo da aula

1. Entender o que é clickjacking (conceitualmente).
2. Ver que página **sem** headers pode ser embutida em iframe.
3. Ver que `X-Frame-Options` / `CSP frame-ancestors` **bloqueiam** o embutimento.
4. Comparar defesa por header (recomendada) vs frame-busting em JS (frágil).

## Conceito

Clickjacking: a vítima é induzida a clicar em algo que acredita ser da página visível, mas o clique atinge um elemento de outra origem embutida (tipicamente via iframe).  
A defesa correta é o **site-alvo** impedir que seja embutido por terceiros.

### Detalhe didático da página-vítima

- Botão rotulado **Adquira seu brinde!** (aparência “inofensiva”).
- Ao clicar, um `alert` mostra **Dinheiro transferido** — ilustra ação sensível escondida atrás de um rótulo enganoso (conceito; sem PoC de overlay).
- No Flask: faixa **vermelha** = sem proteção; faixa **verde** = headers ativos.
- Abrir só `/` ou `vitima.html` “funciona” nas duas apps: a diferença aparece no **iframe** (`/teste` ou `teste-iframe.html`) e nos **headers** (veja `checklist.md`).

## Estrutura

```
kit-defensivo/
├── README.md                 ← este roteiro
├── checklist.md              ← verificação no DevTools
├── estatico/                 ← HTML + servidores mínimos
└── flask/                    ← duas apps Flask (com/sem proteção)
```

## Demonstração A — HTML estático

Em dois terminais (portas diferentes):

```bash
# Terminal 1 — vítima SEM proteção (porta 8001)
cd kit-defensivo/estatico
python3 serve_sem_protecao.py

# Terminal 2 — vítima COM proteção (porta 8002)
python3 serve_protegido.py
```

No navegador:

1. Abra `http://127.0.0.1:8001/vitima.html` — página normal.
2. Abra `http://127.0.0.1:8001/teste-iframe.html` — o iframe **carrega** a vítima.
3. Abra `http://127.0.0.1:8002/teste-iframe.html` — o iframe da vítima protegida **não** deve aparecer (bloqueio do browser).
4. Em DevTools → Network → resposta de `vitima.html` na porta 8002: confira os headers (veja `checklist.md`).

Frame-busting (defesa frágil, só didática):

- `http://127.0.0.1:8001/vitima-framebust.html`
- Explique: depende de JS; headers HTTP são a solução real.

Configs de hospedagem estática: pasta `estatico/headers/`.

## Demonstração B — Flask

```bash
cd kit-defensivo/flask

# Sem proteção (porta 5001)
python3 app_sem_protecao.py

# Em outro terminal — com proteção (porta 5002)
python3 app_protegida.py
```

No navegador:

1. `http://127.0.0.1:5001/` — faixa vermelha; botão dispara o alerta (ação sensível simulada).
2. `http://127.0.0.1:5001/teste` — iframe da vítima **carrega**.
3. `http://127.0.0.1:5002/` — faixa verde (headers ativos); página sozinha ainda abre normalmente.
4. `http://127.0.0.1:5002/teste` — iframe **vazio/bloqueado** = mitigação ok.
5. Confira headers em Network (mesma checklist).

## Mensagens-chave

| Abordagem | Serve? | Observação |
|-----------|--------|------------|
| `X-Frame-Options: DENY` | Sim | Amplamente suportado |
| `CSP: frame-ancestors 'none'` | Sim (preferível) | Mais flexível; padrão moderno |
| Meta tag HTML para `frame-ancestors` | Não | Só funciona via **header HTTP** |
| Frame-busting JS | Frágil | Bypass possível; não substituir headers |
| `sandbox` no iframe do atacante | Não protege a vítima | Quem embute controla o atributo |

