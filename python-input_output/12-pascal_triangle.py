#!/usr/bin/python3
"""fonction"""


def pascal_triangle(n):
    """fonction"""
    if n <= 0:
        return []

    """fonction"""
    triangle = [[1]]

    for i in range(1, n):
        """fonction"""
        prev_row = triangle[-1]
        """fonction"""
        new_row = [1] + [prev_row[j] + prev_row[j + 1]
                         for j in range(len(prev_row) - 1)] + [1]
        triangle.append(new_row)

    return triangle
