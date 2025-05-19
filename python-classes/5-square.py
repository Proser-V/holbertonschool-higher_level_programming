#!/usr/bin/python3
"""
Module Name: 5-square.py

Description:
    This module include a class that defines a square.
    An instance returns the current square area.
"""


class Square:
    """
    A class that defines a square
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """
        A property that retrieves the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        A property that set the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        An instance that returns the surrent square area
        """
        return self.__size ** 2

    def my_print(self):
        i = 0
        if self.__size == 0:
            print()
        else:
            while i < self.__size:
                j = 0
                while j < self.__size:
                    print("#", end="")
                    j += 1
                print()
                i += 1
