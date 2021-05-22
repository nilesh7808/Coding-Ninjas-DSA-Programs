def firstIndex(arr, x,k):
    # Please add your code here
    n = len(arr)
    if n == 0:
        return 0
    if arr[k] == x :
        return k
    return firstIndex(arr,x,k+1)
    pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x,0))
