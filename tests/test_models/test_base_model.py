#!/usr/bin/python3
"""Unittest for Base Model
"""
import datetime
import unittest
import pycodestyle
import models
from models.base_model import BaseModel
import os
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

    def test_Documentation(self):
        """Test if module BaseModel has documentation
        """
        self.assertTrue(len(models.base_model.__doc__) > 0)

    def setUp(self):
        """Creates the instance that can be used in the following tests
        """
        self.b = BaseModel()

    def test_unique_id(self):
        """Test if id of an instance is unique
        """
        b2 = BaseModel()
        self.assertNotEqual(self.b.id, b2.id)

    def test_TypeInstances(self):
        """Test if instances and attributes are correct type
        """
        # Check b is instance of BaseModel
        self.assertIsInstance(self.b, BaseModel)

        # check id is a string
        self.assertIsInstance(self.b.id, str)
        # Check create_at and update_at are strings
        self.assertIsInstance(self.b.created_at, datetime.datetime)
        self.assertIsInstance(self.b.updated_at, datetime.datetime)

    def test_InstancesAttributes(self):
        """Test if instances have correct attributes
        """
        self.assertTrue(hasattr(self.b, "id"))
        self.assertTrue(hasattr(self.b, "created_at"))
        self.assertTrue(hasattr(self.b, "updated_at"))

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
        update_1 = my_model.updated_at
        my_model.save()
        update_2 = my_model.updated_at
        self.assertNotEqual(update_1, update_2)
        output = "[{}] ({}) {}".format(my_model.__class__.__name__,
                                       my_model.id, my_model.__dict__)

        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            print(my_model, end="")
            self.assertEqual(_out.getvalue(), output)
        # since it was updated, create at must not be equal to update at
        self.assertNotEqual(my_model.created_at, my_model.updated_at)
        path = os.getcwd()
        file_name_expected = 'file.json'
        try:
            os.remove(path + "/" + file_name_expected)
        except FileNotFoundError:
            pass

    def test_save_FileStorage(self):
        """Test save method for json file
        """
        path = os.getcwd()
        file_name_expected = 'file.json'
        try:
            os.remove(path + "/" + file_name_expected)
        except FileNotFoundError:
            pass
        my_model = BaseModel()
        my_model.save()
        key = f"{my_model.__class__.__name__}.{my_model.id}"
        with open(file_name_expected, mode="r") as file:
            output = file.read()
        dict_json = eval(output)
        json_keys = dict_json.keys()
        self.assertIn(key, json_keys)
        self.assertEqual(my_model.to_dict(), dict_json[key])
        os.remove(path + "/" + file_name_expected)

    def test_to_dict_NoArguments(self):
        """Tests to dict method without arguments passed
        """
        # creating instance for testing
        my_model = BaseModel()
        my_model.name = "My First Model"
        # calling to_dict method to test it
        my_model_json = my_model.to_dict()
        # Testing if all steps of to_dict method did their job correctly
        self.assertIn('__class__', my_model_json)
        self.assertNotIn('__class__', my_model.__dict__)
        self.assertEqual(my_model.__class__.__name__,
                         my_model_json['__class__'])
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)
        self.assertIsInstance(my_model_json, dict)

    def test_to_dict_emptyDict(self):
        """Tests to dict method empty dict passed
        """
        # creating instance for testing
        my_model = BaseModel({})
        my_model.name = "My First Model"
        # calling to_dict method to test it
        my_model_json = my_model.to_dict()
        # Testing if all steps of to_dict method did their job correctly
        self.assertIn('__class__', my_model_json)
        self.assertNotIn('__class__', my_model.__dict__)
        self.assertEqual(my_model.__class__.__name__,
                         my_model_json['__class__'])
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)
        self.assertIsInstance(my_model_json, dict)

    def test_to_dict_None(self):
        """Tests to dict method None passed
        """
        # creating instance for testing
        my_model = BaseModel(None)
        my_model.name = "My First Model"
        # calling to_dict method to test it
        my_model_json = my_model.to_dict()
        # Testing if all steps of to_dict method did their job correctly
        self.assertIn('__class__', my_model_json)
        self.assertNotIn('__class__', my_model.__dict__)
        self.assertEqual(my_model.__class__.__name__,
                         my_model_json['__class__'])
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)
        self.assertIsInstance(my_model_json, dict)

    def test_create_from_dict(self):
        """Test cases when creating an object from a
            a dictionary representation (**kwargs)
        """
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)

        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(
            my_new_model.__class__.__name__, BaseModel.__name__)
        self.assertEqual(
            my_new_model.__class__.__name__, my_model.__class__.__name__)
        self.assertEqual(my_model.__dict__, my_new_model.__dict__)
