#!/usr/bin/python3
"""Unit tests for place class"""

import unittest
from models.place import Place
from datetime import datetime
import os


class Test_Place_Init(unittest.TestCase):
    """tests for Place's init"""

    def setUp(self):
        """Set up test environment for each test case"""
        self.place = Place()

    def tearDown(self):
        """Clean up test environment after each test case"""
        del self.place

    def test_Place_no_arg(self):
        """Initialize a Place with no args"""
        self.place = Place()
        self.assertTrue(self.place.created_at)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertTrue(self.place.updated_at)
        self.assertIsInstance(self.place.updated_at, datetime)
        self.assertTrue(self.place.id)
        self.assertIsInstance(self.place.id, str)

    def test_Place_with_kwargs(self):
        """Initialize a Place with kwargs"""
        kwargs = {"created_at": "2023-08-11T12:00:00",
                  "updated_at": "2023-08-11T12:30:00",
                  "id": "fd8a62d4-b954-4611-944f-2bb0a49242db"}

        self.place = Place(**kwargs)
        self.assertEqual(self.place.created_at, datetime(2023, 8, 11, 12, 0))
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertEqual(self.place.created_at, datetime(2023, 8, 11, 12, 0))
        self.assertIsInstance(self.place.updated_at, datetime)
        self.assertIsInstance(self.place.id, str)
        self.assertEqual(self.place.id, "fd8a62d4-b954-4611-944f-2bb0a49242db")

    def test_Place_attributes(self):
        """tests the attributes for class place"""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_Place_attributes_default_values(self):
        """test the default values of attributes"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_Place_kwargs_None(self):
        """Initialize a Place with None as kwargs"""
        with self.assertRaises(TypeError):
            p = Place(id=None, created_at=None, updated_at=None)


class Test_Place__str__(unittest.TestCase):
    """Test __str__ method of Place"""

    def test_Place_str_representation(self):
        """string representation of Place"""
        p = Place(id='test_id',
                  created_at="2017-09-28T21:05:54.119427",
                  updated_at="2017-09-28T21:05:54.119572")
        expected_str = ("[Place] (test_id) {'id': 'test_id', "
                        "'created_at': datetime.datetime"
                        "(2017, 9, 28, 21, 5, 54, 119427), "
                        "'updated_at': datetime.datetime"
                        "(2017, 9, 28, 21, 5, 54, 119572)}")
        self.assertEqual(str(p), expected_str)


class Test_Place_save(unittest.TestCase):
    """Tests for the __str__ method of Place"""

    def test_Place_updated_at_save(self):
        """test Place's updated_at with the save method"""
        p = Place()
        updated_at_1 = p.updated_at
        p.save()
        updated_at_2 = p.updated_at
        self.assertLess(updated_at_1, updated_at_2)

    def test_Place_updated_at_two_saves(self):
        """test Place's updated_at two saves with the save method"""
        p = Place()
        updated_at_1 = p.updated_at
        p.save()
        updated_at_2 = p.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        p.save()
        updated_at_3 = p.updated_at
        self.assertLess(updated_at_2, updated_at_3)

    def test_Place_save_saves_to_files(self):
        """test Place's save method with saving to and updating a file"""
        p = Place()
        p.save()
        p_id = "Place." + p.id
        with open("file.json") as JsonFile:
            self.assertIn(p_id, JsonFile.read())


class Test_Place_to_dict(unittest.TestCase):
    """Tests for the to_dict method of Place"""

    def test_Place_to_dict_original_attr(self):
        """test Place's to_dict method without adding attributes"""
        p = Place(id='test_id',
                  created_at="2017-09-28T21:05:54.119427",
                  updated_at="2017-09-28T21:05:54.119572")
        p_dictionary = p.to_dict()
        expected_dict = {"__class__": Place.__name__, "id": "test_id",
                         "created_at": "2017-09-28T21:05:54.119427",
                         "updated_at": "2017-09-28T21:05:54.119572"}
        self.assertEqual(p_dictionary, expected_dict)

    def test_Place_dict_new_attr(self):
        """test Place's to_dict method with added new attributes"""
        p = Place(id='test_id',
                  created_at="2017-09-28T21:05:54.119427",
                  updated_at="2017-09-28T21:05:54.119572")
        p.name = "adxel"
        p.age = 25
        p_dictionary = p.to_dict()
        expected_dict = {"__class__": Place.__name__, "id": "test_id",
                         "created_at": "2017-09-28T21:05:54.119427",
                         "updated_at": "2017-09-28T21:05:54.119572",
                         "name": "adxel", "age": 25}
        self.assertEqual(p_dictionary, expected_dict)


if __name__ == "__main__":
    unittest.main()
