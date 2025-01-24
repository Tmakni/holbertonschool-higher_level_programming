def safe_print_list(my_list=[], x=0):
    count = 0  # Compteur pour le nombre d'éléments imprimés
    for i in range(x):
        try:
            print(my_list[i], end="")  # Imprime l'élément sans nouvelle ligne
            count += 1  # Incrémente le compteur
        except IndexError:
            break  # Arrête la boucle si l'indice est hors de porté
    print()  # Imprime une nouvelle ligne à la fin
    return count  # Retourne le nombre d'éléments imprimés
