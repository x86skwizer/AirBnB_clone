#!/usr/bin/python3
"""
Class responsable in the creation of objects type Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Definition of class Review"""
    place_id = ""
    user_id = ""
    text = ""

    def __str__(self):
        """Representation of class Review"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
