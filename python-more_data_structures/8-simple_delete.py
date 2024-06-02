#!/usr/bin/python3

"""
    /**
      * simple_delete - delete by key
      * @a_dictionary: dictionary
      * @key: key to be deleted
      *
      * Return: dictionary
      */
"""


def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key):
        del a_dictionary[key]
    return a_dictionary