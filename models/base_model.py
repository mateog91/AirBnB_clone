#!/usr/bin/python3
"""Defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods for other classes

    Attributes:
        id: string - unique id for each BaseModel, it will be assigned
        with an uuid when an instance is created
        created_at: datetime - assigned with the current datetime when
        an instance is created
        updated_at: datetime - assigned with the current datetime when an
        instance is created and it will be updated every time you change your
        object
    Methods:
        __str__: should print: [<class name>] (<self.id>) <self.__dict__>
        save(self): updates the public instance attribute updated_at with
        the current datetime
        to_dict(self): returns a dictionary containing all keys/values of
        __dict__ of the instance
    """

    def __init__(self, *args, **kwargs):
        """Constructor
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Returns [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        dictionary = dict(self.__dict__)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
