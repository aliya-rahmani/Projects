# import needed modules
from tkinter import *
import random

# define Score label
score = 0

# list of colors
colors = ['white', 'blue', 'green', 'yellow', 'orange', 'red', 'brown', 'black']

# Timer
timer = 60


# main game function
def startGame(event):
    if timer == 60:
        countdown()
    nextColor()


# function to display next color
def nextColor():
    global score
    global timer
    if timer > 0:
        entryBox.focus_set()
        if entryBox.get().lower() == colors[1].lower():
            score += 1
        entryBox.delete(0, END)
        random.shuffle(colors)
        guessLabel.config(fg=str(colors[1]), text=str(colors[0]))
        scoreLabel.config(text="score:" + str(score))


# function to start timer
def countdown():
    global timer
    if timer > 0:
        timer -= 1
        timeLabel.config(text='Time left:' + str(timer))
        window.after(1000, countdown)


# button press function
def presscolor(colname):
    entryBox.delete(0, END)
    entryBox.insert(0, colname)
    return


# draw window
window = Tk()
window.title('Color Game')
window.geometry('785x435')

# GUI
# instructions for the game
blankLine = Label(window, font=20)
instruction1 = Label(window, text="How to play : Press the Button with the NAME of the color and hit Enter key", font=('helvetica', 11))
instruction2 = Label(window, text="Be careful not to confuse it with the  the TEXT", font=('helvetica', 11))
scoreLabel = Label(window, text="Press Enter to start", font=('helvetica', 9))
timeLabel = Label(window, text='time = 60 sec', font=('helvetica', 13))
guessLabel = Label(window, font=('helvetica', 60))
blankLine1 = Label(window, font=30)


# design all buttons
buttonBlack = Button(window,
                     text="Black",
                     border=0,
                     fg='white',
                     bg='black',
                     height=3,
                     width=10,
                     font=0,
                     command=lambda: presscolor("Black"))
buttonBrown = Button(window,
                     text="Brown",
                     border=0,
                     fg='white',
                     bg='Brown',
                     activebackground='Brown',
                     height=3,
                     width=10,
                     font=0,
                     command=lambda: presscolor("Brown"))
buttonBlue = Button(window,
                    text="Blue",
                    border=0,
                    fg='white',
                    bg='blue',
                    activebackground='blue',
                    height=3,
                    width=10,
                    font=0,
                    command=lambda: presscolor("Blue"))
buttonViolet = Button(window,
                      text="Violet",
                      border=0,
                      fg='white',
                      bg='Violet',
                      activebackground='Violet',
                      height=3,
                      width=10,
                      font=0,
                      command=lambda: presscolor("Violet"))
buttonGreen = Button(window,
                     text="Green",
                     border=0,
                     fg='white',
                     bg='Green',
                     activebackground='Green',
                     height=3,
                     width=10,
                     font=0,
                     command=lambda: presscolor("Green"))
buttonYellow = Button(window,
                      text="Yellow",
                      border=0,
                      fg='Black',
                      bg='Yellow',
                      activebackground='Yellow',
                      height=3,
                      width=10,
                      font=0,
                      command=lambda: presscolor("Yellow"))
buttonOrange = Button(window,
                      text="Orange",
                      border=0,
                      fg='white',
                      bg='Orange',
                      activebackground='Orange',
                      height=3,
                      width=10,
                      font=0,
                      command=lambda: presscolor("Orange"))
buttonRed = Button(window,
                   text="Red",
                   border=0,
                   fg='White',
                   bg='Red',
                   activebackground='Red',
                   height=3,
                   width=10,
                   font=0,
                   command=lambda: presscolor("Red"))
buttonWhite = Button(window,
                     text="White",
                     border=0,
                     fg='Black',
                     bg='White',
                     activebackground='White',
                     height=3,
                     width=10,
                     font=0,
                     command=lambda: presscolor("White"))
entryBox = Entry(window, width=50)


# draw all buttons in Grid
blankLine.grid(column=0, row=0, columnspan=4)
instruction1.grid(column=0, row=1, columnspan=4, padx=150)
instruction2.grid(column=0, row=2, columnspan=4, padx=100)
scoreLabel.grid(column=0, row=3, columnspan=4)
timeLabel.grid(column=0, row=4, columnspan=4)
guessLabel.grid(column=0, row=5, columnspan=4)
entryBox.grid(column=0, row=7, columnspan=4)
blankLine1.grid(column=0, row=8, columnspan=4)
buttonBlack.grid(column=0, row=9)
buttonBrown.grid(column=1, row=9)
buttonBlue.grid(column=2, row=9)
buttonGreen.grid(column=3, row=9)
buttonYellow.grid(column=0, row=10, pady=25)
buttonOrange.grid(column=1, row=10)
buttonRed.grid(column=2, row=10)
buttonWhite.grid(column=3, row=10)

window.bind('<Return>', startGame)

entryBox.focus_set()

window.mainloop()
