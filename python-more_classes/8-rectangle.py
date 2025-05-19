#!/usr/bin/python3
"""
Module Name: 7-rectangle.py

Description:
    This module include an empty class that defines a rectangle.
    An instance returns the rectangle area.
    An instance returns the rectangle perimeter.
    Prints the rectangle with the choosen symbole ("#" default).
"""


class Rectangle:
    """
    A class that defines a rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """
        An instance returns the rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        An instance returns the rectangle perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Prints the rectangle with the choosen symbole ("#" default).
        """
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        lines = [symbol * self.width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """
        Return a string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Called when an instance of Rectangle is deleted.
        Prints a farewell message.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        rect_1_area = rect_1.width * rect_1.height
        rect_2_area = rect_2.width * rect_2.height
        if rect_1_area < rect_2_area:
            return rect_2
        else:
            return rect_1
