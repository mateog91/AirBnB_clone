#!/usr/bin/python3
"""Unittest for Review
"""
import datetime
import unittest
import pycodestyle
from models.base_model import BaseModel
from models.review import Review
import os
import io
import unittest.mock


class TestReview(unittest.TestCase):
    """Class to test Review
    """

    def test_pycodestyle(self):
        """Test pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")