#!/usr/bin/python3
"""
Module Name: 102-square.py

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

    def __eq__(self, other):
        if not isinstance(other, Square):
            raise TypeError("You can only compare 2 squares")
        return self.area() == other.area()

    def __ne__(self, other):
        if not isinstance(other, Square):
            raise TypeError("You can only compare 2 squares")
        return self.area() != other.area()

    def __lt__(self, other):
        if not isinstance(other, Square):
            raise TypeError("You can only compare 2 squares")
        return self.area() < other.area()

    def __le__(self, other):
        if not isinstance(other, Square):
            raise TypeError("You can only compare 2 squares")
        return self.area() <= other.area()

    def __gt__(self, other):
        if not isinstance(other, Square):
            raise TypeError("You can only compare 2 squares")
        return self.area() > other.area()

    def __ge__(self, other):
        if not isinstance(other, Square):
            raise TypeError("You can only compare 2 squares")
        return self.area() >= other.area()
