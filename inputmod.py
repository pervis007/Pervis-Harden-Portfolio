import csv


def readEmployeeFile():
    employees = []
    employeeFile = open('names.txt',mode= 'r')

    csvReader = csv.DictReader(employeeFile)


    for row in csvReader:
        employees.append(row)

    return employees

if __name__ == "__main__":
    print(readEmployeeFile())