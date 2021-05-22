# Single Error Handling and multiple Error Handling or Exception

while True:
    try:
        n = input("Enter Numerator : ")
        num = int(n)
        n = input("Enter Denominator : ")
        denom = int(n)

        value = num/denom
        print(value)
        break
    except ValueError:
        print("Numerator and Denominator should be integers")
    except ZeroDivisionError:
        print("Denominator shouldn't be Zero")