def geometricSum(n):
    if n == 0:
        return (1/(2 ** n))

    a = geometricSum(n - 1)
    s = (a + (1/(2 ** n)))
    return s

from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
print(geometricSum(n))