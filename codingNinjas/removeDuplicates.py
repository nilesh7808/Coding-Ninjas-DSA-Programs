def removeDuplicates(s):
    n = len(s)
    if n == 0 or n == 1:
        return s
    if s[0] == s[1]:
        smallOutput = removeDuplicates(s[1:])
        return smallOutput
    else:
        smallOutput = removeDuplicates(s[1:])
        return  s[0] + smallOutput
s = input()
print(removeDuplicates(s))