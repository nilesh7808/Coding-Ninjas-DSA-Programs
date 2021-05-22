def sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i,len(arr)):
            if arr[j] < arr[min]:
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
arr = list(map(int,input().split()))
sort(arr)
print(arr)