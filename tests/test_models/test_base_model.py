#!/usr/bin/python3
"""Unittest for Base_model class attributes and methods"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime
from models.engine.file_storage import FileStorage
import os


class Test_BaseModel_Init(unittest.TestCase):
    """Tests for BaseModel's init"""

    def test_subclass_User(self):
        """check BaseModel's subclass User"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_subclass_State(self):
        """check BaseModel's subclass State"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_subclass_City(self):
        """check BaseModel's subclass City"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_subclass_Amenity(self):
        """check BaseModel's subclass Amenity"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_subclass_Place(self):
        """check BaseModel's subclass Place"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_subclass_Review(self):
        """check BaseModel's subclass Review"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_type_id_attr(self):
        """check the type of the id BaseModel attribute"""
        b = BaseModel()
        self.assertEqual(type(b.id), str)

    def test_type_created_at_attr(self):
        """check the type of the created_at BaseModel attribute"""
        b = BaseModel()
        self.assertEqual(type(b.created_at), datetime)

    def test_type_updated_at_attr(self):
        """check the type of the created_at BaseModel attribute"""
        b = BaseModel()
        self.assertEqual(type(b.updated_at), datetime)

    def test_BaseModel_no_arg(self):
        """Initialize a BaseModel with no args"""
        b = BaseModel()
        self.assertTrue(b.created_at)
        self.assertIsInstance(b.created_at, datetime)
        self.assertTrue(b.updated_at)
        self.assertIsInstance(b.updated_at, datetime)
        self.assertTrue(b.id)
        self.assertIsInstance(b.id, str)

    def test_BaseModel_with_kwargs(self):
        """Initialize a BaseModel with kwargs"""
        kwargs = {"created_at": "2023-08-11T12:00:00",
                  "updated_at": "2023-08-11T12:30:00",
                  "id": "fd8a62d4-b954-4611-944f-2bb0a49242db"}

        b = BaseModel(**kwargs)
        self.assertEqual(b.created_at, datetime(2023, 8, 11, 12, 0))
        self.assertIsInstance(b.created_at, datetime)
        self.assertEqual(b.created_at, datetime(2023, 8, 11, 12, 0))
        self.assertIsInstance(b.updated_at, datetime)
        self.assertIsInstance(b.id, str)
        self.assertEqual(b.id, "fd8a62d4-b954-4611-944f-2bb0a49242db")

    def test_BaseModel_kwargs_None(self):
        """Initialize a BaseModel with None as kwargs"""
        with self.assertRaises(TypeError):
            b = BaseModel(id=None, created_at=None, updated_at=None)


class Test_BaseModel__str__(unittest.TestCase):
    """Test __str__ method of BaseModel"""

    def test_BaseModel_str_representation(self):
        """string representation of BaseModel"""
        b = BaseModel(id='test_id',
                      created_at="2017-09-28T21:05:54.119427",
                      updated_at="2017-09-28T21:05:54.119572")
        expected_str = ("[BaseModel] (test_id) {'id': 'test_id', "
                        "'created_at': datetime.datetime"
                        "(2017, 9, 28, 21, 5, 54, 119427), "
                        "'updated_at': datetime.datetime"
                        "(2017, 9, 28, 21, 5, 54, 119572)}")
        self.assertEqual(str(b), expected_str)


class Test_BaseModel_save(unittest.TestCase):
    """Tests for the __str__ method of BaseModel"""

    def test_updated_at_save(self):
        """test updated_at with the save method"""
        b = BaseModel()
        updated_at_1 = b.updated_at
        b.save()
        updated_at_2 = b.updated_at
        self.assertLess(updated_at_1, updated_at_2)

    def test_updated_at_two_saves(self):
        """test updated_at two saves with the save method"""
        b = BaseModel()
        updated_at_1 = b.updated_at
        b.save()
        updated_at_2 = b.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        b.save()
        updated_at_3 = b.updated_at
        self.assertLess(updated_at_2, updated_at_3)

    def test_save_saves_to_files(self):
        """test save method with saving to and updating a file"""
        b = BaseModel()
        b.save()
        b_id = "BaseModel." + b.id
        with open(FileStorage._FileStorage__file_path) as JsonFile:
            self.assertIn(b_id, JsonFile.read())


class Test_BaseModel_to_dict(unittest.TestCase):
    """Tests for the to_dict method of BaseModel"""

    def test_to_dict_original_attr(self):
        """test to_dict method without adding attributes"""
        b = BaseModel(id='test_id',
                      created_at="2017-09-28T21:05:54.119427",
                      updated_at="2017-09-28T21:05:54.119572")
        b_dictionary = b.to_dict()
        expected_dict = {"__class__": BaseModel.__name__, "id": "test_id",
                         "created_at": "2017-09-28T21:05:54.119427",
                         "updated_at": "2017-09-28T21:05:54.119572"}
        self.assertEqual(b_dictionary, expected_dict)

    def test_dict_new_attr(self):
        """test to_dict method with added new attributes"""
        b = BaseModel(id='test_id',
                      created_at="2017-09-28T21:05:54.119427",
                      updated_at="2017-09-28T21:05:54.119572")
        b.name = "adxel"
        b.age = 25
        b_dictionary = b.to_dict()
        expected_dict = {"__class__": BaseModel.__name__, "id": "test_id",
                         "created_at": "2017-09-28T21:05:54.119427",
                         "updated_at": "2017-09-28T21:05:54.119572",
                         "name": "adxel", "age": 25}
        self.assertEqual(b_dictionary, expected_dict)


if __name__ == "__main__":
    unittest.main()
