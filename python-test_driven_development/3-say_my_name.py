#!/usr/bin/python3
"""
Module Name: 3-say_my_name.py

Description:
    This module include a function that print a name in this format:
    "My name is <first name> <last name>

Functions:
    say_my_name(first_name, last_name="")

Usage:
    This module can be imported:
        from 3-say_my_name import say_my_name
    Or run directly if it contains:
        if __name__ == "__main__":

Author:
    Valentin DUMONT

Date:
    2025-05-14
"""


def say_my_name(first_name, last_name=""):
    """
    Print the name passed.

    Args:
        first_name: The first name (string).
        last_name: The last name (string).

    Returns:
        No return value.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
