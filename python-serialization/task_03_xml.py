#!/usr/bin/python3
import xml.etree.ElementTree as ET
"""
Function
"""


def serialize_to_xml(dictionary, filename):
    """
    Function
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def eserialize_from_xml(filename):

    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {}
        for child in root:
            data[child.tag] = child.text

        return data

    except FileNotFoundError:
        print(f"Erreur : Le fichier {filename} n'existe pas.")
        return None
