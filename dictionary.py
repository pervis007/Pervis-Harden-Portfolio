studentGrades = {"Ben":92, "Diane":97,"Sam":81}
print(studentGrades["Diane"])
print(studentGrades["Sam"])
print(studentGrades["Ben"])


myCar = ({"Make": "Ford", "Model": "Mustang GT500","Year": 2022,"colors":("Blue","Grey")},
        {"Make": "Ford", "Model": "Mustang GT","Year": 2018,})


print(myCar[0]["colors"][1])


print(myCar[0]["Model"])

for item in studentGrades:
    print(studentGrades[item])

if "Ben" in studentGrades:
    print("It is!")

if 92 in studentGrades.values():
    print("92 gang!")


print(studentGrades.values())


values = studentGrades.values()
valuesList = list(values)
print(valuesList)
print(valuesList[1])

keys = studentGrades.keys()
keysList = list(keys)
print(keys)
print(keysList)

for i in range(0,len(values)):
    print(studentGrades[keysList[i]])


items = studentGrades.items()
print(items)

itemsList = list(items)
print(itemsList[0])
print(itemsList[0][0])

