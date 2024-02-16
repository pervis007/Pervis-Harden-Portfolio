from datetime import date
todaysDate = date.today()
todaysDay10 = int(str(todaysDate)[9])
todaysDay01 = int(str(todaysDate)[8])
todaysDay11 = str(int(todaysDay10)) + str(int(todaysDay01))

todaysMonth = int(str(todaysDate)[5]) + int(str(todaysDate)[6])




dailyCode = todaysMonth * int(todaysDay11)

print(dailyCode)