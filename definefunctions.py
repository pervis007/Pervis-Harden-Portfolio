import time as ti


def GreetUser(name):
    if ti.localtime().tm_hour < 12:
        print(f"Goodmorning {name}!")
    else:
        print(f"Good Evening {name}!")
    

GreetUser("Ben")

def isVowel(value,pos=1): #"xxx=1" will automatically calucate 1 
    if len(value) < pos:
        return "String too short"
    elif value[pos-1] in ["a","A","e","E","i","I","o","O","u","U"]:
        return f"The value in position {pos} IS a vowel."
    else: 
        return f"The value in position {pos} is NOT a vowel."

print(isVowel("Ben",0))
result = isVowel(pos=3, value="Sammy")
print(result)