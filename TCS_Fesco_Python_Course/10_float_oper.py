#!/bin/python3

import math



#
# Complete the 'tria' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. FLOAT n1
#  2. FLOAT n2
#  3. INTEGER n3
#

def triangle(n1, n2, n3):
    area = round((n1 * n2) / 2,n3)
    pi_rounded = round(math.pi, n3)
    return (area, pi_rounded)

if __name__ == '__main__':
    
    n1 = float(input().strip())

    n2 = float(input().strip())

    n3 = int(input().strip())

    result = triangle(n1, n2, n3)

    print(result)