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
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == "/info":
            info = {"version": "1.0", "description": "A simple API built with http.server"}
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

if __name__ == '__main__':
    """
    Démarre le serveur HTTP sur le port 8000 dans un thread séparé,
    lance des requêtes de test sur tous les endpoints définis,
    puis arrête proprement le serveur.
    """
    import threading
    import time
    import urllib.request
    import urllib.error

    PORT = 8000
    server = socketserver.TCPServer(("", PORT), http_SubClass)
    print(f"Serveur démarré sur le port {PORT}")

    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()

    time.sleep(0.5)

    BASE_URL = f"http://localhost:{PORT}"
    endpoints = ['/', '/data', '/info', '/status', '/unknown']

    for path in endpoints:
        url = BASE_URL + path
        try:
            with urllib.request.urlopen(url) as resp:
                status = resp.getcode()
                ctype = resp.info().get_content_type()
                body = resp.read().decode('utf-8')
                print(f"GET {path} -> {status} | Content-Type: {ctype} | Body: {body}")
        except urllib.error.HTTPError as e:
            err_body = e.read().decode('utf-8')
            print(f"GET {path} -> {e.code} | Error: {err_body}")
        except Exception as e:
            print(f"Échec connexion {url}: {e}")

    server.shutdown()
    server.server_close()
