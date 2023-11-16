#!/usr/bin/env python

"""
Author: Asher Downs
File: triangle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape.
"""

from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Triangle shape, and contains values for 3 sides (x, y, z).
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def area(self):
        """
        Compute the area using Heron's Formula
        """
        # s for semi-perimeter
        s = (self.x + self.y + self.z) / 2
        # a for area
        a = (s*(s-self.x)*(s-self.y)*(s-self.z)) ** 0.5
        return a

    def perimeter(self):
        """
        Compute the perimeter adding all 3 sides
        """
        return self.x + self.y + self.z

    def is_equilateral(self):
        """
        Determine if the triangle is equilateral by comparing the value of all 3 sides
        """
        return (self.x == self.y) and (self.y == self.z)