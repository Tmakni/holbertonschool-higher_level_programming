#!/usr/bin/python3


def read_file(filename=""):
    """
    Fonction pour ecrire tout les caractères avec utf-8
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
