def isSorted(arr):
    l = len(arr)
    if l == 0 or l == 1:
        return True
    if arr[0] > arr[1]:
        return False
    smallerList = arr[1:]
    isSmallerListSorted = isSorted(smallerList)
    if isSmallerListSorted:
        return True
    else:
        return False
arr = [1,2,3,4,5,6,7,8,9]
print(isSorted(arr))