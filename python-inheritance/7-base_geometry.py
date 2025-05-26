#!/usr/bin/python3
"""
Module Name: 7-base_geometry.py

Description:
    This module include a class that raise an exception because
    its method is not implemented?!
"""


class BaseGeometry:
    """
        A class that raise an exception because
        its method is not implemented?!
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
