#!/usr/bin/python3

"""
    /**
      * multiply_by_2 - multiply dictionary values by 2
      * @a_dictionary: dictionary
      *
      * Return: dictionary
      */
"""


def multiply_by_2(a_dictionary):
    return {x: y*2 for x, y in a_dictionary.items()}