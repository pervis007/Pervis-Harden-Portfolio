from tkinter import *
from tkcalendar import *
from datetime import date
todaysDate = date.today()
todaysDay10 = int(str(todaysDate)[9])
todaysDay01 = int(str(todaysDate)[8])
todaysDay11 = str(int(todaysDay10)) + str(int(todaysDay01))

todaysMonth = int(str(todaysDate)[5]) + int(str(todaysDate)[6])




dailyCode = todaysMonth * int(todaysDay11)


gangsta = Tk()

gangsta.title('onePOS Daily Code')
gangsta.iconbitmap()
gangsta.geometry("380x380")


caltech = Calendar(gangsta, selectmode="day", year=2023)
caltech.grid(row=1,column=1,padx=20,pady=30)
caltech.pack(pady=20)


def grab_date():
    da_label.config(text="Daily Code: " + str(dailyCode))

da_button = Button(gangsta, text="Get Today's Code", command=grab_date)
da_button.pack(pady=20)

da_label = Label(gangsta, text='')
da_label.pack(pady=20)

gangsta.mainloop()