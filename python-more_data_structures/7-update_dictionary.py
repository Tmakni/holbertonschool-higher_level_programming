#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        for key in sorted(a_dictionary):
            print(f"{key}: {a_dictionary[key]}")
