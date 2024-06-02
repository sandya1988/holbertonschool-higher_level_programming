#!/usr/bin/python3

"""
    /** only_diff_elements - returns set of elements present in only one set
      * @set_1: set
      * @set_2: set
      *
      * Return: set
      */
"""


def only_diff_elements(set_1, set_2):
    return (set_1 ^ set_2)