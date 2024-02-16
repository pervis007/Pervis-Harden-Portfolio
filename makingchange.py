changeAmt = 99

numQrts = changeAmt // 25
changeAmt = changeAmt - (numQrts * 25)

numDimes = changeAmt // 10
changeAmt -= (numDimes * 10)

numNicks = changeAmt // 5
changeAmt -= (numNicks * 5)

numPennies = changeAmt // 1
changeAmt -= (numPennies * 1)

print("Quarters: " + str(numQrts))
print("Dimes: " + str(numDimes))
print("Nickels: " + str(numNicks))
print("Pennies: " + str(numPennies))
