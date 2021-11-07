#!/usr/bin/python3
"""Test Module for File Storage
"""
import pycodestyle
import unittest
import models
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """Class to test File Storage
    """

    def test_pycodestyle(self):
        """Test pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_Documentation(self):
        """Test if module file_storage has documentation
        """
        self.assertTrue(len(models.engine.file_storage.__doc__) > 0)

    def test_type_field(self):
        """Test type of field
        """
        object = FileStorage()
        self.assertIsInstance(object, FileStorage)
        self.assertIsInstance(object.all(), dict)
        self.assertIsInstance(object._FileStorage__file_path, str)
        self.assertIsInstance(object._FileStorage__objects, dict)

    def test_all(self):
        """Test all method
        """
        object = BaseModel()
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIsInstance(storage.all(), dict)
        key_object = f"{object.__class__.__name__}.{object.id}"
        self.assertEqual(all_objs[key_object], object)

    def test_new(self):
        """Test new method
        """
        object = BaseModel()
        storage.new(object)
        dict_objects = storage.all()

        # Testing if key was set correctly and in __objects
        key = f"{object.__class__.__name__}.{object.id}"
        keys_dict = dict_objects.keys()
        self.assertIn(key, keys_dict)

        # Testing if value was correctly added to __objects
        self.assertEqual(dict_objects[key], object)

    def test_save(self):
        """Test for save method
        """
        path = os.getcwd()
        file_name_expected = 'file.json'
        try:
            os.remove(path + "/" + file_name_expected)
        except FileNotFoundError:
            pass

        my_model = BaseModel()
        my_model.save()

        dummy_dict = my_model.to_dict()
        dummy_key = f"{my_model.__class__.__name__}.{my_model.id}"

        self.assertTrue(os.path.isfile(path + "/" + file_name_expected))
        with open(file_name_expected, mode="r") as file:
            output = file.read()
        dict_json = eval(output)
        keys = dict_json.keys()
        self.assertIn(dummy_key, keys)
        self.assertEqual(dummy_dict, dict_json[dummy_key])
        os.remove(path + "/" + file_name_expected)

    def test_reload(self):
        """Test Reload Method
        """
        path = os.getcwd()
        file_name_expected = 'file.json'
        try:
            os.remove(path + "/" + file_name_expected)
        except FileNotFoundError:
            pass

        json_string = {"BaseModel.e79e744a": {"__class__": "BaseModel",
            "id": "e79e744a", "updated_at": "2017-09-28T21:08:06.151750",
                "created_at": "2017-09-28T21:08:06.151711",
                    "name": "My_First_Model", "my_number": 89}}
        expected_dictionary = {"BaseModel.e79e744a":
                               {"__class__": "BaseModel", "id": "e79e744a",
                                "updated_at": "2017-09-28T21:08:06.151750",
                                "created_at": "2017-09-28T21:08:06.151711",
                                "name": "My_First_Model", "my_number": 89}}
        with open('file.json', mode="w") as file:
            json.dump(json_string, file)

        storage.reload()
        dictionary_reload = storage.all()
        key_expected = "BaseModel.e79e744a"
        self.assertIn(key_expected, dictionary_reload.keys())
        self.assertEqual(
            dictionary_reload[key_expected].name,
            expected_dictionary[key_expected]["name"])
        os.remove(path + "/" + file_name_expected)
