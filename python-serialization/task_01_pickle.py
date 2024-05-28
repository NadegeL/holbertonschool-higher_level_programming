#!/usr/bin/env python3
"""Pickling Custom Classes"""
import pickle


class CustomObject:
    """Create a custom Python class"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """method to print in a specific format"""

        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is_student: {self.is_student}")

    def serialize(self, filename):
        """
        Method that serialize the current instance of the object
        and save it to the provided filename.
        """

        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Method that load and return an instance of
        the CustomObject from the provided filename
        """

        with open(filename, "rb") as f:
            return pickle.load(f)
