def Stair_case(n):
    if n == 0  or n == 1:
        return 1
    elif n == 2 :
        return 2
    elif n == 3:
        return 4
    else :
        return Stair_case(n-1) + Stair_case(n-2) +Stair_case(n-3)

from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
print(Stair_case(n))