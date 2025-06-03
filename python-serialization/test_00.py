from task_00_basic_serialization import serialize_and_save_to_file, load_and_deserialize

data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

filename = "data.json"

serialize_and_save_to_file(data_to_serialize, filename)
print("Données enregistrées dans", filename)

deserialized_data = load_and_deserialize(filename)
print("Données récupérées :", deserialized_data)
