def firstIndex(arr, x):
    # Please add your code here
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == x:
        return 0
    newArr = arr[1:]
    isfirstOccur = firstIndex(newArr, x)
    if isfirstOccur == -1:
        return -1
    else:
        return isfirstOccur + 1
    pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x))
