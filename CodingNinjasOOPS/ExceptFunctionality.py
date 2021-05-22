class ZeroDenominatorError(ZeroDivisionError):  # Whatever come first They will served first due to the inheritation
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
    except ZeroDenominatorError:                    # Whatever come first They will served first
        print("ZeroDenominatorError is raised")
    except ZeroDivisionError:
        print("Denominator with Zero not be allowed .")
    except:
        print("Some Unknown Error has been Found ")