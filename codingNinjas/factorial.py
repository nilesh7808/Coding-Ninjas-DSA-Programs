def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
import sys
sys.setrecursionlimit(4000)
n = int(input())
print(fact(n))