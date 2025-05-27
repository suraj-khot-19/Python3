# string are immutable but list are mutable 
 
str="suraj"

print(str) # suraj

print(str[2]) # r

# str[2]="k" # check it lol

'''
Traceback (most recent call last):
  File "d:\python\list\04_diff_string_list.py", line 5, in <module>
    str[2]="k"
    ~~~^^^
TypeError: 'str' object does not support item assignment
'''


list=[1,2,3]

print(list) # [1, 2, 3]

print(list[2]) # 3

list[2]=10

print(list) # [1, 2, 10]