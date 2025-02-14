#!/usr/bin/env python3
"""Ceci est une description"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Ceci est une description"""
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True

    except Exception as e:
        print(f"Erreur lors de la sérialisation : {e}")
        return False


def deserialize_from_xml(filename):
    """Ceci est une description"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result

    except Exception as e:
        print(f"Erreur lors de la désérialisation : {e}")
        return {}
