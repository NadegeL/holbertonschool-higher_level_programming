#!/usr/bin/python3
"""Learn how to serialize and deserialize
custom Python objects using the pickle module."""

import pickle


class CustomObject:
    """custom Python class"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """display object attributes"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """serialize and save current object"""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """deserialize and load object from file"""
        with open(filename, 'rb') as file:
            instance = pickle.load(file)
            return instance
