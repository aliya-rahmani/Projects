# importing needed modules
from tkinter import *
import random

# creating and naming a window
window = Tk()
window.geometry('720x330')
window.title("Rock, Paper, Scissors")

# defining user score
u_score = 0

# defining computer score
c_score = 0

# list of options
options = [('Rock', 0), ('Paper', 3), ('Scissors', 2)]


# user input function
def player_choice(pinput):
    global u_score, c_score
    cinput = computer_choice()
    PlayerChoiceLabel.config(text='You Selected:' + pinput[0])
    ComputerChoiceLabel.config(text='Computer Selected:' + cinput[0])

    if cinput == pinput:
        WinnerLabel.config(text='Tie')
    elif (pinput[1] - cinput[1]) % 3 == 1:
        u_score += 1
        WinnerLabel.config(text='You Won')
        PlayerScoreLabel.config(text='Your Score:' + str(u_score))
    else:
        c_score += 1
        WinnerLabel.config(text='Computer Won')
        ComputerScoreLabel.config(text='Computer Score:' + str(c_score))


# computer input function
def computer_choice():
    return random.choice(options)


# GUI
# adding a blank line to make it look more beautiful
blank_line = Label(text='', font=('helvetica', 20))
blank_line.pack()
# Heading
GTitle = Label(text='Rock Paper Scissors', fg='grey', font=('helvetica', 20))
GTitle.pack()

# Display The winner name
WinnerLabel = Label(text='Chose to Start', fg='Green', font=('helvetica', 13))
WinnerLabel.pack()

windows = Frame(window)
windows.pack()

# define and customise all buttons and labels
OptionsLabel = Label(windows,
                     text='Options:',
                     fg='Grey',
                     font=('helvetica', 12))
RButton = Button(windows,
                 text='Rock',
                 bg='Pink',
                 activebackground='Pink',
                 border=0,
                 width=15,
                 pady=15,
                 command=lambda: player_choice(options[0]))
PButton = Button(windows,
                 text='Paper',
                 bg='Silver',
                 activebackground='Silver',
                 border=0,
                 width=15,
                 pady=15,
                 command=lambda: player_choice(options[1]))
SButton = Button(windows,
                 text='Scissors',
                 bg='Light Blue',
                 activebackground='Light Blue',
                 border=0,
                 width=15,
                 pady=15,
                 command=lambda: player_choice(options[2]))
ScoreLabel = Label(windows,
                   text='Score:',
                   fg='Grey',
                   font=('helvetica', 12))
PlayerChoiceLabel = Label(windows,
                          text='You Selected:---',
                          font=12)
PlayerScoreLabel = Label(windows,
                         text='Your Score:---',
                         font=12)
ComputerChoiceLabel = Label(windows,
                            text='Computer Selected:---',
                            font=12)
ComputerScoreLabel = Label(windows,
                           text='Computer Score:---',
                           font=12)

# display all buttons and labels in Grid
OptionsLabel.grid(row=2, column=0, padx=50, pady=15)
RButton.grid(row=3, column=1, padx=15)
PButton.grid(row=3, column=2, padx=15)
SButton.grid(row=3, column=3, padx=15)
ScoreLabel.grid(row=4, column=0, padx=50, pady=15)
PlayerChoiceLabel.grid(row=5, column=0, columnspan=2)
PlayerScoreLabel.grid(row=5, column=2, columnspan=2)
ComputerChoiceLabel.grid(row=6, column=0, columnspan=2)
ComputerScoreLabel.grid(row=6, column=2, columnspan=2)

window.mainloop()
