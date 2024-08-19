#!/usr/bin/python3
"""
Parent class (called BaseModel) to take care of instances's:
-Initialization
-Serialization
-Deserialization
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """Class BaseModel define all common attributes/methods"""

    def __init__(self, *args, **kwargs):
        """ Constructor """
        if kwargs and kwargs != {}:
            for key, vle in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at", ):
                        vle = datetime.strptime(vle, "%Y-%m-%dT%H:%M:%S.%f")
                    self.__dict__[key] = vle

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Representation of class BaseModel"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update public instance attribute updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionnary of __dict__ of the instance"""
        iso_created_at = self.created_at.isoformat()
        iso_updated_at = self.updated_at.isoformat()
        class_name = self.__class__.__name__
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = class_name
        instance_dict['created_at'] = iso_created_at
        instance_dict['updated_at'] = iso_updated_at
        return instance_dict