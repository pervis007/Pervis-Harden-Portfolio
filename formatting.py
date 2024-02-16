name = "Pervis"
age = 27

print("Hello",name,"," , "you","are",age,"years","old!") #not formatted

print("Hello %s, you are %s years old!" % (name,age)) # percent formatting

print("Hello {0}, you are {1} years old!".format(name,age)) #string formatting (name 0range, age 1range)

print(f"Hello {name}, you are {age} years old!") #f string. Recommended way to format

print(f"Hello {name}, you will be {age + 10} years old in 10 years!") #you can do operations inside of the f strings


message = (   
    f"Hello {name}, "
    f"you are {age} years old. "
    f"In ten years you will be {age + 10} years old."
)

print(message)