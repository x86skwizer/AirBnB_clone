#!/usr/bin/python3
"""
Class responsable in the creation of objects type User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Definition of class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __str__(self):
        """Representation of class User"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
