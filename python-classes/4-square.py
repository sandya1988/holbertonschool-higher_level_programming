#!/usr/bin/python3

"""
A script that creates a class and validates its given attribute
Attributes:
    Square (class): with a valid attribute 'size'

Todo:
    * Private instance attribute: size
    * property setter def 'size(self, value)' to set it
    * size must be an integer, otherwise raise a 'TypeError' exception with
    the message size must be an integer
    * if size is less than 0, raise a 'ValueError' exception with the message
    size must be >= 0
    * Public instance method: 'def area(self)' that returns the current
    square area
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
        self.__size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Args:
            self (Square): instance of class
        Return:
            area (int)
        """
        return (self.__size * self.__size)