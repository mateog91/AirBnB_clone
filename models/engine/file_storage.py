#!/usr/bin/python3
"""Serializes instances to a JSON file and deserializes JSON file to instances
"""


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
            obj ([type]): [description]
        """

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
