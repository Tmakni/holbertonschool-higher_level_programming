#!/usr/bin/python3


def read_file(filename=""):
    """
    Fonction qui lit un fichier texte (en encodage UTF-8) et affiche
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
