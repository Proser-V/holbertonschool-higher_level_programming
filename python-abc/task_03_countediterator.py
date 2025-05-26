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
    counter = 0
    
    def __init__(self, object):
        self.object = iter(object)

    def __next__(self):
        CountedIterator.counter += 1
        return next(self.object)

    def get_count(self):
        return CountedIterator.counter
