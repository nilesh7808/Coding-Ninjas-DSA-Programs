def partition(arr,start,end):
    pivot = arr[start]
    #Now find the number of elements smaller than pivot
    c = 0
    for i in range(start, end + 1):
        if arr[i] < pivot:
            c = c + 1
    arr[start + c],arr[start] = arr[start],arr[start + c]
    pi = start + c
    i = start
    j = end
    while i < j:
        if arr[i] < pivot :
            i = i + 1
        elif arr[j] >= pivot:
            j = j - 1
        else:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j -= 1
    return pi

def quickSort(arr, start, end):
    # Please add your code here
    if start >= end:
        return
    pi = partition(arr, start, end)
    quickSort(arr, start, pi - 1)
    quickSort(arr, pi + 1, end)
    pass


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, len(arr)-1)
print(*arr)
