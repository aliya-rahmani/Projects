from tkinter import *

Win = Tk()

expression = ''
equation = StringVar()
topeq = StringVar()

Win.title('Mobile Calaculator')
Win.geometry('1080x2340')
Win.configure(highlightbackground='white')

def press(num):
	global expression
	global topeq
	expression += str(num)
	equation.set(expression)
	topeq.set(expression)
	
def clear():
	global expression
	expression = ""
	equation.set(expression)
	topeq.set(expression)
	
def equalpress():
	global expression
	total = str(eval(expression))
	equation.set(total)

blankline = Label(Win, text =' ', font=('helvetica',30))
blankline.grid(row=0, column=0, columnspan=4)

screenS=Entry(Win, width=23, border=0, font=('helvetica', 14), justify=RIGHT,textvariable = topeq)
screenS.grid(row=1, column=0, columnspan= 4, padx=10, pady=0)

screenB=Entry(Win, width=8, border=0, font=('helvetica', 41), justify=RIGHT, textvariable = equation)
screenB.grid(row=2, column=0, columnspan= 4, padx=15, pady=0)

blankline2 = Label(Win, text =' ', font=('helvetica',10))
blankline2.grid(row=3, column=0, columnspan=4)

buttonC=Button(Win, text='C', border=0, fg='white', bg='red', activebackground='light grey', height=3, width=5, command = clear)
buttonC.grid(row=4, column=3, padx=0, pady=20)

button7=Button(Win, text='7', border=0, fg='black', bg='white', activebackground='light grey', height=3, width=5, command = lambda : press(7))
button7.grid(row=5, column=0, padx=0, pady=20)

button8=Button(Win, text='8', border=0, fg='black', bg='white', activebackground='light grey', height=3, width=5, command = lambda : press(8))
button8.grid(row=5, column=1, padx=0, pady=20)

button9=Button(Win, text='9', border=0, fg='black', bg='white', activebackground='light grey', height=3, width=5, command = lambda : press(9))
button9.grid(row=5, column=2, padx=0, pady=20)

buttondivide=Button(Win, text='÷', border=0, fg='white', bg='#00fa4f', activebackground='#119119', height=3, width=5, command = lambda : press('/'))
buttondivide.grid(row=5, column=3, padx=0, pady = 20)

button4=Button(Win, text='4', border=0, fg='black', bg='white', activebackground='light grey', height=3, width=5, command = lambda : press(4))
button4.grid(row=6, column=0, padx=0, pady=20)

button5=Button(Win, text='5', border=0, fg='black', bg='white', activebackground='light grey', height=3, width=5, command = lambda : press(5))
button5.grid(row=6, column=1, padx=0, pady=20)

button6=Button(Win, text='6', border=0, fg='black', bg='white', activebackground='light grey', height=3, width=5, command = lambda : press(6))
button6.grid(row=6, column=2, padx=0, pady=20)

buttonmultiply=Button(Win, text='×', border=0, fg='white', bg='#00fa4f', activebackground='#119119', height=3, width=5, command = lambda : press('*'))
buttonmultiply.grid(row=6, column=3, padx=0, pady=20)

button1=Button(Win, text='1', border=0, fg='black', bg='white', activebackground='light grey', height=3, width=5, command = lambda : press(1))
button1.grid(row=7, column=0, padx=0, pady=20)

button2=Button(Win, text='2', border=0, fg='black', bg='white', activebackground='light grey', height=3, width=5, command = lambda : press(2))
button2.grid(row=7, column=1, padx=0, pady=20)

button3=Button(Win, text='3', border=0, fg='black', bg='white', activebackground='light grey', height=3, width=5, command = lambda : press(3))
button3.grid(row=7, column=2, padx=0, pady=20)

buttonsubtract=Button(Win, text='-', border=0, fg='white', bg='#00fa4f', activebackground='#119119', height=3, width=5, command = lambda : press('-'))
buttonsubtract.grid(row=7, column=3, padx=0, pady=20)

buttonadd=Button(Win, text='+', border=0, fg='white', bg='#00fa4f', activebackground='#119119', height=3, width=5, command = lambda : press('+'))
buttonadd.grid(row=8, column=0, padx=0, pady=20)

button0=Button(Win, text='0', border=0, fg='black', bg='white', activebackground='light grey', height=3, width=5, command = lambda : press(0))
button0.grid(row=8, column=1, padx=0, pady=20)

buttonpoint=Button(Win, text='.', border=0, fg='black', bg='white', activebackground='light grey', height=3, width=5, command = lambda : press('.'))
buttonpoint.grid(row=8, column=2, padx=0, pady=20)

buttonequal=Button(Win, text='=', border=0, fg='white', bg='#308546', activebackground='white', height=3, width=5, command = equalpress )
buttonequal.grid(row=8, column=3, padx=0, pady=20)

Win.mainloop()
