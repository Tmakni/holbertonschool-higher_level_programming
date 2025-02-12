#!/usr/bin/python3
"""fonction"""
import sys
import json


def load_from_json_file(filename):
    """fonction"""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)


def save_to_json_file(my_obj, filename):
    """fonction"""
    with open(filename, "w", encoding="utf-8") as file:
        this = file.write(json.dumps(my_obj))
    return this


filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
