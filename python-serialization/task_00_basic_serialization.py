#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    with open(filename "w") as file:
        json.dump(data)
    pass
