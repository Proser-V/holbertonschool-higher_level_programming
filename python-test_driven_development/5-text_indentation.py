#!/usr/bin/python3
"""
Module Name: 5-text_indentation.py

Description:
    Prints a text with 2 new lines after certain characters.

Functions:
    text_indentation(text): indentation modification of a text.

Usage:
    This module can be imported:
        from 5-text_indentation.py import text_indentation
    Or run directly if it contains:
        if __name__ == "__main__":

Author:
    Valentin DUMONT

Date:
    2025-05-14
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after certain characters.

    Args:
        text: A string.

    Returns:
        No return value. Prints strings.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    new_line_check = 0
    for i in range(len(text)):
        char = text[i]
        if new_line_check == 1:
            if char != " ":
                new_line_check = 0
                print(char, end="")
            continue
        if char in '.:?':
            print(char)
            print()
            new_line_check = 1
        else:
            print(char, end="")
