list=[43,12,-90,120,33]

print("list before sorting :",list) # list before sorting : [43, 12, -90, 120, 33]

list.sort()

print("list after sorting :",list) # list after sorting : [-90, 12, 33, 43, 120]

list.sort(reverse=True)

print("list after reverse sorting :",list) # list after reverse sorting : [120, 43, 33, 12, -90]