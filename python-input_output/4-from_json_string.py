#!/usr/bin/python3
"""json import"""


import json


def from_json_string(my_str):
    """
    converti une chaine json et obj
    """
    return json.loads(my_str)
