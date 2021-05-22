pos = 0
def search(arr,n):
    beg = 0
    end = len(arr)-1
    for i in range(len(arr)):
        mid = (beg+end)//2
        if arr[mid] == n:
            globals()['pos']=i
            return True
        else:
            if arr[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False
arr = list(map(int,input().split()))
arr = arr.sort()
n = int(input("Enter Number to be searched "))
if search(arr,n):
    print("Found at",pos+1)
else:
    print("No element Found.")