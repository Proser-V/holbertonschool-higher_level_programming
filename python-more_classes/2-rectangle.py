#!/usr/bin/python3
"""
Module Name: 2-rectangle.py

Description:
    This module include an empty class that defines a rectangle.
    An instance returns the rectangle area.
    An instance returns the rectangle perimeter.
"""


class Rectangle:
    """
    A class that defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.width + self.height) * 2
