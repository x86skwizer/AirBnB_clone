#!/usr/bin/python3
"""
Parent class (called BaseModel) to take care of instances's:
-Initialization
-Serialization
-Deserialization
"""
import uuid
from datetime import datetime


class BaseModel():
    """Class BaseModel define all common attributes/methods"""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = created_at

    def __init__(self, *args, **kwargs):
        """ Constructor """
        if kwargs:
            for attr_name, attr_value in kwargs.items():
                if attr_name != "__class__":
                    if attr_name in ("created_at", "updated_at"):
                        attr_value = datetime.strptime(attr_value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, attr_name, attr_value)

        else:
            id = str(uuid.uuid4())
            created_at = datetime.now()


    def __str__(self):
        """Representation of class BaseModel"""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Update public instance attribute updated_at"""
        self.updated_at = datetime.datetime.now()

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
