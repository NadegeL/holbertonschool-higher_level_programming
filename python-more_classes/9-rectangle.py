#!/usr/bin/python3
"""Write an empty class that define a rectangle"""


class Rectangle:
    """an empty rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """width value set"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """value of height set"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """find perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """return a string representation of rectangle"""
        if self.__width == 0 or self.height == 0:
            return ""

        lines = [str(self.print_symbol) * self.__width for _ in range
                 (self.height)]
        return "\n".join(lines)

    def __repr__(self):
        """ create a repr de str rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """del rectangle and print 'Bye'"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size"""
        return cls(size, size)