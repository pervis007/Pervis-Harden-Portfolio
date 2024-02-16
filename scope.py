#global ;variable is available everywhere

myName = 'Ben' 



def myFunc(color):
    global myName #how to make variable global
    myName = "Pervis"
    print(color) #local; variable only defined in the function
    print(myName)

    def nestedFunc():
        print(color)

    nestedFunc()

myFunc("red")


print(myName)