#!/usr/bin/env python3
"""Flask task 03 : affiche des produits depuis JSON ou CSV."""

from flask import Flask, render_template, request
import json, csv
from pathlib import Path
from typing import List, Dict

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent


def read_json() -> List[Dict]:
    path = BASE_DIR / "products.json"
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv() -> List[Dict]:
    path = BASE_DIR / "products.csv"
    items = []
    try:
        with path.open(encoding="utf-8") as f:
            for row in csv.DictReader(f):
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                items.append(row)
    except FileNotFoundError:
        pass
    return items


@app.route("/products")
def products():
    source = request.args.get("source", "").lower()
    product_id = request.args.get("id", type=int)

    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    else:
        return render_template("product_display.html",
                               error="Wrong source", products=[])

    if product_id is not None:
        data = [p for p in data if p["id"] == product_id]
        if not data:
            return render_template("product_display.html",
                                   error="Product not found", products=[])

    return render_template("product_display.html",
                           error=None, products=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
