#!/usr/bin/env python3
"""create a polymorphisme class"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Shape Class abstract"""
    @abstractmethod
    def area(self):
        """abstract method area"""
        pass

    @abstractmethod
    def perimeter(self):
        """abstract method perimeter"""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape"""

    def __init__(self, radius):
        """initialize Circle"""
        self.radius = radius

    def area(self):
        """implement area method"""
        return self.radius ** 2 * 3.14159265359

    def perimeter(self):
        """implement perimeter method"""
        return 2 * 3.14159265359 *(abs(self.radius))


class Rectangle(Shape):
    """Rectangle class that inherits from Shape"""

    def __init__(self, width, height):
        """initialize Rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """implement area method"""
        return self.width * self.height

    def perimeter(self):
        """implement perimeter method"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """print the area and perimeter of the shape"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
