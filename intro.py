import Circle

c1 = Circle.Circle(14)

print(c1.__dir__())

if "color" in c1.__dir__():
    print("Yea it was found!")
else:
    ("Nope!")


print(c1.__ne__)

