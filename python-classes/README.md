readme

| Terme / Syntaxe                            | Signification / Utilisation                                                                                                |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| `import unittest`                          | Module Python standard pour écrire et lancer des tests unitaires automatiques.                                             |
| `__` (double underscore) avant un attribut | Indique un attribut privé (name mangling) : protection légère pour éviter l’accès direct.                                  |
| `self`                                     | Représente l’instance (objet) courant dans une méthode de classe. Permet d’accéder aux attributs et méthodes de cet objet. |
| `def`                                      | Mot-clé pour **définir une fonction** ou une méthode dans une classe.                                                      |
| `__init__`                                 | Méthode spéciale appelée automatiquement lors de la création d’un objet pour l’initialiser.                                |
| `self.__size = size`                       | Stocke la valeur `size` dans un attribut privé `__size` de l’objet courant.                                                |
| `my_object = ClassName(params)`            | Création d’une instance (objet) de la classe `ClassName`, appelant automatiquement `__init__` avec les paramètres fournis. |
| `my_object.__dict__`                       | Dictionnaire interne d’un objet qui montre ses attributs et leurs valeurs.                                                 |

isinstance(size, int)
Qu’est-ce que isinstance ?
 C’est une fonction intégrée de Python qui sert à vérifier le type d’un objet.
raise est utilisé pour lancer une exception (une erreur contrôlée).
