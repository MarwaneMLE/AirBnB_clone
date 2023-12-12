#!/usr/bin/python3

'''import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """ Test of User class"""
    def setUp(self):
        """This method is called before each test is executed"""
        self.user = User()

        """user = User()
        #self.assertEqual(self.)"""
        '''


import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test User class"""
    def setUp(self):
        """This method is called before each test"""
        self.user = User()

    def test_inheritance(self):
        """Test if User inherits from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Test if attributes are present
        and set to default values
        """
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertEqual(self.user.email, "")
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertEqual(self.user.password, "")
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertEqual(self.user.first_name, "")
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.last_name, "")

    def test_str_method(self):
        """Test the __str__ method"""
        user_clss = self.user.__class__.__name__
        expected_str = f"[{user_clss}] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), expected_str)

    def test_save_method_updates_updated_at(self):
        """Test if the save method updates the updated_at attribute"""
        previous_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(previous_updated_at, self.user.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        obj_dict = self.user.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'User')
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('email', obj_dict)
        self.assertIn('password', obj_dict)
        self.assertIn('first_name', obj_dict)
        self.assertIn('last_name', obj_dict)

    def test_init_from_dict(self):
        """Test if an instance can be created
        from a dictionary representation
        """
        data = {
            'id': 'some_id',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-02T15:30:00.000000',
            'email': 'test@example.com',
            'password': 'secure_password',
            'first_name': 'John',
            'last_name': 'Doe',
            # ... other attributes ...
        }
        new_instance = User(**data)
        self.assertEqual(new_instance.id, 'some_id')
        self.assertEqual(new_instance.email, 'test@example.com')
        self.assertEqual(new_instance.password, 'secure_password')
        self.assertEqual(new_instance.first_name, 'John')
        self.assertEqual(new_instance.last_name, 'Doe')


if __name__ == '__main__':
    unittest.main()
