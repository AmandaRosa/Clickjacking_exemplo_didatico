"""EXEMPLO DIDÁTICO — defesa recomendada contra clickjacking no Flask.

Envia X-Frame-Options e CSP frame-ancestors em todas as respostas, impedindo
que as páginas da aplicação sejam embutidas em iframes de outros sites.
"""

from flask import Flask

app = Flask(__name__)


@app.after_request
def security_headers(response):

    response.headers["X-Frame-Options"] = "DENY"

    response.headers[
        "Content-Security-Policy"
    ] = "frame-ancestors 'none'"

    return response