# Checklist — verificar proteção anti-clickjacking

Use no DevTools do Chrome/Firefox/Edge (F12).

## 1. Headers na resposta da página-alvo

1. Abra a URL da **vítima** (não só a página de teste).
2. Aba **Network** → recarregue (Ctrl+R).
3. Clique no documento `vitima` / `/` / `vitima.html`.
4. Aba **Headers** → **Response Headers**.

### Com proteção (esperado)

- `X-Frame-Options: DENY`  
  **ou** `SAMEORIGIN` (só permite frames do mesmo site)
- e/ou  
  `Content-Security-Policy: frame-ancestors 'none'`  
  **ou** `frame-ancestors 'self'` / lista explícita de origens confiáveis

### Sem proteção (esperado na demo)

- Ausência desses headers (ou valores permissivos demais).

## 2. Comportamento do iframe

Na página `teste-iframe` / `/teste`:

| Cenário | O que o aluno deve ver |
|---------|-------------------------|
| Sem proteção | Conteúdo da vítima dentro do quadro |
| Com proteção | Quadro vazio / erro / bloqueio; console pode citar framing |

## 3. Console (opcional)

- Mensagens do browser sobre recusa de exibir a página em um frame.
- Em `vitima-framebust.html`: log “Esta página está dentro de um frame” se embutida **e** JS habilitado.

## 4. Perguntas rápidas para a turma

1. Por que meta tag não resolve `frame-ancestors`?
2. Qual a diferença entre `DENY` e `SAMEORIGIN`?
3. Por que frame-busting sozinho não basta?
4. O atributo `sandbox` no iframe protege o site da vítima? (Não.)
