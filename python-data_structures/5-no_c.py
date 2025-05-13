#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for lettre in my_string:
        if lettre != 'c' and lettre != 'C':
            new_string.append(lettre)
    return ''.join(new_string)
