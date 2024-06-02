#!/usr/bin/python3

"""
    /** uniq_add - adds all unique integers in a list once for each integer
      * @my_list: list
      *
      * Return: integer
      */
"""


def uniq_add(my_list=[]):
    add = 0
    for s in set(my_list):
        add += s
    return (add)