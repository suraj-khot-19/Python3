length=int(input("Enter list size:"))

list=[]

for i in range(length):
    list.append(int(input(f"Enter {i} th element of list :")))

listCopy=list[:]

list.reverse()

listReverse=list

if listCopy == listReverse :
    print("Palindrome")
else:
    print("Not Palindrome")