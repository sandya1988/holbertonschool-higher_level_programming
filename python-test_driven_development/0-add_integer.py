#!/usr/bin/python3

"""
An integer addition module.
"""


def add_integer(a, b=98):
    """
    Adds to intgers/floats
    Float parameters are typecasted to int before operated upon.

    Returns:
        sum (int): Addition of a and b

    Raises:
        TypeError: if either a or b is a not an integer neither float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))