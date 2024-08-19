#!/usr/bin/python3
import json, os


class FileStorage():
	__file_path = "file.json"
	__objects = {}

	def all(self):
		"""Returns the dictionary __objects."""
		return self.__objects
	
	def new(self, obj):
		"""Sets in __objects the obj with key <obj class name>.id."""
		key = f"{obj.__class__.__name__}.{obj.id}"
		self.__objects[key] = obj

	def save(self):
		"""Serializes __objects to the JSON file (path: __file_path)."""
		tmp = {}
		with open( self.__file_path , "w" ) as write_file:
			tmp = {key: value.to_dict() for key,value in self.__objects.items()}
			json.dump(tmp, write_file)
	
	def reload(self):
		"""Deserializes the JSON file to __objects, if it exists."""
		try:
			with open( self.__file_path , "r" ) as read_file:
				from models.base_model import BaseModel
				self.__objects = {key: BaseModel(**value) for key, value in json.load(read_file).items()}
		except:
			pass
