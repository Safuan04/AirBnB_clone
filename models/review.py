#!/usr/bin/python3
"""Defining a class called Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
