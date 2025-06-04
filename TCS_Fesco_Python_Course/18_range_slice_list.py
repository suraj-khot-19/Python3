#!/bin/python3

import math
import os
import random
import re
import sys

'''
Print the first three continuous numbers from the given range. 
Print the last five continuous numbers in the reverse order from the given range. 
Print every 4th element from the given range. 
Print every 2nd element in decreasing order from the given range.   
'''

#
# Complete the 'generateList' function below.
#
# The function accepts following parameters:
#  1. INTEGER startvalue
#  2. INTEGER endvalue
#

def generateList(startvalue, endvalue):
    numbers = list(range(startvalue, endvalue + 1))
    print(numbers[:3])
    print( numbers[-5:][::-1])
    print(numbers[::4])
    print(numbers[::-2])
if __name__ == '__main__':
    startvalue = int(input().strip())

    endvalue = int(input().strip())

    generateList(startvalue, endvalue)
