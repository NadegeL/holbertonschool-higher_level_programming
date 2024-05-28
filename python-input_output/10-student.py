#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """create a dict of class attributs"""

        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list):
            my_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                my_dict[attr] = getattr(self, attr)
        return my_dict
    
        return self.__dict__
