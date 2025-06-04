#!/bin/python3

import math
import os
import random
import re
import sys

'''
Find the union of 'seta and setb and return it. 
Find the intersection of 'seta' and 'setb and return it. 
Find the difference of 'seta and setb and return it. 
Find the difference of 'setb and seta' and return it. 
Find the symmetric difference of 'seta' and 'setb' and return it. 
Convert 'seta' list into frozenset, return it.   
'''


#
# Complete the 'setOperation' function below.
#
# The function is expected to return a union, intersection, difference(a,b), difference(b,a), symmetricdifference and frozen set.
# The function accepts following parameters:
#  1. List seta
#  2. List setb
#

def setOperation(seta, setb):
    # Write your code here
    set_a = set(seta)
    set_b = set(setb)
    
    union = set_a | set_b
    intersection = set_a & set_b
    difference_a_b = set_a - set_b
    difference_b_a = set_b - set_a
    symmetric_difference = set_a ^ set_b
    frozen_set_a = frozenset(seta)
    
    return union, intersection, difference_a_b, difference_b_a, symmetric_difference, frozen_set_a

if __name__ == '__main__':
    seta_count = int(input().strip())

    seta = []

    for _ in range(seta_count):
        seta_item = input()
        seta.append(seta_item)

    setb_count = int(input().strip())

    setb = []

    for _ in range(setb_count):
        setb_item = input()
        setb.append(setb_item)

    un, intersec, diffa, diffb, sydiff, frset = setOperation(seta, setb)
    print(sorted(un))
    print(sorted(intersec))
    print(sorted(diffa))
    print(sorted(diffb))
    print(sorted(sydiff))
    print("Returned value is {1} frozenset".format(frset, "a" if type(frset) == frozenset else "not a"))