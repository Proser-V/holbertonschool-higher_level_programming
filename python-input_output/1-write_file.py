#!/usr/bin/python3

"""
Description : This module contain a function that writes a string to a
text file (UTF8) and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    This function that writes a string to a text file (UTF8) and
    returns the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    return len(text)
