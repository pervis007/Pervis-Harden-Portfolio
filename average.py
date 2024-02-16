import fileinput

studentGrades = {}
total = 0
for line in fileinput.input():
    value = line.strip()
    value = value.split(",")

    studentGrades.update({value[0] : int(value[1])})

print(studentGrades)

for student in studentGrades:
    total = total + studentGrades[student]
 
average = total / len(studentGrades)
 
print(f"The average is: {average}")