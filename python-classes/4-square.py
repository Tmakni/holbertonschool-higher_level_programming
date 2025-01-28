#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        """Initialise un carré avec une taille optionnelle."""
        self.size = size  # Appelle le setter pour valider et initialiser la taille


    @property
    def size(self):
        """Getter pour récupérer la taille du carré."""
        return self._size


    @size.setter
    def size(self, value):
        """Setter pour valider et définir la taille du carré."""
        if not isinstance(value, int):  # Vérifie si la taille est un entier
            raise TypeError("size must be an integer")
        if value < 0:  # Vérifie si la taille est positive ou nulle
            raise ValueError("size must be >= 0")
        self._size = value  # Assigne la taille validée


    def area(self):
        """Retourne l'aire du carré."""
        return self._size ** 2  # Calcul de l'aire (côté au carré)
