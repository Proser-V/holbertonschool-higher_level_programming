#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi


"""
Module Name: task_01_duck_typing.py

Description:
    This module include an abstract class and subclasses
"""


class Shape(ABC):
    """
        An abstract class with abstract method for sub classes
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
        A subclass for a typical object
    """
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """
        A subclass for a typical object
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """
    A function simulating duck-typing
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
