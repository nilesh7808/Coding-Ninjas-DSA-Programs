def pairStar(n):

    if len(n) == 0 or len(n) == 1:
        return n

    if n[0] == n[1]:
        smallerOutput = pairStar(n[1:])
        return n[0] + "*" + smallerOutput
    else:
        smallerOutput = pairStar(n[1:])
        return n[0] + smallerOutput
n = input()
print(pairStar(n))