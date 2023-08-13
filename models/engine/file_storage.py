#!/usr/bin/python3
"""Defining a class called FileStorage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    class FileStorage that serializes instances
    to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        new_obj_dict = {}
        for key, obj in self.__objects.items():
            new_obj_dict[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as JsonFile:
            json.dump(new_obj_dict, JsonFile)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path) as JsonFile:
                file_data = json.load(JsonFile)
                for key, value in file_data.items():
                    cls_name, cls_id = key.split(".")
                    obj = globals()[cls_name](**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
