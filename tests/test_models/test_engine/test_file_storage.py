#!/usr/bin/python3
"""Test Module for File Storage
"""
import pycodestyle
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Class to test File Storage
    """
    def test_pycodestyle(self):
        """Test pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def type_field(self):
        """Test type of field
        """
        object = FileStorage()
        self.assertEqual(type(object), FileStorage)
        self.assertEqual(type(object.__file_path, str))
        self.assertEqual(type(object.__objects, dict))

    def test_all(self):
        """Test all method
        """
        object = FileStorage()
        all_objs = object.all()
        self.assertEqual(dict, type(all_objs))
    
    def test_new(self):
        """Test new method
        """
        object = 
        
        for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        print(my_model)
