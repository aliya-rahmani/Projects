"""

"""
# ====================================================== IMPORTS =======================================================
import tkinter
import random

# ===================================================== BEGIN CODE =====================================================


# Class that holds the data for the GUI
class Rolltk(tkinter.Tk):
    # ""Constructor"" that initiates the GUI
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()



    def initialize(self):

        # ================================================= ARRAYS =====================================================
        self.images = [tkinter.PhotoImage(file="images/die1.png"), tkinter.PhotoImage(file="images/die2.png"),
                       tkinter.PhotoImage(file="images/die3.png"), tkinter.PhotoImage(file="images/die4.png"),
                       tkinter.PhotoImage(file="images/die5.png"), tkinter.PhotoImage(file="images/die6.png")]

        self.resize = [self.images[0].subsample(6, 6), self.images[1].subsample(6, 6), self.images[2].subsample(6, 6),
                       self.images[3].subsample(6, 6), self.images[4].subsample(6, 6), self.images[5].subsample(6, 6)]

        # ============================================= TKINTER CODE ===================================================

        # Frame that the dice will display in after being rolled
        self.frame = tkinter.Frame(self, width = 1000, height = 110)
        self.frame.pack()

        # Label so the user knows this is where they input their desired amount of dice to roll
        tkinter.Label(self, text="Number of Dice:").pack()

        # Text box that accepts user input
        self.dienum = tkinter.Text(self, width=5, height=1)
        self.dienum.pack()

        # Button that will call function buttonclick to roll and display the dice
        tkinter.Button(self, text="Roll Dice", command=self.buttonclick).pack()

        # Label for the sum of all dice values
        tkinter.Label(self, text="Total: ").pack()

        # Variable that changes based on the sum of the dice values
        self.labelVariable = tkinter.IntVar()
        self.w = tkinter.Label(self, textvariable=self.labelVariable)
        self.w.pack()



    def userinput(self):
        # Converts the input from a string to an integer
        return int(self.dienum.get("1.0", tkinter.END))



    def roll(self):
        # Generates a random number for a random index of array self.resize
        return random.randrange(0, 5)



    def rollthedice(self):
        # Resets the sum of the dice when the user rerolls
        self.totals = 0
        # Resets the die faces when the user rerolls
        for x in self.frame.winfo_children():
            x.destroy()



    def buttonclick(self):
        # Calls rollthedice for the random number
        self.rollthedice()
        # For loop that will display a die value for the length of however many die the user wants to roll
        for x in range(0, self.userinput()):
            # Variable that will be used to find the sum of the die faces
            die = self.roll()
            # Displays a die face in a label
            tkinter.Label(self.frame, image=self.resize[die]).pack(side=tkinter.LEFT)
            # Since the random number is used to find the index it is one less than the die face. This will make each
            # value of the die face have the proper integer added to the total sum
            self.totals += (die + 1)
        # Sets the variable below the "Roll" button to the sum of the die faces
        self.labelVariable.set(self.totals)
        # Returns the value of the die faces
        return self.totals
        # print(self.totals)
        # return self.totals




if __name__ == "__main__":
    # Calls the main class "Rolltk
    app = Rolltk(None)
    # Sets the title of the window to "Dice Roller"
    app.title("Dice Roller")
    # Loops the program so the GUI can work
    app.mainloop()
