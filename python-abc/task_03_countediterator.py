#!/usr/bin/python3
"""
Module Name: task_03_countediterator.py

Description:
    This module include a class that extends the built-in iterator
    obtained from the "iter" function.
"""


class CountedIterator:
    """
        A class that extends the built-in iterator obtained from
        the "iter" function.
    """

    def __init__(self, object):
        self.__object = iter(object)
        self.__counter = 0

    def get_count(self):
        return self.__counter

    def __next__(self):
        try:
            item = next(self.__object)
            self.__counter += 1
            return item
        except StopIteration:
            raise
