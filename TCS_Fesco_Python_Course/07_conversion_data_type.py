#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'Integer_fun' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. FLOAT a
#  2. STRING b
#

def Integer_fun(a, b):
    # Write your code here
    c=int(a)
    d=int(b)
    
    print(type(a))
    print(type(b))
    print(c)
    print(d)
    print(type(c))
    print(type(d))
    
    
if __name__ == '__main__':
    a = float(input().strip())

    b = input()

    Integer_fun(a, b)