#!/usr/bin/python3
"""
Class responsable in the creation of objects type amenity
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Definition of class City"""
    state_id = ""
    name = ""

    def __str__(self):
        """Representation of class City"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
