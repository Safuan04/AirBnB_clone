#!/usr/bin/python3
"""Defining a class called BaseModel"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel of the AirBnB Project"""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance for the BaseModel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        value = datetime.fromisoformat(value)
                    if key == "updated_at":
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            models.storage.new(self)

    def __str__(self):
        """string representation of BaseModel's instances"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/vales of the instance"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
