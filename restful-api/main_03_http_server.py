#!/usr/bin/python3
"""Script de test des endpoints de l'API sans dépendance externe (urllib)."""
import urllib.request
import urllib.error

PORT = 8000
BASE_URL = f"http://localhost:{PORT}"
endpoints = ['/', '/data', '/info', '/status', '/unknown']

if __name__ == '__main__':
    for path in endpoints:
        url = BASE_URL + path
        try:
            with urllib.request.urlopen(url) as resp:
                print(f"GET {path} -> {resp.getcode()}")
                print(f"Content-Type: {resp.info().get_content_type()}")
                print(f"Body: {resp.read().decode('utf-8')}\n")
        except urllib.error.HTTPError as e:
            print(f"GET {path} -> {e.code}")
            print(f"Error message: {e.read().decode('utf-8')}\n")
        except Exception as e:
            print(f"Erreur connexion à {url}: {e}\n")
