"""
Author: Nick Russo
File: triangle_test.py
Purpose: Unit tests for the Triangle class.
"""

from unittest import TestCase
from shapes.triangle import Triangle


class TriangleTest(TestCase):
    """
    Defines a test case for the Triangle class.
    """

    def setUp(self):
        """
        Create a few test objects.
        """
        self.x6y3z4 = Triangle(6, 3, 4)
        self.x5y5z5 = Triangle(5, 5, 5)


    def test_area(self):
        """
        Compare the test triangle area computations to the actual values.
        """
        self.assertEqual(self.x6y3z4.area(), 5.33)
        self.assertEqual(self.x5y5z5.area(), 10.83)

    def test_perimeter(self):
        """
        Compare the test triangle perimeter computations to the actual values.
        """
        self.assertEqual(self.x6y3z4.perimeter(), 13)
        self.assertEqual(self.x5y5z5.perimeter(), 15)