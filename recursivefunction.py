#factorial

def factorial(number):
    final = 1 
    for i in range(number, 0, -1):
        final = final * i
    return final
print(factorial(6))


#recursive

def factorialRecur(number):
    if number == 1:
        return number
    else:
        return number * factorialRecur(number - 1)
print(factorialRecur(7))