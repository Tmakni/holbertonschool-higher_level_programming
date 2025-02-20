#!/usr/bin/python3
"""
This is my first HTTP requests handler
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
"""
Mandatory to handle requests
"""


class NeuralRequest(BaseHTTPRequestHandler):
    """
    In this class we implement how to handle requests
    """
    def do_GET(self):
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
