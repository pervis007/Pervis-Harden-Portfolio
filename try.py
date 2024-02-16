
while True:
    try:
        value1 = input("Enter Value 1: ")
        value1 = int(value1)

        value2 = input("Enter Value 2: ")
        value2 = int(value2)
        
        break
    except:
        print("The value entered is invalid.")

try:
    print(value1 / value2)
except ZeroDivisionError:
    print("Cannot use 0 young bull")
    raise ZeroDivisionError
except:
    print("There was an error in the division.")