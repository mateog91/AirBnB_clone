#!/usr/bin/python3
"""Serializes instances to a JSON file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id

        Args:
            obj: object to add as value
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        obj_dic = {k: value.to_dict() for k, value in self.__objects.items()}
        with open(self.__file_path, mode="w") as file:
            json.dump(obj_dic, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, mode="r") as file:
                dict = json.loads(file.read())
            for key in dict.keys():
                class_name = dict[key]['__class__']
                self.new(eval(class_name)(**dict[key]))

        except FileNotFoundError:
            pass
