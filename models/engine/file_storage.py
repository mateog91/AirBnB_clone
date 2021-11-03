#!/usr/bin/python3
"""Serializes instances to a JSON file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
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
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id

        Args:
            obj: object to add as value
        """
        key = "{}.{}".format(self.__class__.__name__, self.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        object_dic = {key: value.to_dict for key, value in FileStorage.__objects}
        with open(FileStorage.__file_path, mode="w") as file:
            json.dump(object_dic, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, mode="r") as file:
                dict = json.loads(file.read())
            for key, value in dict.items():
                if key in ['created_at', 'updated_at']:
                        setattr(dict, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(dict, key, value)
                
        except FileNotFoundError:
            pass
