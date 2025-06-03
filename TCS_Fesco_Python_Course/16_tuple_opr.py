'''
Python - List Operations 2 
Define a function called 'tuplefunction' which takes four parameters. 
The first parameter is list¹ which takes a list of integers 
The second parameter is list2 which takes a list of strings 
The third parameter is string1 which takes a string 
The fourth parameter is n which takes an integer 
The function definition code stub is given in the editor. 
Generate the print statements based on condition given below: 
convert the lists (list1, list2) into tuples and store them as tuple1 and tuple2. 
concatenate tuple1 and tuple2 and print the concatenated tuple. 
print the 4th index in the concatenated tuple. 
create a nested tuple out of the two tuples (tuple1 and tuple2). 
print the length of the nested tuple. 
create a tuple with repetition of the string string1, n number of times and print the tuple 
print the maximum of tuple tuple1.   
'''

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'tuplefun' function below.
#
# The function accepts following parameters:
#  1. LIST list1
#  2. LIST list2
#  3. STRING string1
#  4. INTEGER n
#

def tuplefunction(list1, list2, string1, n):
    tuple1 = tuple(list1)
    tuple2 = tuple(list2)
    concat_tuple = tuple1 + tuple2
    print(concat_tuple)
    print(concat_tuple[4])
    nested_tuple = (tuple1, tuple2)
    print(nested_tuple)
    print(len(nested_tuple))
    repeated_tuple = (string1,) * n
    print(repeated_tuple)
    print(max(tuple1))


if __name__ == '__main__':
    
    qw1_count = int(input().strip())

    qw1 = []

    for _ in range(qw1_count):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)

    qw2_count = int(input().strip())

    qw2 = []

    for _ in range(qw2_count):
        qw1_item = input()
        qw2.append(qw1_item)
        
    str1 = input()

    n = int(input().strip())

    tuplefunction(qw1,qw2,str1, n)
