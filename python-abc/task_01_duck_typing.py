#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Defines a class Shape
    """
    @abstractmethod
    def area(self):
        """
        Empty abstract method area
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Empty abstract method perimeter
        """
        pass


class Circle(Shape):
    """
    class Circle inherits from Shape
    """

    def __init__(self, radius):
        """
        initialize the class Circle
        """
        self.radius = radius

    def area(self):
        """
            area of circle
        """
        return abs(math.pi * (self.radius ** 2))

    def perimeter(self):
        """
            perimeter of circle
        """
        return abs(2 * math.pi * self.radius)


class Rectangle(Shape):
    """
    class Rectangle inherits from Shape
    """

    def __init__(self, width, height):
        """
        initialize attributes
        """
        self.width = width
        self.height = height

    def area(self):
        """
            area of the Rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
            perimeter of the class Rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Method that print the area and perimeter of the shape
    """
    try:
        shape_area = shape.area()
        shape_perimeter = shape.perimeter()
        print("Area: {}".format(shape_area))
        print("Perimeter: {}".format(shape_perimeter))
    except AttributeError as e:
        print(f"Error: {e}")
