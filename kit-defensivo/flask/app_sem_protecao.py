"""Flask SEM headers anti-framing — demo didática. Porta 5001."""

from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def vitima():
    return render_template(
        "vitima.html",
        modo="sem proteção (headers ausentes)",
        protegida=False,
    )


@app.get("/teste")
def teste():
    return render_template(
        "teste.html",
        modo="sem proteção",
        protegida=False,
    )


if __name__ == "__main__":
    print("Sem proteção: http://127.0.0.1:5001/teste")
    app.run(host="127.0.0.1", port=5001, debug=False)
