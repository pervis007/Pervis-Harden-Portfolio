name1 = "Pervis" 
name2 = "harden is the man"

value = name1 + name2 #Concatenation (+)
print(value)

value1 = name1 * 3 #reptition (*)
print(value1)

value2 = name1[2] #slice prints the position of 0,1,2,3,4,...& so on. The [2] of Pervis = r
print(value2)

value3 = name1[2:4] #range slice. Slices from first digit in range to right before last digit in range. [2:4] of Pervis = rv
print(value3)

if "rv" in name1: #in 
    print("Nope not this one")

if "jk" not in name2: #not in
    print("haha")

print(r"Hello\r\nThere") # r"" ignores escape characters and print with string

print(name1.upper()) #turns everything to upper case

print(name1.lower()) #turns everything to lower case

print(name2.capitalize()) #Upper-case first letter of string

print(name2.split()) #creates a list for the string

print(ord("6")) #prints hex number for the string
print(chr(65)) #prints string for hex number


print(len(name1)) #number of characters