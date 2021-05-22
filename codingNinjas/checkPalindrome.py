def checkPalindrome(s, si, li):
    if si > li:
        return True

    if s[si] == s[li]:
        smallerList = checkPalindrome(s, si+1, li -1)
        if smallerList:
            return True
        else:
            return False
    return False
from sys import setrecursionlimit
setrecursionlimit(11000)
s = input()
if (checkPalindrome(s, 0, len(s) - 1)) == True:
    print("true")
else:
    print("false")
