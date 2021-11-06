#!/usr/bin/python3
"""Unittest for Place
"""
import datetime
import unittest
import pycodestyle
from models.base_model import BaseModel
from models.place import Place
import os
import io
import unittest.mock


class TestPlace(unittest.TestCase):
    """Class to test Place
    """

    def test_pycodestyle(self):
        """Test pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")