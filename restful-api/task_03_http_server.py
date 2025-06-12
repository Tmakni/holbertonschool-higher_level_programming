#!/usr/bin/python3
"""
Ceci est une API simple construite avec http.server et socketserver.
Elle définit plusieurs endpoints pour renvoyer du texte ou du JSON,
puis lance un serveur HTTP et exécute des tests automatiques.
"""
import http.server
import socketserver
import json


class http_SubClass(http.server.BaseHTTPRequestHandler):
    """
    Gestionnaire de requêtes HTTP GET pour notre API simple.
    Hérite de BaseHTTPRequestHandler et redéfinit do_GET pour traiter
    différents chemins d'URL et renvoyer les réponses appropriées.
    """
    def do_GET(self):
        """
        Traitement des requêtes GET :
        '/'       : renvoie un message texte "Hello, this is a simple API!"
        '/data'   : renvoie un JSON avec des données d'exemple
        '/info'   : renvoie un JSON avec la version et une description
        '/status' : renvoie un simple message texte "OK"
        autre     : renvoie un code 404 et un message d'erreur
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/info":
            dataset = {"version": "1.0", "description":
                    "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


PORT = 8000
server = HTTPServer(("", PORT), NeuralRequest)
server.serve_forever()
