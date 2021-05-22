def strToInteger(s):
    if s == 0:
        return
    return int(s)

from sys import setrecursionlimit
setrecursionlimit(11000)
s = input()
print(strToInteger(s))