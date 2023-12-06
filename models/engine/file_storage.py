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
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open( self.__file_path , "w" ) as write_file:
            json.dump(self.__objects, write_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open( self.__file_path , "r" ) as read_file:
                self.__objects = json.loads(read_file)
        except:
            pass
