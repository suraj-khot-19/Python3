#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'Integer_Math' function below.
#
# The function accepts following parameters:
#  1. INTEGER Side
#  2. INTEGER Radius
#

def Integer_Math(Side, Radius):
    pi = 3.14  

    print(f"Area of Square is {round(Side * Side, 2)}")
    print(f"Volume of Cube is {round(Side ** 3, 2)}")
    print(f"Area of Circle is {round(pi * Radius ** 2, 2)}")
    print(f"Volume of Sphere is {round((4 / 3) * pi * Radius ** 3, 2)}")
if __name__ == '__main__':
    Side = int(input().strip())

    Radius = int(input().strip())

    Integer_Math(Side, Radius)