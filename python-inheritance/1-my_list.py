class MyList(list):
    """Classe qui hérite de list et ajoute une méthode pour afficher une version triée de la liste."""
    
    def print_sorted(self):
        """Affiche la liste triée sans modifier l'originale."""
        print(sorted(self))
