def countZeros(n):
    if n == 0:
        return 0

    smallerOutput = countZeros(n // 10)

    if n % 10 == 0:
        return 1 + smallerOutput

    else:
        return smallerOutput


import sys

sys.setrecursionlimit(11100000)
n = int(input())
print(countZeros(n))
