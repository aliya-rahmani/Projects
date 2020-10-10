"""
Building a simple calulator which performs the following operations 
 1> Multiplication
 2> Division
 3>Addition
 4>Substraction

_________________________________________________
|               simple calculator               |
-------------------------------------------------
|    ____________________________________       |
|   |____________________________________|      |
|   |        |        |        |         |      |
|   |   7    |    8   |   9    |    *    |      |
|   |________|________|________|_________|      |
|   |        |        |        |         |      |
|   |   4    |    5   |   6    |    /    |      |
|   |________|________|________|_________|      |
|   |        |        |        |         |      |
|   |   1    |    2   |   3    |    +    |      |
|   |________|________|________|_________|      |
|   |        |        |        |         |      |
|   |   C    |    0   |   =    |    -    |      |
|   |________|________|________|_________|      |
|_______________________________________________|   


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<(-_-)    serious ???     (-_-)>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
__________________________________C     O     D      E________________________________________
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>``""""""""""""""""""``<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


"""
from tkinter import *
root  = Tk()
root.title("Simple Calculator")

#creating a Entry text field 
#Widget

e = Entry(root,width = 60,borderwidth = 5)
e.grid(row = 0,column = 0,columnspan = 4,padx = 10,pady = 5)



#Adding value to text field
def add_button(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,current+str(number))

#Clear text field
def clear():
    e.delete(0,END)

#Evaluation operations
#   Addition
def add():
    global prev
    global operation
    operation = "A"
    prev = int(e.get())
    e.delete(0,END) 

#   Substraction
def sub():
    global prev
    global operation
    operation = "S"
    prev = int(e.get())
    e.delete(0,END)

#   Division 
def div():
    global prev
    global operation
    operation = "D"
    prev = int(e.get())
    e.delete(0,END)

#   Multiplication
def mul():
    global prev
    global operation
    operation = "M"
    prev = int(e.get())
    e.delete(0,END)
    

#   evaluation
def equals():
    sec_no = int(e.get())
    e.delete(0,END)
    if operation == "M":
        e.insert(0,prev*sec_no)

    if operation == "D":
        #   for the sake of zero division error
        #   we'll use try-except-finally block

        try:
            e.insert(0,prev/sec_no)

        except Exception as obj:
            e.insert(0,obj)    
        
        finally:
            pass
    if operation == "A":
        e.insert(0,prev+sec_no)

    if operation == "S":
        e.insert(0,prev-sec_no)                   
    


#creating all buttons
#   numeric buttons 0-9
button_1 = Button(root,text = "1",padx = 40,pady = 20,command =lambda: add_button(1))
button_2 = Button(root,text = "2",padx = 40,pady = 20,command =lambda: add_button(2))
button_3 = Button(root,text = "3",padx = 40,pady = 20,command =lambda: add_button(3))
button_4 = Button(root,text = "4",padx = 40,pady = 20,command =lambda: add_button(4))
button_5 = Button(root,text = "5",padx = 40,pady = 20,command =lambda: add_button(5))
button_6 = Button(root,text = "6",padx = 40,pady = 20,command =lambda: add_button(6))
button_7 = Button(root,text = "7",padx = 40,pady = 20,command =lambda: add_button(7))
button_8 = Button(root,text = "8",padx = 40,pady = 20,command =lambda: add_button(8))
button_9 = Button(root,text = "9",padx = 40,pady = 20,command =lambda: add_button(9))
button_0 = Button(root,text = "0",padx = 40,pady = 20,command =lambda: add_button(0))

#   clear button as c
#   equals button as =
button_c = Button(root,text = "C",padx = 40,pady = 20,command = clear)
button_e = Button(root,text = "=",padx = 40,pady = 20,command = equals)

#   sign of operators
button_add = Button(root,text = "+",padx = 40,pady = 20,command = add)
button_sub = Button(root,text = "-",padx = 40,pady = 20,command = sub)
button_div = Button(root,text = "/",padx = 40,pady = 20,command = div)
button_mul = Button(root,text = "*",padx = 40,pady = 20,command = mul)

#Adding buttons to canvas
#   2nd row , 0-3 column
button_7.grid(row = 1,column = 0)
button_8.grid(row = 1,column = 1)
button_9.grid(row = 1,column = 2)
button_mul.grid(row = 1,column = 3)

#   3rd row , 0-3 column
button_4.grid(row = 2,column = 0)
button_5.grid(row = 2,column = 1)
button_6.grid(row = 2,column = 2)
button_div.grid(row = 2,column = 3)

#4th row , 0-3 column
button_1.grid(row = 3,column = 0)
button_2.grid(row = 3,column = 1)
button_3.grid(row = 3,column = 2)
button_sub.grid(row = 3,column = 3)

#   5th row , 0-3 column
button_c.grid(row = 4,column = 0)
button_0.grid(row = 4,column = 1)
button_e.grid(row = 4,column = 2)
button_add.grid(row = 4,column = 3)

#Everything ready-to-go let's call mainloop()
root.mainloop()


