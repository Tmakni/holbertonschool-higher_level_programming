#!/usr/bin/python3
"""
Serialisation
"""


from task_01_pickle import CustomObject

obj = CustomObject(name="John", age=25, is_student=True)
print("Objet original :")
obj.display()

obj.serialize("object.pkl")

new_obj = CustomObject.deserialize("object.pkl")
print("\nObjet désérialisé :")
if new_obj:
    new_obj.display()
else:
    print("Erreur lors de la désérialisation.")
