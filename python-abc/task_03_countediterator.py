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
        self.object = iter(object)
        self.counter = 0

    def __next__(self):
        try:
            self.counter += 1
            return next(self.object)
        except StopIteration:
            raise

    def get_count(self):
        return self.counter
