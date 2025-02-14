if __name__ == "__01-main.py__":
    # Créer une instance de CustomObject
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    # Sérialiser l'objet
    obj.serialize("object.pkl")

    # Désérialiser l'objet dans une nouvelle instance
    new_obj = CustomObject.deserialize("object.pkl")
    
    # Afficher l'objet désérialisé
    if new_obj:
        print("\nDeserialized Object:")
        new_obj.display()
