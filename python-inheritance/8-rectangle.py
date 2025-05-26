#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""
Module Name: 8-rectangle.py

Description:
    This module include a class that validates a rectangle values
"""


class Rectangle(BaseGeometry):
    """
        A class that validates a rectangle values
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
