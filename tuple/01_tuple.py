tuple=(1,2,3,4,5)

print(tuple)

print(tuple[2])

#  we can not update the value at any index when it is declared

tuple[2]=10

'''
    tuple[2]=10
    ~~~~~^^^
TypeError: 'tuple' object does not support item assignment
'''

# print(tuple)