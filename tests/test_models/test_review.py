#!/usr/bin/python3
"""Unit tests for review class"""

import unittest
from models.review import Review
from datetime import datetime
import os


class Test_Review_Init(unittest.TestCase):
    """tests for Review's init"""

    def setUp(self):
        """Set up test environment for each test case"""
        self.rev = Review()

    def tearDown(self):
        """Clean up test environment atfer each test case"""
        del self.rev

    def test_Review_no_arg(self):
        """Initialize a Review with no args"""
        self.rev = Review()
        self.assertTrue(self.rev.created_at)
        self.assertIsInstance(self.rev.created_at, datetime)
        self.assertTrue(self.rev.updated_at)
        self.assertIsInstance(self.rev.updated_at, datetime)
        self.assertTrue(self.rev.id)
        self.assertIsInstance(self.rev.id, str)

    def test_Review_with_kwargs(self):
        """Initialize a Review with kwargs"""
        kwargs = {"created_at": "2023-08-11T12:00:00",
                  "updated_at": "2023-08-11T12:30:00",
                  "id": "fd8a62d4-b954-4611-944f-2bb0a49242db"}

        self.rev = Review(**kwargs)
        self.assertEqual(self.rev.created_at, datetime(2023, 8, 11, 12, 0))
        self.assertIsInstance(self.rev.created_at, datetime)
        self.assertEqual(self.rev.created_at, datetime(2023, 8, 11, 12, 0))
        self.assertIsInstance(self.rev.updated_at, datetime)
        self.assertIsInstance(self.rev.id, str)
        self.assertEqual(self.rev.id, "fd8a62d4-b954-4611-944f-2bb0a49242db")

    def test_Review_attributes(self):
        """tests the attributes for class review"""
        self.assertTrue(hasattr(self.rev, "place_id"))
        self.assertTrue(hasattr(self.rev, "user_id"))
        self.assertTrue(hasattr(self.rev, "text"))

    def test_Review_attributes_default_values(self):
        """test the default values of attributes"""
        self.assertEqual(self.rev.place_id, "")
        self.assertEqual(self.rev.user_id, "")
        self.assertEqual(self.rev.text, "")

    def test_Review_kwargs_None(self):
        """Initialize a Review with None as kwargs"""
        with self.assertRaises(TypeError):
            r = Review(id=None, created_at=None, updated_at=None)


class Test_Review__str__(unittest.TestCase):
    """Test __str__ method of Review"""

    def test_Review_str_representation(self):
        """string representation of Review"""
        r = Review(id='test_id',
                   created_at="2017-09-28T21:05:54.119427",
                   updated_at="2017-09-28T21:05:54.119572")
        expected_str = ("[Review] (test_id) {'id': 'test_id', "
                        "'created_at': datetime.datetime"
                        "(2017, 9, 28, 21, 5, 54, 119427), "
                        "'updated_at': datetime.datetime"
                        "(2017, 9, 28, 21, 5, 54, 119572)}")
        self.assertEqual(str(r), expected_str)


class Test_Review_save(unittest.TestCase):
    """Tests for the __str__ method of Review"""

    def test_Review_updated_at_save(self):
        """test Review's updated_at with the save method"""
        r = Review()
        updated_at_1 = r.updated_at
        r.save()
        updated_at_2 = r.updated_at
        self.assertLess(updated_at_1, updated_at_2)

    def test_Review_updated_at_two_saves(self):
        """test Review's updated_at two saves with the save method"""
        r = Review()
        updated_at_1 = r.updated_at
        r.save()
        updated_at_2 = r.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        r.save()
        updated_at_3 = r.updated_at
        self.assertLess(updated_at_2, updated_at_3)

    def test_Review_save_saves_to_files(self):
        """test Review's save method with saving to and updating a file"""
        r = Review()
        r.save()
        r_id = "Review." + r.id
        with open("file.json") as JsonFile:
            self.assertIn(r_id, JsonFile.read())


class Test_Review_to_dict(unittest.TestCase):
    """Tests for the to_dict method of Review"""

    def test_Review_to_dict_original_attr(self):
        """test Review's to_dict method without adding attributes"""
        r = Review(id='test_id',
                   created_at="2017-09-28T21:05:54.119427",
                   updated_at="2017-09-28T21:05:54.119572")
        r_dictionary = r.to_dict()
        expected_dict = {"__class__": Review.__name__, "id": "test_id",
                         "created_at": "2017-09-28T21:05:54.119427",
                         "updated_at": "2017-09-28T21:05:54.119572"}
        self.assertEqual(r_dictionary, expected_dict)

    def test_Review_dict_new_attr(self):
        """test Review's to_dict method with added new attributes"""
        r = Review(id='test_id',
                   created_at="2017-09-28T21:05:54.119427",
                   updated_at="2017-09-28T21:05:54.119572")
        r.name = "adxel"
        r.age = 25
        r_dictionary = r.to_dict()
        expected_dict = {"__class__": Review.__name__, "id": "test_id",
                         "created_at": "2017-09-28T21:05:54.119427",
                         "updated_at": "2017-09-28T21:05:54.119572",
                         "name": "adxel", "age": 25}
        self.assertEqual(r_dictionary, expected_dict)


if __name__ == "__main__":
    unittest.main()
