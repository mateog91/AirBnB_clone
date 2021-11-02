#!/usr/bin/python3
"""Unittest for Base Model
"""
import datetime
import unittest
import pycodestyle
from models.base_model import BaseModel
import sys
import io
import unittest.mock


class TestBaseModel(unittest.TestCase):
    """Class to test Base Model
    """

    def test_pycodestyle(self):
        """Test pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        self.b = BaseModel()

    def test_Instances(self):
        """Test if instances and attributes are correct type
        """
        # Check b is instance of BaseModel
        self.assertIsInstance(self.b, BaseModel)

        # check id is a string
        self.assertIsInstance(self.b.id, str)
        # Check create_at and update_at are strings
        self.assertIsInstance(self.b.created_at, datetime.datetime)
        self.assertIsInstance(self.b.updated_at, datetime.datetime)

    def test_str_method(self):
        """Test __str__ method correct printing
        """
        my_model = BaseModel()
        output = "[{}] ({}) {}".format(my_model.__class__.__name__,
                                       my_model.id, my_model.__dict__)

        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            print(my_model, end="")
            self.assertEqual(_out.getvalue(), output)

    def test_save_method(self):
        """Test save method correct printing
        """
        my_model = BaseModel()
        my_model.save()
        output = "[{}] ({}) {}".format(my_model.__class__.__name__,
                                       my_model.id, my_model.__dict__)

        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            print(my_model, end="")
            self.assertEqual(_out.getvalue(), output)
        # since it was updated, create at must not be equal to update at
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_to_dict(self):
        """Tests to dict method
        """
        # creating instance for testing
        my_model = BaseModel()
        my_model.name = "My First Model"
        # calling to_dict method to test it
        my_model_json = my_model.to_dict()
        dictionary = my_model.__dict__
        # Test if they are the same
        self.assertEqual(my_model_json, dictionary)
        # Testing if all steps of to_dict method did their job correctly
        self.assertIn('__class__', my_model_json)
        self.assertEqual(my_model.__class__.__name__,
                         my_model_json['__class__'])
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)
        self.assertIsInstance(my_model_json, dict)