#!/usr/bin/python3
"""Unit tests for state class"""

import unittest
from models.state import State
from datetime import datetime
import os


class Test_State_Init(unittest.TestCase):
    """tests for State's init"""

    def setUp(self):
        """Set up test environment for each test case"""
        self.s = State()

    def tearDown(self):
        """Clean up test environment atfer each test case"""
        del self.s

    def test_State_no_arg(self):
        """Initialize a State with no args"""
        self.s = State()
        self.assertTrue(self.s.created_at)
        self.assertIsInstance(self.s.created_at, datetime)
        self.assertTrue(self.s.updated_at)
        self.assertIsInstance(self.s.updated_at, datetime)
        self.assertTrue(self.s.id)
        self.assertIsInstance(self.s.id, str)

    def test_State_with_kwargs(self):
        """Initialize a State with kwargs"""
        kwargs = {"created_at": "2023-08-11T12:00:00",
                  "updated_at": "2023-08-11T12:30:00",
                  "id": "fd8a62d4-b954-4611-944f-2bb0a49242db"}

        self.s = State(**kwargs)
        self.assertEqual(self.s.created_at, datetime(2023, 8, 11, 12, 0))
        self.assertIsInstance(self.s.created_at, datetime)
        self.assertEqual(self.s.created_at, datetime(2023, 8, 11, 12, 0))
        self.assertIsInstance(self.s.updated_at, datetime)
        self.assertIsInstance(self.s.id, str)
        self.assertEqual(self.s.id, "fd8a62d4-b954-4611-944f-2bb0a49242db")

    def test_State_attributes(self):
        """tests the attributes for class state"""
        self.assertTrue(hasattr(self.s, "name"))

    def test_State_attributes_default_values(self):
        """test the default values of attributes"""
        self.assertEqual(self.s.name, "")

    def test_State_kwargs_None(self):
        """Initialize a State with None as kwargs"""
        with self.assertRaises(TypeError):
            s = State(id=None, created_at=None, updated_at=None)


class Test_State__str__(unittest.TestCase):
    """Test __str__ method of State"""

    def test_State_str_representation(self):
        """string representation of State"""
        s = State(id='test_id',
                  created_at="2017-09-28T21:05:54.119427",
                  updated_at="2017-09-28T21:05:54.119572")
        expected_str = ("[State] (test_id) {'id': 'test_id', "
                        "'created_at': datetime.datetime"
                        "(2017, 9, 28, 21, 5, 54, 119427), "
                        "'updated_at': datetime.datetime"
                        "(2017, 9, 28, 21, 5, 54, 119572)}")
        self.assertEqual(str(s), expected_str)


class Test_State_save(unittest.TestCase):
    """Tests for the __str__ method of State"""

    def test_State_updated_at_save(self):
        """test State's updated_at with the save method"""
        s = State()
        updated_at_1 = s.updated_at
        s.save()
        updated_at_2 = s.updated_at
        self.assertLess(updated_at_1, updated_at_2)

    def test_State_updated_at_two_saves(self):
        """test State's updated_at two saves with the save method"""
        s = State()
        updated_at_1 = s.updated_at
        s.save()
        updated_at_2 = s.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        s.save()
        updated_at_3 = s.updated_at
        self.assertLess(updated_at_2, updated_at_3)

    def test_State_save_saves_to_files(self):
        """test State's save method with saving to and updating a file"""
        s = State()
        s.save()
        s_id = "State." + s.id
        with open("file.json") as JsonFile:
            self.assertIn(s_id, JsonFile.read())


class Test_State_to_dict(unittest.TestCase):
    """Tests for the to_dict method of State"""

    def test_State_to_dict_original_attr(self):
        """test State's to_dict method without adding attributes"""
        s = State(id='test_id',
                  created_at="2017-09-28T21:05:54.119427",
                  updated_at="2017-09-28T21:05:54.119572")
        s_dictionary = s.to_dict()
        expected_dict = {"__class__": State.__name__, "id": "test_id",
                         "created_at": "2017-09-28T21:05:54.119427",
                         "updated_at": "2017-09-28T21:05:54.119572"}
        self.assertEqual(s_dictionary, expected_dict)

    def test_State_dict_new_attr(self):
        """test State's to_dict method with added new attributes"""
        s = State(id='test_id',
                  created_at="2017-09-28T21:05:54.119427",
                  updated_at="2017-09-28T21:05:54.119572")
        s.name = "adxel"
        s.age = 25
        s_dictionary = s.to_dict()
        expected_dict = {"__class__": State.__name__, "id": "test_id",
                         "created_at": "2017-09-28T21:05:54.119427",
                         "updated_at": "2017-09-28T21:05:54.119572",
                         "name": "adxel", "age": 25}
        self.assertEqual(s_dictionary, expected_dict)


if __name__ == "__main__":
    unittest.main()
