#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'Assign' function below.
#
# The function accepts following parameters:
#  1. INTEGER i
#  2. FLOAT f
#  3. STRING s
#  4. BOOLEAN b
#

def Assign(i, f, s, b):
    # Write your code here
    w=i
    x=f
    y=s
    z=b
    print(w)
    print(x)
    print(y)
    print(z)
    
    print(dir())
    

if __name__ == '__main__':

    i = int(input().strip())

    f = float(input().strip())

    s = input()

    b = input().strip()
    
    Assign(i, f, s, b)