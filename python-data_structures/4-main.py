#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list[idx] = element


new_list = [1, 2, 3, 9, 5]
print(new_list)

new_in_list(new_list, 3, 4)
print(new_list)
