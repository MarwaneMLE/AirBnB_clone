#!/usr/bin/python3
"""Defines unittests for models/amenity.py"""

import os
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    """Unittests for Amenity class."""

    def setUp(self):
        # Backup the existing file.json
        os.rename("file.json", "tmp")

    def tearDown(self):
        # Restore the original file.json
        os.remove("file.json")
        os.rename("tmp", "file.json")

    def test_instantiation(self):
        """Test Amenity instantiation."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIn(amenity, storage.all().values())
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertIsInstance(Amenity.name, str)
        self.assertNotIn("name", amenity.__dict__)

    def test_attributes(self):
        """Test Amenity attributes."""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)
        self.assertLess(amenity1.created_at, amenity2.created_at)
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_str_representation(self):
        """Test Amenity string representation."""
        dt = datetime.today()
        amenity = Amenity()
        amenity.id = "123456"
        amenity.created_at = amenity.updated_at = dt
        dt_repr = repr(dt)
        amenity_str = str(amenity)
        self.assertIn("[Amenity] (123456)", amenity_str)
        self.assertIn("'id': '123456'", amenity_str)
        self.assertIn("'created_at': " + dt_repr, amenity_str)
        self.assertIn("'updated_at': " + dt_repr, amenity_str)

    def test_instantiation_with_kwargs(self):
        """Test Amenity instantiation with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        amenity = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amenity.id, "345")
        self.assertEqual(amenity.created_at, dt)
        self.assertEqual(amenity.updated_at, dt)

    def test_save_method(self):
        """Test Amenity save method."""
        amenity = Amenity()
        first_updated_at = amenity.updated_at
        sleep(0.05)
        amenity.save()
        self.assertLess(first_updated_at, amenity.updated_at)
        amid = "Amenity." + amenity.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())

    def test_to_dict_method(self):
        """Test Amenity to_dict method."""
        dt = datetime.today()
        amenity = Amenity()
        amenity.id = "123456"
        amenity.created_at = amenity.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(amenity.to_dict(), tdict)


if __name__ == "__main__":
    unittest.main()

