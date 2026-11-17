"""Serve arquivos estáticos SEM headers anti-framing. Porta 8001."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

PORT = 8001
ROOT = Path(__file__).resolve().parent


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Sem proteção: http://127.0.0.1:{PORT}/teste-iframe.html")
    server.serve_forever()
