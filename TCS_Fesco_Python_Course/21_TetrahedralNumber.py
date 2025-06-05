#!/bin/python3

'''
Python - While (Tetrahedral Number) 
A number is termed as a tetrahedral number if it can be represented as a pyramid with a triangular base and three sides, called a tetrahedron. The nth tetrahedral number is the sum of the first n triangular number. 
1 
4 
10 
20 
The first five tetrahedral numbers are: 1, 4, 10, 20, 35 
The formula for the nth tetrahedral number is: 
Tn = n(n+1)(n+2) 6 
Define a function called 
calculateNTetrahedralNumber' which takes two parameters. The first parameter is 'startvalue and the next parameter is endvalue.startvalue and endvalue both are inclusive in the range. The function definition code stub is given in the editor. Calculate tetrahedral numbers for all n numbers given in a range, store into the list, and return it.
'''
import math
import os
import random
import re
import sys



#
# Complete the 'calculateNTetrahedralNumber' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER startvalue
#  2. INTEGER endvalue
#

def calculateNTetrahedralNumber(startvalue, endvalue):
    result = []
    for n in range(startvalue, endvalue + 1):
        tetrahedral = (n * (n + 1) * (n + 2)) // 6 
        result.append(tetrahedral)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    startvalue = int(input().strip())

    endvalue = int(input().strip())

    result = calculateNTetrahedralNumber(startvalue, endvalue)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
