#!/usr/bin/python3
"""
Ceci est une API simple construite avec http.server et socketserver.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
"""
Ceci est une API simple construite avec http.server et socketserver.
"""


class http_SubClass(http.server.BaseHTTPRequestHandler):
    """
    Gestionnaire de requêtes HTTP GET pour notre API simple.
    """
    def do_GET(self):
        """
        Traitement des requêtes GET
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode())
        elif self.path == '/data':
            self.send_response(200)
            object = {"name": "John", "age": 30, "city": "New York"}
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(object).encode())
        elif self.path == '/info':
            self.send_response(200)
            object = {"version": "1.0", "description": "A simple API built "
                      "with http.server"}
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(object).encode())
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode())


PORT = 8000
server = HTTPServer(("", PORT), NeuralRequest)
server.serve_forever()
