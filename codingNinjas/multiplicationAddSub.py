def multiPlication(m, n):
    if n == 0:
        return 0

    ans = m * ( n - 1)
    return ans + m

m = int(input())
n = int(input())
print(multiPlication(m,n))