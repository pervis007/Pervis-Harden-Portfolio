import tkinter  as tk 
from tkcalendar import DateEntry 
from datetime import date

todaysDate = date.today()
todaysDay10 = int(str(todaysDate)[9])
todaysDay01 = int(str(todaysDate)[8])
todaysDay11 = str(int(todaysDay10)) + str(int(todaysDay01))

todaysMonth = int(str(todaysDate)[5]) + int(str(todaysDate)[6])




dailyCode = todaysMonth * int(todaysDay11)

my_w = tk.Tk()
my_w.geometry("380x220")  
cal=DateEntry(my_w,selectmode='day')
cal.grid(row=1,column=1,padx=20,pady=30)
def my_upd(): 
    l1.config(text=dailyCode) 
l1=tk.Label(my_w,text='data',bg='yellow')  
l1.grid(row=1,column=3)

b1=tk.Button(my_w,text='Read', command=lambda:my_upd())
b1.grid(row=1,column=2)

my_w.mainloop()