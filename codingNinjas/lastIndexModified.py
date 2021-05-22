def lastIndex(arr,x,li):
    n = len(arr)
    if li == n:
        return -1
    newLastIndex = lastIndex(arr,x,li + 1)
    if newLastIndex != -1:
        return newLastIndex
    else:
        if arr[li] == x:
            return li
        else:
            return -1
from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split())
x = int(input())
print(lastIndex(arr,x,0))
