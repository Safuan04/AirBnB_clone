#!/usr/bin/python3
"""Defining a variable storage to create a unique
FileStorage instance for the AirBnB Application
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
