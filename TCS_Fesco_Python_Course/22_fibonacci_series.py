#!/bin/python3
#
# Complete the 'sumOfNFibonacciNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def sumOfNFibonacciNumbers(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    n1 = 0
    n2 = 1
    total = 1

    for i in range(2, n):
        temp = n1 + n2
        total += temp
        n1 = n2
        n2 = temp

    return total
if __name__ == '__main__':

    n = int(input().strip())

    result = sumOfNFibonacciNumbers(n)
    print(result)
