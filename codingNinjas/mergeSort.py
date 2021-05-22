def merge(arr1,arr2,arr):
    i = 0
    j = 0
    k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr[k] = arr2[j]
            k = k + 1
            j = j + 1
    while i < len(arr1):
        arr[k] = arr1[i]
        k = k + 1
        i = i + 1

    while j < len(arr2) :
        arr[k] = arr2[j]
        k = k + 1
        j = j + 1

def mergeSort(arr,start,end):
    l = len(arr)
    mid = (0+l) // 2
    if mid == 0:
        return

    arr1 = arr[0:mid]
    arr2 = arr[mid:]

    mergeSort(arr1,0,mid)
    mergeSort(arr2,mid,end)

    merge(arr1,arr2,arr)
# Main

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n)
print(*arr)