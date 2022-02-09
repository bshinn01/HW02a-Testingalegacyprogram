# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: bss
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # Test Invalid Triangles ----------------------------------------------------------------
    def testInvalidTriangles1(self):
        self.assertEqual(classifyTriangle(1, 2, 4), 'NotATriangle', '1,2,4 is Not a Triangle')

    def testInvalidTriangles2(self):
        self.assertEqual(classifyTriangle(4, 2, 1), 'NotATriangle', '4,2,1 is Not a Triangle')

    def testInvalidTriangles3(self):
        self.assertEqual(classifyTriangle(2, 4, 1), 'NotATriangle', '2,4,1 is Not a Triangle')

    # Test Right Triangles -----------------------------------------------------------------
    def testRightTriangle1(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right Triangle')

    def testRightTriangle2(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right Triangle')

    def testRightTriangle3(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right', '4,5,3 is a Right Triangle')

    def testRightTriangle4(self):
        self.assertEqual(classifyTriangle(10, 6, 8), 'Right', '10,6,8 is a Right Triangle')

    def testRightTriangle5(self):
        self.assertEqual(classifyTriangle(12, 20, 16), 'Right', '12,20,16 is a Right Triangle')

    # Test Equilateral Triangles -------------------------------------------------------------
    def testEquilateralTriangles1(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 is an Equilateral Triangle')

    def testEquilateralTriangles2(self):
        self.assertEqual(classifyTriangle(100, 100, 100), 'Equilateral', '100,100,100 is an Equilateral Triangle')

    # Test Scalene Triangles -----------------------------------------------------------------
    def testScaleneTriangles1(self):
        self.assertEqual(classifyTriangle(3, 6, 5), 'Scalene', '3,6,5 is a Scalene Triangle')

    def testScaleneTriangles2(self):
        self.assertEqual(classifyTriangle(10, 8, 5), 'Scalene', '10,8,5 is a Scalene Triangle')

    def testScaleneTriangles3(self):
        self.assertEqual(classifyTriangle(3, 5, 7), 'Scalene', '3,5,7 is a Scalene Triangle')

    # Test Isosceles Triangles ---------------------------------------------------------------
    def testIsoscelesTriangles1(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles', '2,2,3 is a Isosceles Triangle')

    def testIsoscelesTriangles2(self):
        self.assertEqual(classifyTriangle(5, 3, 3), 'Isosceles', '5,3,3 is a Isosceles Triangle')

    def testIsoscelesTriangles3(self):
        self.assertEqual(classifyTriangle(7, 13, 7), 'Isosceles', '7,13,7 is a Isosceles Triangle')

    # Test Invalid Inputs -------------------------------------------------------------------------
    def testInvalidInputs1(self):
        self.assertEqual(classifyTriangle(-1, -1, -1), 'InvalidInput', '-1,-1,-1 is an Invalid Input')

    def testInvalidInputs2(self):
        self.assertEqual(classifyTriangle(201, 1, 1), 'InvalidInput', '200, 1, 1 is an Invalid Input')

    def testInvalidInputs3(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', '0, 0, 0 is an Invalid Input')

    def testInvalidInputs4(self):
        self.assertEqual(classifyTriangle('a', 'b', 'c'), 'InvalidInput', 'a,b,c is an Invalid Input')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

