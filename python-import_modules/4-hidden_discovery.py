#!/usr/bin/python3
import marshal

# Fonction pour charger et récupérer les noms depuis un fichier .pyc
def load_pyc_names(filename):
    with open(filename, "rb") as f:
        f.read(16)  # Ignorer l'entête du fichier .pyc
        code_obj = marshal.load(f)  # Charger le code Python depuis le fichier .pyc
        return code_obj.co_names  # Récupérer tous les noms définis dans le fichier

if __name__ == "__main__":
    # Charger les noms depuis le fichier .pyc
    names = load_pyc_names("hidden_4.pyc")

    # Filtrer les noms pour ne garder que ceux qui ne commencent pas par "__"
    filtered_names = sorted(name for name in names if not name.startswith("__"))

    # Afficher les noms filtrés
    for name in filtered_names:
        print(name)
