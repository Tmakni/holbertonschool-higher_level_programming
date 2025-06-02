import json

def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8")as file:
        my_obj = json.dumps(my_obj)
        return my_obj
