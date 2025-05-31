#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'func' function below.
#
# The function is expected to print an INTEGER.
# The function accepts following parameters:
#  1. INTEGER startvalue
#  2. INTEGER endvalue
#  3. INTEGER stepvalue
#

def rangefunction(startvalue, endvalue, stepvalue):
    # Write your code here
    print(*[i**2 for i in range(startvalue,endvalue,stepvalue)])

if __name__ == '__main__':

    x = int(input().strip())

    y = int(input().strip())

    z = int(input().strip())

    rangefunction(x, y, z)
