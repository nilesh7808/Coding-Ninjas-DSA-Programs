sum = 0
def sumArray(arr):
    # Please add your code here
    sum = 0
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sumArray(arr[1:])
    pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))