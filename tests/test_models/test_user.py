#!/usr/bin/python3
"""Unittest for User
"""
import unittest
import pycodestyle
import models
from models.user import User


class TestUser(unittest.TestCase):
    """Class to test User
    """

    def test_pycodestyle(self):
        """Test pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """Creates the instance that can be used in the following tests
        """
        self.new_user = User()

    def test_TypeInstances(self):
        """Test if instances and attributes are correct type
        """
        # Check new_user is instance of User
        self.assertIsInstance(self.new_user, User)

        # check atributes are a string
        self.assertIsInstance(self.new_user.email, str)
        self.assertIsInstance(self.new_user.password, str)
        self.assertIsInstance(self.new_user.first_name, str)
        self.assertIsInstance(self.new_user.last_name, str)

    def test_InstancesAttributes(self):
        """Test if instances have correct attributes
        """
        self.assertTrue(hasattr(self.new_user, "email"))
        self.assertTrue(hasattr(self.new_user, "password"))
        self.assertTrue(hasattr(self.new_user, "first_name"))
        self.assertTrue(hasattr(self.new_user, "last_name"))

    def test_Documentation(self):
        """Test if module user has documentation
        """
        self.assertTrue(len(models.user.__doc__) > 0)
