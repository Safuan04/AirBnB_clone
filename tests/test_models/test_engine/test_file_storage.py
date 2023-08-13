#!/usr/bin/python3
"""Unittest for FileStorage class attributes and methods"""

import unittest
import models
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime
from models.engine.file_storage import FileStorage


class Test_FileStorage_Init(unittest.TestCase):
    """Tests for FileStorage attributes"""

    def test_file_path_private_attr_type(self):
        """test file_path attribute type"""
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_file_path_attr_json(self):
        """check if file_path attribute is json file"""
        json_file = FileStorage._FileStorage__file_path.split(".")
        json_check = json_file[1]
        self.assertEqual(json_check, "json")

    def test_objects_private_attr_type(self):
        """test objects attribute type"""
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_FileStorage_no_arg(self):
        """test FileStorage with no args"""
        f = FileStorage()
        self.assertEqual(type(f), FileStorage)

    def test_FileStorage_with_arg(self):
        """test FileStorage with args"""
        with self.assertRaises(TypeError):
            FileStorage(12)

    def test_storage_init(self):
        """test storage initialization"""
        self.assertEqual(type(models.storage), FileStorage)


class Test_FileStorage_all_method(unittest.TestCase):
    """Tests for FileStorage all method"""

    def test_all_no_arg(self):
        """test all method with no arg"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_arg(self):
        """test all method with args"""
        with self.assertRaises(TypeError):
            models.storage.all(12)


class Test_FileStorage_new_method(unittest.TestCase):
    """Tests FileStorage new method"""

    def test_new_BaseModel(self):
        """test new method on BaseModel class"""
        base = BaseModel()
        models.storage.new(base)
        self.assertIn(f"BaseModel.{base.id}", models.storage.all())
        self.assertEqual(models.storage.all()[f"BaseModel.{base.id}"], base)

    def test_new_User(self):
        """test new method on User class"""
        user = User()
        models.storage.new(user)
        self.assertIn(f"User.{user.id}", models.storage.all())
        self.assertEqual(models.storage.all()[f"User.{user.id}"], user)

    def test_new_State(self):
        """test new method on State class"""
        state = State()
        models.storage.new(state)
        self.assertIn(f"State.{state.id}", models.storage.all())
        self.assertEqual(models.storage.all()[f"State.{state.id}"], state)

    def test_new_City(self):
        """test new method on City class"""
        city = City()
        models.storage.new(city)
        self.assertIn(f"City.{city.id}", models.storage.all())
        self.assertEqual(models.storage.all()[f"City.{city.id}"], city)

    def test_new_Amenity(self):
        """test new method on Amenity class"""
        ameni = Amenity()
        models.storage.new(ameni)
        self.assertIn(f"Amenity.{ameni.id}", models.storage.all())
        self.assertEqual(models.storage.all()[f"Amenity.{ameni.id}"], ameni)

    def test_new_Place(self):
        """test new method on Place class"""
        place = Place()
        models.storage.new(place)
        self.assertIn(f"Place.{place.id}", models.storage.all())
        self.assertEqual(models.storage.all()[f"Place.{place.id}"], place)

    def test_new_Review(self):
        """test new method on Review class"""
        review = Review()
        models.storage.new(review)
        self.assertIn(f"Review.{review.id}", models.storage.all())
        self.assertEqual(models.storage.all()[f"Review.{review.id}"], review)

    def test_new_no_arg(self):
        """test new method with no args"""
        with self.assertRaises(TypeError):
            models.storage.new()

    def test_new_more_than_one_arg(self):
        """test new method with more than one arg"""
        with self.assertRaises(TypeError):
            models.storage.new(User, "new_id")


class Test_FileStorage_save_method(unittest.TestCase):
    """Tests for FileStorage save method"""

    def test_save_BaseModel(self):
        """test save method on BaseModel class"""
        base = BaseModel()
        models.storage.save()
        with open(FileStorage._FileStorage__file_path) as JsonFile:
            file_data = JsonFile.read()
            self.assertIn(f"BaseModel.{base.id}", file_data)

    def test_save_User(self):
        """test save method on User class"""
        user = User()
        models.storage.save()
        with open(FileStorage._FileStorage__file_path) as JsonFile:
            file_data = JsonFile.read()
            self.assertIn(f"User.{user.id}", file_data)

    def test_save_State(self):
        """test save method on State class"""
        state = State()
        models.storage.save()
        with open(FileStorage._FileStorage__file_path) as JsonFile:
            file_data = JsonFile.read()
            self.assertIn(f"State.{state.id}", file_data)

    def test_save_City(self):
        """test save method on City class"""
        city = City()
        models.storage.save()
        with open(FileStorage._FileStorage__file_path) as JsonFile:
            file_data = JsonFile.read()
            self.assertIn(f"City.{city.id}", file_data)

    def test_save_Amenity(self):
        """test save method on Amenity class"""
        amenity = Amenity()
        models.storage.save()
        with open(FileStorage._FileStorage__file_path) as JsonFile:
            file_data = JsonFile.read()
            self.assertIn(f"Amenity.{amenity.id}", file_data)

    def test_save_Place(self):
        """test save method on Place class"""
        place = Place()
        models.storage.save()
        with open(FileStorage._FileStorage__file_path) as JsonFile:
            file_data = JsonFile.read()
            self.assertIn(f"Place.{place.id}", file_data)


class Test_FileStorage_reload_method(unittest.TestCase):
    """Tests for FileStorage reload method"""

    def test_reload_BaseModel(self):
        """test the reload method on BaseModel"""
        base = BaseModel()
        models.storage.new(base)
        models.storage.save()
        models.storage.reload()
        self.assertIn(f"BaseModel.{base.id}", models.storage.all())
        reload_base = models.storage.all()[f"BaseModel.{base.id}"]
        self.assertEqual(reload_base.id, base.id)

    def test_reload_User(self):
        """test the reload method on User"""
        user = User()
        models.storage.new(user)
        models.storage.save()
        models.storage.reload()
        self.assertIn(f"User.{user.id}", models.storage.all())
        reload_user = models.storage.all()[f"User.{user.id}"]
        self.assertEqual(reload_user.id, user.id)

    def test_reload_State(self):
        """test the reload method on State"""
        state = State()
        models.storage.new(state)
        models.storage.save()
        models.storage.reload()
        self.assertIn(f"State.{state.id}", models.storage.all())
        reload_state = models.storage.all()[f"State.{state.id}"]
        self.assertEqual(reload_state.id, state.id)

    def test_reload_City(self):
        """test the reload method on City"""
        city = City()
        models.storage.new(city)
        models.storage.save()
        models.storage.reload()
        self.assertIn(f"City.{city.id}", models.storage.all())
        reload_city = models.storage.all()[f"City.{city.id}"]
        self.assertEqual(reload_city.id, city.id)

    def test_reload_Amenity(self):
        """test the reload method on Amenity"""
        amenity = Amenity()
        models.storage.new(amenity)
        models.storage.save()
        models.storage.reload()
        self.assertIn(f"Amenity.{amenity.id}", models.storage.all())
        reload_amenity = models.storage.all()[f"Amenity.{amenity.id}"]
        self.assertEqual(reload_amenity.id, amenity.id)

    def test_reload_Place(self):
        """test the reload method on Place"""
        place = Place()
        models.storage.new(place)
        models.storage.save()
        models.storage.reload()
        self.assertIn(f"Place.{place.id}", models.storage.all())
        reload_place = models.storage.all()[f"Place.{place.id}"]
        self.assertEqual(reload_place.id, place.id)

    def test_reload_Review(self):
        """test the reload method on Review"""
        review = Review()
        models.storage.new(review)
        models.storage.save()
        models.storage.reload()
        self.assertIn(f"Review.{review.id}", models.storage.all())
        reload_review = models.storage.all()[f"Review.{review.id}"]
        self.assertEqual(reload_review.id, review.id)

    def test_reload_with_arg(self):
        """test the reload method with arguments"""
        with self.assertRaises(TypeError):
            models.storage.reload(User)


if __name__ == "__main__":
    unittest.main()
