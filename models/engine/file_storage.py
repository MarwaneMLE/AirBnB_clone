#!/usr/bin/python3
"""
Module that contains the FileStore class
"""

from base_model import BaseModel
import json
from json import JSONDecodeError


class FileStorage():
    """
    FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    
    def __init__(self):
        pass

    def all(self):
        """ Return the dictionary """
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objects = {} 
        for key, val in FileStorage.__objects.items():
            serialized_objects[key] = val.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for key, val in data.items():
                    class_name, obj_id = key.split(".")
                    class_obj = globals()[class_name]
                    instance = class_obj(**val)
                    FileStorage.__objects[key] = instance
        except (FileNotFoundError, JSONDecodeError):
            pass
