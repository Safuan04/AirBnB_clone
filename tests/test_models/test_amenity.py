#!/usr/bin/python3
"""Unit tests for amenity class"""

import unittest
import models
from models.amenity import Amenity
from datetime import datetime
import os


class Test_Amenity_Init(unittest.TestCase):
    """tests for Amenity's init"""

    def setUp(self):
        """Set up test environment for each test case"""
        self.am = Amenity()

    def tearDown(self):
        """Clean up test environment atfer each test case"""
        del self.am

    def test_Amenity_no_arg(self):
        """Initialize a Amenity with no args"""
        self.am = Amenity()
        self.assertTrue(self.am.created_at)
        self.assertIsInstance(self.am.created_at, datetime)
        self.assertTrue(self.am.updated_at)
        self.assertIsInstance(self.am.updated_at, datetime)
        self.assertTrue(self.am.id)
        self.assertIsInstance(self.am.id, str)

    def test_Amenity_with_kwargs(self):
        """Initialize a Amenity with kwargs"""
        kwargs = {"created_at": "2023-08-11T12:00:00",
                  "updated_at": "2023-08-11T12:30:00",
                  "id": "fd8a62d4-b954-4611-944f-2bb0a49242db"}

        self.am = Amenity(**kwargs)
        self.assertEqual(self.am.created_at, datetime(2023, 8, 11, 12, 0))
        self.assertIsInstance(self.am.created_at, datetime)
        self.assertEqual(self.am.created_at, datetime(2023, 8, 11, 12, 0))
        self.assertIsInstance(self.am.updated_at, datetime)
        self.assertIsInstance(self.am.id, str)
        self.assertEqual(self.am.id, "fd8a62d4-b954-4611-944f-2bb0a49242db")

    def test_Amenity_attributes(self):
        """tests the attributes for class amenity"""
        self.assertTrue(hasattr(self.am, "name"))

    def test_Amenity_attributes_default_values(self):
        """test the default values of attributes"""
        self.assertEqual(self.am.name, "")

    def test_Amenity_kwargs_None(self):
        """Initialize a Amenity with None as kwargs"""
        with self.assertRaises(TypeError):
            a = Amenity(id=None, created_at=None, updated_at=None)


class Test_Amenity__str__(unittest.TestCase):
    """Test __str__ method of Amenity"""

    def test_Amenity_str_representation(self):
        """string representation of Amenity"""
        a = Amenity(id='test_id',
                    created_at="2017-09-28T21:05:54.119427",
                    updated_at="2017-09-28T21:05:54.119572")
        expected_str = ("[Amenity] (test_id) {'id': 'test_id', "
                        "'created_at': datetime.datetime"
                        "(2017, 9, 28, 21, 5, 54, 119427), "
                        "'updated_at': datetime.datetime"
                        "(2017, 9, 28, 21, 5, 54, 119572)}")
        self.assertEqual(str(a), expected_str)


class Test_Amenity_save(unittest.TestCase):
    """Tests for the __str__ method of Amenity"""

    def test_Amenity_updated_at_save(self):
        """test Amenity's updated_at with the save method"""
        a = Amenity()
        updated_at_1 = a.updated_at
        a.save()
        updated_at_2 = a.updated_at
        self.assertLess(updated_at_1, updated_at_2)

    def test_Amenity_updated_at_two_saves(self):
        """test Amenity's updated_at two saves with the save method"""
        a = Amenity()
        updated_at_1 = a.updated_at
        a.save()
        updated_at_2 = a.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        a.save()
        updated_at_3 = a.updated_at
        self.assertLess(updated_at_2, updated_at_3)

    def test_Amenity_save_saves_to_files(self):
        """test Amenity's save method with saving to and updating a file"""
        a = Amenity()
        a.save()
        a_id = "Amenity." + a.id
        with open("file.json") as JsonFile:
            self.assertIn(a_id, JsonFile.read())


class Test_Amenity_to_dict(unittest.TestCase):
    """Tests for the to_dict method of Amenity"""

    def test_Amenity_to_dict_original_attr(self):
        """test Amenity's to_dict method without adding attributes"""
        a = Amenity(id='test_id',
                    created_at="2017-09-28T21:05:54.119427",
                    updated_at="2017-09-28T21:05:54.119572")
        a_dictionary = a.to_dict()
        expected_dict = {"__class__": Amenity.__name__, "id": "test_id",
                         "created_at": "2017-09-28T21:05:54.119427",
                         "updated_at": "2017-09-28T21:05:54.119572"}
        self.assertEqual(a_dictionary, expected_dict)

    def test_Amenity_dict_new_attr(self):
        """test Amenity's to_dict method with added new attributes"""
        a = Amenity(id='test_id',
                    created_at="2017-09-28T21:05:54.119427",
                    updated_at="2017-09-28T21:05:54.119572")
        a.name = "adxel"
        a.age = 25
        a_dictionary = a.to_dict()
        expected_dict = {"__class__": Amenity.__name__, "id": "test_id",
                         "created_at": "2017-09-28T21:05:54.119427",
                         "updated_at": "2017-09-28T21:05:54.119572",
                         "name": "adxel", "age": 25}
        self.assertEqual(a_dictionary, expected_dict)


if __name__ == "__main__":
    unittest.main()
