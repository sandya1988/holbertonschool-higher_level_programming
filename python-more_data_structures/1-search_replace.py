#!/usr/bin/python3

"""
    /**
      * search_replace - replaces all occurrences by another in a new list
      * @my_list: List
      * @search: element to replace
      * @replace: new element
      *
      * Return: new List
      */
"""


def search_replace(my_list, search, replace):
    return [replace if item == search else item for item in my_list]