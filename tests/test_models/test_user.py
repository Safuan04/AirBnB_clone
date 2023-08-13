#!/usr/bin/python3
"""Unit tests for user class"""

import unittest
import models
from models.user import User
from datetime import datetime
import os


class Test_User(unittest.TestCase):
    """Test casess for User class"""

    def setUp(self):
        """Set up test environment for each test case"""
        self.user = User()

    def tearDown(self):
        """Clean up test environment atfer each test case"""
        del self.user

    def test_User_no_arg(self):
        """Initialize a User with no args"""
        self.user = User()
        self.assertTrue(self.user.created_at)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertTrue(self.user.updated_at)
        self.assertIsInstance(self.user.updated_at, datetime)
        self.assertTrue(self.user.id)
        self.assertIsInstance(self.user.id, str)

    def test_User_with_kwargs(self):
        """Initialize a User with kwargs"""
        kwargs = {"created_at": "2023-08-11T12:00:00",
                  "updated_at": "2023-08-11T12:30:00",
                  "id": "fd8a62d4-b954-4611-944f-2bb0a49242db"}

        self.user = User(**kwargs)
        self.assertEqual(self.user.created_at, datetime(2023, 8, 11, 12, 0))
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertEqual(self.user.created_at, datetime(2023, 8, 11, 12, 0))
        self.assertIsInstance(self.user.updated_at, datetime)
        self.assertIsInstance(self.user.id, str)
        self.assertEqual(self.user.id, "fd8a62d4-b954-4611-944f-2bb0a49242db")

    def test_User_kwargs_None(self):
        """Initialize a User with None as kwargs"""
        with self.assertRaises(TypeError):
            u = User(id=None, created_at=None, updated_at=None)

    def test_User_attributes(self):
        """tests the attributes for class user"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_User_attributes_default_values(self):
        """test the default values of attributes"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_User_unique_id(self):
        """test different User's ids"""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_updated_at_datetime(self):
        """Checks if attribute is a datetime object"""
        self.assertEqual(datetime, type(User(). updated_at))

    def test_User_str_representation(self):
        """string representation of User"""
        u = User(id='test_id',
                 created_at="2017-09-28T21:05:54.119427",
                 updated_at="2017-09-28T21:05:54.119572")
        expected_str = ("[User] (test_id) {'id': 'test_id', "
                        "'created_at': datetime.datetime"
                        "(2017, 9, 28, 21, 5, 54, 119427), "
                        "'updated_at': datetime.datetime"
                        "(2017, 9, 28, 21, 5, 54, 119572)}")
        self.assertEqual(str(u), expected_str)

    def test_User_updated_at_save(self):
        """test User's updated_at with the save method"""
        u = User()
        updated_at_1 = u.updated_at
        u.save()
        updated_at_2 = u.updated_at
        self.assertLess(updated_at_1, updated_at_2)

    def test_User_updated_at_two_saves(self):
        """test User's updated_at two saves with the save method"""
        u = User()
        updated_at_1 = u.updated_at
        u.save()
        updated_at_2 = u.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        u.save()
        updated_at_3 = u.updated_at
        self.assertLess(updated_at_2, updated_at_3)

    def test_save_updates_file(self):
        """tests that updates are updated and stored correctly"""
        usr = User()
        usr.save()
        usrid = "User." + usr.id
        with open("file.json", "r") as file:
            self.assertIn(usrid, file.read())

    def test_to_dict(self):
        """Tests the expected output"""
        expected_dict = {
            'id': self.user.id,
            'created_at': self.user.created_at.isoformat(),
            'updated_at': self.user.updated_at.isoformat(),
            '__class__': 'User'
        }
        self.assertEqual(self.user.to_dict(), expected_dict)

    def test_User_to_dict_original_attr(self):
        """test User's to_dict method without adding attributes"""
        u = User(id='test_id',
                 created_at="2017-09-28T21:05:54.119427",
                 updated_at="2017-09-28T21:05:54.119572")
        u_dictionary = u.to_dict()
        expected_dict = {"__class__": User.__name__, "id": "test_id",
                         "created_at": "2017-09-28T21:05:54.119427",
                         "updated_at": "2017-09-28T21:05:54.119572"}
        self.assertEqual(u_dictionary, expected_dict)

    def test_User_dict_new_attr(self):
        """test User's to_dict method with added new attributes"""
        u = User(id='test_id',
                 created_at="2017-09-28T21:05:54.119427",
                 updated_at="2017-09-28T21:05:54.119572")
        u.name = "adxel"
        u.age = 25
        u_dictionary = u.to_dict()
        expected_dict = {"__class__": User.__name__, "id": "test_id",
                         "created_at": "2017-09-28T21:05:54.119427",
                         "updated_at": "2017-09-28T21:05:54.119572",
                         "name": "adxel", "age": 25}
        self.assertEqual(u_dictionary, expected_dict)


if __name__ == "__main__":
    unittest.main()
