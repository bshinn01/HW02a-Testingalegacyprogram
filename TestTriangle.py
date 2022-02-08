# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInvalidTriangles(self):
        self.assertEqual(classifyTriangle(1, 2, 4), 'NotATriangle', '1,2,4 is Not a Triangle')
        self.assertEqual(classifyTriangle(4, 2, 1), 'NotATriangle', '4,2,1 is Not a Triangle')
        self.assertEqual(classifyTriangle(2, 4, 1), 'NotATriangle', '2,4,1 is Not a Triangle')
        self.assertEqual(classifyTriangle(-1, -1, -1), 'NotATriangle', '-1,-1,-1 is Not a Triangle')

    def testRightTriangle(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right Triangle')
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right Triangle')
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right', '4,5,3 is a Right Triangle')
        self.assertEqual(classifyTriangle(10, 6, 8), 'Right', '10,6,8 is a Right Triangle')
        self.assertEqual(classifyTriangle(12, 20, 16), 'Right', '12,20,16 is a Right Triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 is an Equilateral Triangle')
        self.assertEqual(classifyTriangle(100, 100, 100), 'Equilateral', '100,100,100 is an Equilateral Triangle')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(3, 6, 5), 'Scalene', '3,6,5 is a Scalene Triangle')
        self.assertEqual(classifyTriangle(10, 8, 5), 'Scalene', '10,8,5 is a Scalene Triangle')
        self.assertEqual(classifyTriangle(3, 5, 7), 'Scalene', '3,5,7 is a Scalene Triangle')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles', '2,2,3 is a Isosceles Triangle')
        self.assertEqual(classifyTriangle(5, 3, 3), 'Isosceles', '5,3,3 is a Isosceles Triangle')
        self.assertEqual(classifyTriangle(7, 13, 7), 'Isosceles', '7,13,7 is a Isosceles Triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

