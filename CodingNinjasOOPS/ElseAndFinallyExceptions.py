class ZeroDenominatorError(ZeroDivisionError):
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
    except ValueError:
        print("Numerator and Denominator should be Interger")
    except ZeroDenominatorError:                    # Whatever come first They will served first
        print("ZeroDenominatorError is raised")
    except ZeroDivisionError:
        print("Denominator with Zero not be allowed .")
    except:
        print("Some Unknown Error has been Found ")
    else:
        print(value)
        break
    finally:
        print(num)
        print(denom)
        print(value)        # whatever come in the sequence they will get printed first
        print("Hey! There may be exception or may not be exceptions")