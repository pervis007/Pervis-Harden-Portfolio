

studentNames = ["Ben","Diane","Sam","Pat"]
print(studentNames)
print(studentNames[2])
for name in studentNames:
    print(name)

studentNames.append("Joe")
print(studentNames)
studentNames.remove("Diane")
print(studentNames)


studentTuple = ("Lori","Kate","David")
print(studentTuple[1])

studentSet = {"Alan","Steven","Bridget"}
print(studentSet)

for name in studentSet:
    print(name)