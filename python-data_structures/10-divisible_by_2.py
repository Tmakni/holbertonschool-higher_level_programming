#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    resultats = []
    for number in my_list:
        if number % 2 == 0:
            resultats.append(True)
        else:
            resultats.append(False)
    return resultats
