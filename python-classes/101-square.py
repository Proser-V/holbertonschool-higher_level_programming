#!/usr/bin/python3
"""
Module Name: 101-square.py

Description:
    This module include a class that defines a square.
    An instance returns the current square area.
"""


class Square:
    """
    A class that defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        A property that retrieves the size of the square.
        """
        return self.__size

    @property
    def position(self):
        """
        A property that retrieves the position of the square.
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        A property that set the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """
        A property that set the indentation of the square.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        An instance that returns the surrent square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        An instance that prints the square with "#".
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        if self.__size == 0:
            return ""

        lines = [""] * self.__position[1]

        for _ in range(self.__size):
            line = " " * self.__position[0] + "#" * self.__size
            lines.append(line)

        return "\n".join(lines)
