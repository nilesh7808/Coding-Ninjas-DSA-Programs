def isSortedBetter(arr,si):
    l = len(arr)
    if si == l-1 or si == l:
        return True
    if arr[si] > arr[si + 1]:
        return False
    isSmallerlistSorted = isSortedBetter(arr, si + 1)
    return isSmallerlistSorted
arr = list(map(int,input().split()))
print(isSortedBetter(arr,0))
