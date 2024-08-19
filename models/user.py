#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __str__(self):
        """Representation of class User"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"