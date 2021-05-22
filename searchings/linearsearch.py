pos = 0
def search(arr,n):
    for i in range(len(arr)):
        if arr[i] == n:
            globals()['pos'] = i
            return True
    return False
arr = list(map(int,input().split()))
n = int(input("Enter number to be searched "))
if search(arr,n):
    print("Found at",pos+1)
else:
    print("Not Found")
