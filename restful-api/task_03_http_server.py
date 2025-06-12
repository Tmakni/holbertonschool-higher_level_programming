#!/usr/bin/python3
"""
Ceci est une API simple construite avec http.server.
Démo minimaliste avec un handler GET et un serveur HTTP.
"""
import http.server
import json


class http_SubClass(http.server.BaseHTTPRequestHandler):
    """
    Gestionnaire de requêtes HTTP GET minimaliste.
    Redéfinit do_GET pour renvoyer des réponses selon l'URL.
    """

    def do_GET(self):
        """
        Traitement des requêtes GET :
        - '/'       : message texte simple
        - '/data'   : JSON d'exemple
        - '/status' : texte OK
        - autre     : 404 Not Found
        """

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(payload).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            payload = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(payload).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == '__main__':
    """
    Lancement du serveur HTTP sur le port 8000.
    """

    PORT = 8000
    server = http.server.HTTPServer(("", PORT), http_SubClass)
    print(f"Serving on port {PORT}")
    server.serve_forever()
