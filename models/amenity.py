#!/usr/bin/python3
"""Subclass Amenity that inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Subclass amenity that inherits from BaseModel

    Args:
        BaseModel (superclass): Defines all common
        attributes/methods for other classes

    Description:
        name: string - empty string
    """
    name = ""
