#!/usr/bin/python3

"""
    /**
      * update_dictionary - eplaces or adds key/value in a dictionary
      * @a_dictionary: dictionary
      * @key: key
      * @value: value
      *
      * Return: dictionary
      */
"""


def update_dictionary(a_dictionary, key, value):
    a_dictionary.update([(key, value)])
    return a_dictionary