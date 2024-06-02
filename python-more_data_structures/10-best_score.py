#!/usr/bin/python3

"""
    /** best_score - returns a key with the biggest integer value
      * @a_dictionary: dictionary
      *
      * Return: string or None
      */
"""


def best_score(a_dictionary):
    key = None
    if a_dictionary:
        for idx, item in a_dictionary.items():
            if item > a_dictionary.get(key, 0):
                key = idx
    return (key)