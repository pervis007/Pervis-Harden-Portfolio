changeAmt = input("What is the customer's change amount?:")
changeAmt = int(changeAmt)

coins = [25,10,5,1]
coinsCounts = [0,0,0,0]
coinNames = ["Quarters","Dimes","Nickels","Pennies"]

for i in range(0, len(coins)):
    coinsCounts[i] = changeAmt // coins[i]
    changeAmt = changeAmt - (coinsCounts[i] * coins[i]) 
    print(f"{coinNames[i]}:{coinsCounts[i]}")




