#!/usr/bin/python3
"""Classs to test BaseModel"""
import unittest
from models.base_model import BaseModel 
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """ Test of BaseModel class"""
    def setUp(self):
        """This method is called before each test is executed"""
        self.base_model = BaseModel()

    def test_attributes(self):
        """Test if the attributes are set correctly upon instantiation"""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_str(self):
        """Test the __str__ method"""
        expected_str = f"[{self.base_model.__class__.__name__}] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_updates(self):
        """Test if the save method updates the updated_at attribute"""
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        """ Test the to_dict method"""
        obj_dict = self.base_model.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)


    def test_from_dict(self):
        """Test if an instance can be created from a dictionary representation"""
        data = {
            "id": "instance_id",
            "created_at": "2023-12-09T18:01:04.905657",
            "updated_at": "2023-12-09T18:10:04.905657"
        }

        new_instance = BaseModel(**data)
        self.assertEqual(new_instance.id, "instance_id")
        self.assertEqual(new_instance.created_at.isoformat(), "2023-12-09T18:01:04.905657")
        self.assertEqual(new_instance.updated_at, "2023-12-09T18:10:04.905657")


if __name__ == '__main__':
    unittest.main()

