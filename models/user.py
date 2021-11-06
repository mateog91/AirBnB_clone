#!/usr/bin/python3
"""Subclass User that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Subclass User that inherits from BaseModel

    Args:
        BaseModel (superclass): Defines all common
        attributes/methods for other classes
    Description:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
