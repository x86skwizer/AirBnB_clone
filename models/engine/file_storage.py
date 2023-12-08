#!/usr/bin/python3
"""
File contains a class FileStorage that serializes instances 
to a JSON file and deserializes JSON file to instances
"""
import json

class FileStorage():
    """Class serialize instances to JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        tmp = {}
        with open( self.__file_path , "w" ) as write_file:
            tmp = {key: value.to_dict()
                for key,value in self.__objects.items()}
            json.dump(tmp, write_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open( self.__file_path , "r" ) as read_file:
                from models.base_model import BaseModel
                from models.user import User
                class_mapping = {
                    "BaseModel": BaseModel,
                    "User": User
                }
                json_data = json.load(read_file)
                self.__objects = { key: class_mapping[value['__class__']](**value)
                    for key, value in json_data.items() }
        except (FileNotFoundError):
            pass


