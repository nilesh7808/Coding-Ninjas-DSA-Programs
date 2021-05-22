def checkAB(s):
    if s == 'a' or s == 'abb':
        return True

    if s[0] == 'a' and s[1] == 'a':
        return checkAB(s[1:])
    if s[0] == 'a' and s[1] == 'b' and s[2] == 'b' and s[3] == 'a':
        return checkAB(s[3:])

    return False


s = input()
if checkAB(s) == True:
    print("true")
else:
    print("false")