def binarySearch(arr, x, si, li):
    if si > li :
        return -1
    mid = (si + li)// 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binarySearch(arr, x, si, mid - 1)
    else:
        return binarySearch(arr, x, mid + 1, li)
arr = list(int(i) for i in input().split())
x = int(input())
print(binarySearch(arr, x, 0, len(arr)-1))