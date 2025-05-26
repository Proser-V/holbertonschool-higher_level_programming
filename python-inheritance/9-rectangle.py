#!/usr/bin/python3


"""
Module Name: 9-rectangle.py

Description:
    This module include a class that calculate the area of a rectangle
    and print its height and width
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        A class that calculate the area of a rectangle and print its
        height and width
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        rect_area = self.__height * self.__width
        return rect_area

    def print(self):
        print("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __str__(self):
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
