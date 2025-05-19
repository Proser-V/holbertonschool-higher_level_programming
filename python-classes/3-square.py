#!/usr/bin/python3
"""
Module Name: 1-square.py

Description:
    This module include a class that defines a square.
    An instance returns the current square area.
"""


class Square:
    """
    A class that defines a square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        An instance that returns the surrent square area
        """
        return self.__size ** 2
