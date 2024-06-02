#!/usr/bin/python3

"""
This script builds a class with a private attribute

Attributes:
    Square (class): a class with a private attribute called 'size'
"""


class Square:
    """
    A square with a 'size' attribute
    """
    def __init__(self, size):
        """
        Args:
            self (Square): class object.
            size (int): object dimension
        """
        self.__size = size