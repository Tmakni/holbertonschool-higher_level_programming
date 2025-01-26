#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            # Tenter de diviser les éléments correspondants des deux listes
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            # Si une des listes est trop courte
            print("out of range")
            result = 0
        except ZeroDivisionError:
            # Si une division par zéro est tentée
            print("division by 0")
            result = 0
        except (TypeError, ValueError):
            # Si l'un des éléments n'est pas un nombre
            print("wrong type")
            result = 0
        finally:
            # Ajouter le résultat (même si c'est 0) à la liste
            result_list.append(result)
    return result_list
