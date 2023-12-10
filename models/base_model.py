#!/usr/bin/python3
"""
This is BaseModel class tha define common
attributes/methods for other classes
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    class BaseModel that defines all common attributes/methods
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """ Constructor function"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, val in kwargs.items():
                if key == "__class__":
                    continue
                formatdate = "%Y-%m-%dT%H:%M:%S.%f"
                if key == "created_at" or key == "created_at":
                    """sets the value of the attribute of an object"""
                    setattr(self, key, datetime.strptime(val, formatdate))
                else:
                    setattr(self, key, val)
        else:
            """Add the new instance to the FileStorage"""
            models.storage.new(self)

    def __str__(self):
        """
        String representation of BaseModel instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance attribute
        updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        """To save the objects to the JSON
        file using FileStore module"""
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
