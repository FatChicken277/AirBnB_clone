#!/usr/bin/python3
"""Module for the file storage engine
"""
import json


class FileStorage:
    """Class FileStorage, is the engine to store
    """
    __file_path = "file.json"
    __objects = {}

    def __models(self):
        """This class is used to store the avaliable models while avoiding
circular importation

        Returns:
            dict: The dictionary of models - objects k - v combination
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.state import State

        models = {"BaseModel": BaseModel, "User": User,
                  "City": City, "Amenity": Amenity,
                  "Place": Place, "Review": Review,
                  "State": State}
        return models

    def all(self):
        """Getter for __objects

        Returns:
            dict: THe dictionary of objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """THis function creates a new entry in the object

        Args:
            obj (object): This makes a new object entry
        """
        FileStorage.__objects["{}.{}"
                              .format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Saves to a json file
        """
        fili = FileStorage.__objects
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in fili.items()}, f)

    def reload(self):
        """This reloads from a json file (if there's none or empty doesn't
do anything)
        """
        try:
            patty = FileStorage.__file_path
            with open(patty, mode="r", encoding="utf-8") as file:
                val = json.load(file)
                val = {k: self.__models()[v["__class__"]](**v)
                       for k, v in val.items()}
                FileStorage.__objects = val
        except Exception:
            pass
