#!/usr/bin/python3
"""Unit tests for city class"""

import unittest
from models.city import City
from datetime import datetime
import os


class Test_City_Init(unittest.TestCase):
    """tests for City's init"""

    def setUp(self):
        """Set up test environment for each test case"""
        self.city = City()

    def tearDown(self):
        """Clean up test environment atfer each test case"""
        del self.city

    def test_City_no_arg(self):
        """Initialize a City with no args"""
        self.city = City()
        self.assertTrue(self.city.created_at)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertTrue(self.city.updated_at)
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertTrue(self.city.id)
        self.assertIsInstance(self.city.id, str)

    def test_City_with_kwargs(self):
        """Initialize a City with kwargs"""
        kwargs = {"created_at": "2023-08-11T12:00:00",
                  "updated_at": "2023-08-11T12:30:00",
                  "id": "fd8a62d4-b954-4611-944f-2bb0a49242db"}

        self.city = City(**kwargs)
        self.assertEqual(self.city.created_at, datetime(2023, 8, 11, 12, 0))
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertEqual(self.city.created_at, datetime(2023, 8, 11, 12, 0))
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertIsInstance(self.city.id, str)
        self.assertEqual(self.city.id, "fd8a62d4-b954-4611-944f-2bb0a49242db")

    def test_City_kwargs_None(self):
        """Initialize a City with None as kwargs"""
        with self.assertRaises(TypeError):
            c = City(id=None, created_at=None, updated_at=None)

    def test_City_attributes(self):
        """tests the attributes for class city"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_City_attributes_default_values(self):
        """test the default values of attributes"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_City_str_representation(self):
        """string representation of City"""
        c = City(id='test_id',
                 created_at="2017-09-28T21:05:54.119427",
                 updated_at="2017-09-28T21:05:54.119572")
        expected_str = ("[City] (test_id) {'id': 'test_id', "
                        "'created_at': datetime.datetime"
                        "(2017, 9, 28, 21, 5, 54, 119427), "
                        "'updated_at': datetime.datetime"
                        "(2017, 9, 28, 21, 5, 54, 119572)}")
        self.assertEqual(str(c), expected_str)

    def test_City_updated_at_save(self):
        """test City's updated_at with the save method"""
        c = City()
        updated_at_1 = c.updated_at
        c.save()
        updated_at_2 = c.updated_at
        self.assertLess(updated_at_1, updated_at_2)

    def test_City_updated_at_two_saves(self):
        """test City's updated_at two saves with the save method"""
        c = City()
        updated_at_1 = c.updated_at
        c.save()
        updated_at_2 = c.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        c.save()
        updated_at_3 = c.updated_at
        self.assertLess(updated_at_2, updated_at_3)

    def test_City_save_saves_to_files(self):
        """test City's save method with saving to and updating a file"""
        c = City()
        c.save()
        c_id = "City." + c.id
        with open("file.json") as JsonFile:
            self.assertIn(c_id, JsonFile.read())

    def test_City_to_dict_original_attr(self):
        """test City's to_dict method without adding attributes"""
        c = City(id='test_id',
                 created_at="2017-09-28T21:05:54.119427",
                 updated_at="2017-09-28T21:05:54.119572")
        c_dictionary = c.to_dict()
        expected_dict = {"__class__": City.__name__, "id": "test_id",
                         "created_at": "2017-09-28T21:05:54.119427",
                         "updated_at": "2017-09-28T21:05:54.119572"}
        self.assertEqual(c_dictionary, expected_dict)

    def test_City_dict_new_attr(self):
        """test City's to_dict method with added new attributes"""
        c = City(id='test_id',
                 created_at="2017-09-28T21:05:54.119427",
                 updated_at="2017-09-28T21:05:54.119572")
        c.name = "adxel"
        c.age = 25
        c_dictionary = c.to_dict()
        expected_dict = {"__class__": City.__name__, "id": "test_id",
                         "created_at": "2017-09-28T21:05:54.119427",
                         "updated_at": "2017-09-28T21:05:54.119572",
                         "name": "adxel", "age": 25}
        self.assertEqual(c_dictionary, expected_dict)


if __name__ == "__main__":
    unittest.main()
