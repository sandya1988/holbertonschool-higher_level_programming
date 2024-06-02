#!/usr/bin/python3

"""
    /** square_matrix_simple - computes the square value of integers in matrix
      * @matrix: 2 dimensional matrix
      *
      * Return: matrix
      */
"""


def square_matrix_simple(matrix=[]):
    return list(map(lambda m: list(map(lambda y: y**2, m)), matrix))