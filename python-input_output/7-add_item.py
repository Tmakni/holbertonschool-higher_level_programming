#!/usr/bin/python3

"""
fonction
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":

    try:
        items = load_from_json_file("add_item.json")
    except Exception:
        mylist = []
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        mylist.append(sys.argv[i])
save_to_json_file(mylist, filename)
