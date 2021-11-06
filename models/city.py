#!/usr/bin/python3
"""Subclass City that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Subclass City that inherits from BaseModel

    Args:
        BaseModel (superclass): Defines all common
        attributes/methods for other classes

    Description:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""
