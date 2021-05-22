def removeChar(s,a):
    if len(s) == 0:
        return s
    newS = s[1:]
    smallOutput = removeChar(newS, a)

    if s[0] == a:
        return smallOutput
    else:
        return s[0] + smallOutput

s = input()
a = input()
print(removeChar(s, a))