#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sliceit' function below.
#
# The function accepts List mylist as parameter.
#

def sliceit(mylist):
    # Write your code here
    print(mylist[1:3])    # secound and third element
    print(mylist[1::2]) # odd indexed elements
    print(mylist[:-4:-1]) # last three elements in revese order
if __name__ == '__main__':
    mylist_count = int(input().strip())

    mylist = []

    for _ in range(mylist_count):
        mylist_item = input()
        mylist.append(mylist_item)

    sliceit(mylist)
