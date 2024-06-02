#!/usr/bin/python3

"""
    /** print_sorted_dictionary - prints a dictionary by ordered keys
      * @a_dictionary: dictionary
      *
      * Return: dictionary
      */
"""


def print_sorted_dictionary(a_dictionary):
    newdict = {}
    for item in sorted(a_dictionary):
        print("{}: {}".format(item, a_dictionary.get(item)))