# slicing [x:y] where y is excluded

data=["suraj","tcs",1.9,1,True,"fucking life", "no hopes"]

print(data) # data=["suraj","tcs",1.9,1,True,"fucking life", "no hopes"]

print(data[1:4]) # ['tcs', 1.9, 1]

print(data[6:0]) # []
