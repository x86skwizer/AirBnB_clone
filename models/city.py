#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    name = ""

    def __str__(self):
        """Representation of class User"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
