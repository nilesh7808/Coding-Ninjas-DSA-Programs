class ZeroDenominatorError(Exception):
    pass
while True:
    try:
        n = input("Enter Numerator: ")
        num = int(n)
        n = input("Enter the Denominator: ")
        denom = int(n)
        if denom == 0:
            raise ZeroDenominatorError("Denominator Should not be Zero")
        value = num / denom
        print(value)
        break

    except ValueError:
        print("Numerator and Denominator should be Interger")
    except ZeroDivisionError:
        print("Denominator should not be zero.")
    except NameError:
        print("Name is not defined. ")
    except ZeroDenominatorError:
        print("ZeroDenominatorError is raised")