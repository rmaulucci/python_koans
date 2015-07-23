#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    try:
        pretest(a,b,c)
        test_1 = set([a,b,c])
        if len(test_1) == 1:
            return 'equilateral'
        elif len(test_1) == 2:
            return 'isosceles'
        else:
            return 'scalene'
    except StandardError:
        raise TriangleError
    
def pretest(a, b, c):
    pretest_1 = [a,b,c]
    pretest_1.sort()
    cond_1 = (pretest_1[0] + pretest_1[1]) > pretest_1[2]
    cond_2 = (sum(x > 0 for x in pretest_1) == len(pretest_1)) 

    if cond_1 and cond_2:
        return True
    else:
        raise StandardError

class TriangleError(StandardError):
    pass
