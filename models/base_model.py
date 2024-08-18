#!/usr/bin/python3
"""
Parent class (called BaseModel) to take care of instances's:
-Initialization
-Serialization
-Deserialization
"""
from datetime import datetime
import uuid


class BaseModel():
	def __init__(self, *args, **kwargs):
		"""Initialize a new BaseModel instance.
        
        If kwargs is not empty, this method will initialize an instance based
        on the dictionary of attributes passed in kwargs. Otherwise, it will
        generate a new instance with a unique id, and current datetime for
        `created_at` and `updated_at`.
        """
		if kwargs:
			for key, value in kwargs.items():
				if key == 'created_at' or key == 'updated_at':
					value = datetime.fromisoformat(value)
				if key != '__class__':
					setattr(self, key, value)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = self.created_at

	def __str__(self):
		"""Return a string representation of the instance."""
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

	def save(self):
		"""Update the public instance attribute updated_at with the current datetime."""
		self.updated_at = datetime.now()

	def to_dict(self):
		"""Return a dictionary containing all keys/values of __dict__ of the instance."""
		dict_representation = self.__dict__.copy()
		dict_representation['__class__'] = self.__class__.__name__
		dict_representation['created_at'] = self.created_at.isoformat()
		dict_representation['updated_at'] = self.updated_at.isoformat()
		return dict_representation