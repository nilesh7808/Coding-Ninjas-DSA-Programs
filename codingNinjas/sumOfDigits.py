def sumOfDigits(n):
    if n == 0:
        return 0
    return (n % 10) + sumOfDigits(n // 10)
n = int(input())
print(sumOfDigits(n))