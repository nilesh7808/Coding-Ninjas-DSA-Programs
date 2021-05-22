def n_to_1(n):
    if n == 0:
        return
    print(n)
    n_to_1(n-1)
    return
n = int(input())
n_to_1(n)