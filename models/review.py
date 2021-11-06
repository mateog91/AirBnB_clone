#!/usr/bin/python3
"""Subclass Review that inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Subclass amenity that inherits from BaseModel

    Args:
        BaseModel (superclass): Defines all common
        attributes/methods for other classes

    Description:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
