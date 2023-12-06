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
        return __objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        key = obj.__class__.name + "." + obj.id
        __objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open( __file_path , "w" ) as write:
            json.dump(__objects, write)
