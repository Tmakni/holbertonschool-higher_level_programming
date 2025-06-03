#!/usr/bin/python3
"""
Serialisation
"""


def serialize_and_save_to_file(data, filename):
    """Sérialise un dictionnaire et le sauvegarde dans un fichier JSON."""
    with open(filename, 'w') as file:
        file.write(str(data).replace("'", '"'))


def load_and_deserialize(filename):
    """Charge un fichier JSON et retourne un dictionnaire Python."""
    with open(filename, 'r') as file:
        content = file.read()
        return eval(content.replace("null", "None"))
