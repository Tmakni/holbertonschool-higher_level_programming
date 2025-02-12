#!/usr/bin/python3

"""
fonction
"""

import json


def save_to_json_file(my_obj, filename):
    """
    fonction
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
