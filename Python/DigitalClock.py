#import all useful module in the program
from tkinter import *
import datetime
import time

# Create a window by using the Tkinter
root = Tk()

# write the Heading on the window
root.title('Digital Clock By HS')

# geomerty of the window
root.geometry('500x300')
# fixed the window
root.resizable(0,0)
# set the colour of backroundwindow 
root.configure(background='black')

# create a Label Widget for print on the window
t1 = Label(root,text='Digital Clock',font=('Arial',30),fg='red',bg='black').place(x=140,y=0)


# create a function for finding the time 
def clock():
    l1=time.strftime("%H:%M:%S %p")
    l2=Label(root,text=l1,font=('ds digital',40,'bold'),fg='light green',bg='black')
    l2.after(200,clock)
    l2.place(x=80,y=190)
    l5=datetime.date.today()
    l8=Label(root,text=l5.day,font=('ds digital',40,'bold'),fg='light green',bg='black').place(x=355,y=90)
    l7=Label(root,text=l5.month,font=('ds digital',40,'bold'),fg='light green',bg='black').place(x=260,y=90)
    l6=Label(root,text=l5.year,font=('ds digital',40,'bold'),fg='light green',bg='black').place(x=80,y=90)
    l11=Label(root,text="DATE",font=('ds digital',15,'bold'),fg='light green',bg='black').place(x=355,y=160)
    l10=Label(root,text="MONTH",font=('ds digital',15,'bold'),fg='light green',bg='black').place(x=235,y=160)
    l9=Label(root,text="YEAR",font=('ds digital',15,'bold'),fg='light green',bg='black').place(x=90,y=160)        
    l12=Label(root,text="HOUR",font=('ds digital',15,'bold'),fg='light green',bg='black').place(x=80,y=260)
    l13=Label(root,text="MIN",font=('ds digital',15,'bold'),fg='light green',bg='black').place(x=185,y=260)
    l14=Label(root,text="SEC",font=('ds digital',15,'bold'),fg='light green',bg='black').place(x=280,y=260)

# clock function 
clock()

# end the program
root.mainloop()
