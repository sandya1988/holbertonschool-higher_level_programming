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
    * Private instance attribute: position
        * property 'def position(self)': to retrieve it
        * property setter 'def position(self, value)': to set it
    * Public instance method: 'def area(self)' that returns the current
    square area
    * Public instance method: def my_print(self): that prints in stdout the
    square with the character #
"""


class Square:
    """
        Atrributes:
            __init__ (function): assign and validate attributes
            area (function): calculate area of square
            my_print (function): print 2D of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            self (Square): object
            size (int): size of square
            position (tuple): print coordinates
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        size getter

        Returns:
            int: size of Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is -ve
        """
        if isinstance(value, int) is False:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """
        position getter

        Returns:
            tuple: Size of Square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        position setter

        Args:
            value (tuple): New Square position

        Raises:
            TypeError: if value is not a tuple and elements are not integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Args:
            self (Square): instance of class
        Return:
            area (int)
        """
        return (self.size * self.size)

    def my_print(self):
        """
        Print the Square to stdout using '#'
        """
        if self.size == 0:
            print()
        else:
            if self.position[1] > 0:
                for i in range(self.position[1]):
                    print('\n', end="")
            for i in range(self.size):
                print("{}{}".format(' ' * self.position[0], '#' * self.size))