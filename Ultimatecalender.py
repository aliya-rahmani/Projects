from tkinter import *
import calendar
win=Tk()
win.title( "Calander")
def text() :
	month_str = month.get()
	year_str = year.get()
	month_int = int(month_str)
	year_int = int(year_str)
	cal = calendar.month(year_int, month_int)
	textfield.delete(0.0, END)
	textfield. insert(INSERT, cal)
   
label1 = Label (win, text= "Month:")
label1.grid(row=0, column=0)
month = Spinbox(win, from_=1, to=12, width=5)
month.grid(row=1, column=0)
label2 = Label(win, text= "Year:")
label2.grid(row=0, column=1)
year = Spinbox(win, from_=1700, to=2100, width=12)
year.grid (row=1, column=1, padx=8)
button = Button(win, text="Go", command=text)
button.grid( row=1, column =2 )
textfield = Text(win, height =10, width=25, foreground="red")
textfield.grid(row=3, columnspan=3)
win.mainloop()

     
