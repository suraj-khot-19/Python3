#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'find' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER num1
#  2. INTEGER num2
#  3. INTEGER num3
#

def find(num1, num2, num3):
    # Write your code here
    print(f"{num1<num2 and num2>=num3} {num1>num2 and num2<=num3} {num3==num1 and num1!=num2}")

if __name__ == '__main__':

    num1 = int(input().strip())

    num2 = int(input().strip())

    num3 = int(input().strip())

    find(num1, num2, num3)

