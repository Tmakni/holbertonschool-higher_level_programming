#!/usr/bin/python3

from task_00_basic_serialization import serialize_and_save_to_file, load_and_deserialize

data = {"name": "John Doe", "age": 30, "city": "New York"}

# Sauvegarder en JSON
serialize_and_save_to_file(data, "data.json")
print("Data serialized and saved to 'data.json'.")

# Charger depuis JSON
deserialized_data = load_and_deserialize("data.json")
print("Deserialized Data:", deserialized_data)
