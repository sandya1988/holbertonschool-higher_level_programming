#!/usr/bin/python3

"""
A script that creates a class and validates its given attribute

Attributes:
    Square (class): with a valid attribute 'size'

Todo:
    * size must be an integer, otherwise raise a TypeError exception with
    the message size must be an integer
    * if size is less than 0, raise a ValueError exception with the message
    size must be >= 0
"""


class Square:
    """
        Atrributes:
            __init__ (function): assign and validate attributes
            area (function): calculate area of square
    """
    def __init__(self, size=0):
        """
        Args:
            self (Square): object
            size (int): size of square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Args:
            self (Square): instance of class

        Return:
            area (int)
        """
        return (self.__size * self.__size)