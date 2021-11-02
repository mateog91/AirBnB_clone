#!/usr/bin/python3
"""Defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime, timezone


class BaseModel:
    """Defines all common attributes/methods for other classes
    """
    def __init__(self):
        """Constructor
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        dictionary = self.__dict__
        dictionary['__class__'] = __class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
