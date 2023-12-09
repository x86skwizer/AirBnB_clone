#!/usr/bin/python3
"""
Class responsable in the creation of objects type State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Definition of class State"""
    name = ""

    def __str__(self):
        """Representation of class State"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
