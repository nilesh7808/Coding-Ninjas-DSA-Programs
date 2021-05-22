
def sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(0,len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
arr = list(map(int,input().split()))
sort(arr)
print(arr)