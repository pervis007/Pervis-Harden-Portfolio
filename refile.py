import fileinput #get access to fileinput library

for line in fileinput.input(): #creating a reference to the fileinput function
    print(line)