#!/bin/python3

import math



#
# Complete the 'calc' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER c as parameter.
#

def calc(c):
    # Write your code here
    radius=c/(2*math.pi)
    area=math.pi*radius*radius
    
    return (round(radius,2),round(area,2))

if __name__ == '__main__':
    c = int(input().strip())

    result = calc(c)

    print(result)
