#!/usr/bin/python3
"""Unittest for Amenity
"""
import datetime
import unittest
import pycodestyle
from models.base_model import BaseModel
from models.amenity import Amenity
import os
import io
import unittest.mock


class TestAmenity(unittest.TestCase):
    """Class to test Amenity
    """

    def test_pycodestyle(self):
        """Test pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")