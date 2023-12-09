#!/usr/bin/python3
"""
Class responsable in the creation of objects type amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Definition of class Amenity"""
    name = ""

    def __str__(self):
        """Representation of class Amenity"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
