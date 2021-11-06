#!/usr/bin/python3
"""Unittest for State
"""
import datetime
import unittest
import pycodestyle
from models.base_model import BaseModel
from models.state import State
import os
import io
import unittest.mock


class TestState(unittest.TestCase):
    """Class to test State
    """

    def test_pycodestyle(self):
        """Test pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")