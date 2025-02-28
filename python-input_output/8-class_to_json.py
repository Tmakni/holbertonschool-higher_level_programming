#!/usr/bin/python3


def class_to_json(obj):
    """
    Retourne le dictionnaire de description de l'objet
    qui peut être sérialisé en JSON
    """
    return {key: value for key, value in obj.__dict__.items()
            if isinstance(value, (str, int, bool, list, dict))}
