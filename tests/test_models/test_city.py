#!/usr/bin/python3
"""Unittest for City
"""
import datetime
import unittest
import pycodestyle
from models.base_model import BaseModel
from models.city import City
import os
import io
import unittest.mock


class TestCity(unittest.TestCase):
    """Class to test City
    """

    def test_pycodestyle(self):
        """Test pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")