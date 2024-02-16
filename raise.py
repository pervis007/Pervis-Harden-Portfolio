value1 = int(input("Enter Value 1: "))
value2 = input("Enter Value 2: ")

assert(value2 != "0"), "Value 2 cannot be zero."

# if value2 == "0":
#     raise Exception("The value 2 value cannot be zero.")
value2 = int(value2)
print(value1 / value2)
