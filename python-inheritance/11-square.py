#!/usr/bin/python3


"""
Module Name: 11-square.py

Description:
    This module include a class that calculate the area of a square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        A class that calculate the area of a square
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        square_area = self.__size ** 2
        return square_area

    def __str__(self):
        return str("[Square] {}/{}".format(self.__size, self.__size))
