#!/usr/bin/python3
"""
Serialisation
"""


def convert_csv_to_json(csv_filename):
    import csv
    import json

    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

            with open('data.json', 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
