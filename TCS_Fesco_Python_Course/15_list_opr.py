'''
Basic List Operations 
Write the function definition for the function 'List_Op' which takes 2 parameters 'Mylist' and 'Mylist2' both of which are LIST of INTEGERS 
Do as per the following to get the expected output: 
1.Print 'Mylist' 
2.Print the 2nd element of 'Mylist' 
3.Print the Last element of 'Mylist' 
4.Add '3' as the Last element of 'Mylist' 
5.Change the 4th element of 'Mylist' into '60' 
6.Print 'Mylist' again 
7.Print from the '2nd' element to the '5th' element of 'Mylist' 
8. Append 'Mylist2' to 'Mylist' 
9.Print 'Mylist' again 
10.Extend 'Mylist' using 'Mylist2' 
11.Print 'Mylist' again 
12. Remove the Last element of 'Mylist' 
13.Print 'Mylist' again 
14.Print 'Length' of 'Mylist'  
'''

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'List_Op' function below.
#
# The function accepts following parameters:
#  1. LIST Mylist
#  2. LIST Mylist2
#

def List_Op(Mylist, Mylist2):
    print(Mylist)
    print(Mylist[1])
    print(Mylist[-1])
    Mylist.append(3)
    Mylist[3] = 60
    print(Mylist)
    print(Mylist[1:5])
    Mylist.append(Mylist2)
    print(Mylist)
    Mylist.extend(Mylist2)
    print(Mylist)
    Mylist.pop()
    print(Mylist)
    print(len(Mylist))


if __name__ == '__main__':
    qw1_count = int(input().strip())

    qw1 = []

    for _ in range(qw1_count):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)

    qw2_count = int(input().strip())

    qw2 = []

    for _ in range(qw2_count):
        qw1_item = int(input().strip())
        qw2.append(qw1_item)

    List_Op(qw1,qw2)