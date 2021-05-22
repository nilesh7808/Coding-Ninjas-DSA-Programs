def lastIndex(arr,x):
    n = len(arr)
    if n == 0:
        return -1
    newArr = arr[1:]
    newLastIndex = lastIndex(newArr,x)
    if newLastIndex != -1:
        return newLastIndex + 1
    else:
       if arr[0] == x:
           return 0
       else:
           return -1
from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split())
x = int(input())
print(lastIndex(arr,x))
