def checkNumber(arr, x):
    # Please add your code here
    if n == 0:
        return False
    if arr[0] == x:
        return True
    newArr = arr[1:]
    newCheckNumber = checkNumber(arr[1:],x)
    if newCheckNumber:
        return True
    else:
        return False
    pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
