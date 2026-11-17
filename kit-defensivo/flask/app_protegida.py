"""Flask COM X-Frame-Options + CSP frame-ancestors. Porta 5002."""

from flask import Flask, render_template

app = Flask(__name__)


@app.after_request
def security_headers(response):
    # Diferença real em relação a app_sem_protecao são os HEADERS.
    # A página aberta “sozinha” continua normal; o browser só bloqueia
    # quando alguém tenta colocá-la dentro de um iframe.
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "frame-ancestors 'none'"
    return response


@app.get("/")
def vitima():
    return render_template(
        "vitima.html",
        modo="protegida (X-Frame-Options + CSP frame-ancestors)",
        protegida=True,
    )


@app.get("/teste")
def teste():
    return render_template(
        "teste.html",
        modo="protegida",
        protegida=True,
    )


if __name__ == "__main__":
    print("Com proteção: http://127.0.0.1:5002/teste")
    app.run(host="127.0.0.1", port=5002, debug=False)
