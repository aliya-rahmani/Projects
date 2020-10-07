from tkinter import *
from random_words import RandomWords
from tkinter import messagebox

rw = RandomWords()
word = rw.random_word() 


while len(word)>9:
	word = rw.random_word() 

word=word.upper()
t=word
word=list(word)


root=Tk()
root.title("HANGMAN GAME")
root.geometry("625x350+400+200")
root.configure(bg='#EEC170')
root.resizable(0,0)

g_left=10
w_guesses=[]

def update_guess_left(c):
	global g_left
	
	if c not in word:
		g_left-=1
		Label(root, text=g_left, relief=SOLID, width=5, font=('Arial', 10), bg='#EEC170').place(x=235, y=120)
		if g_left==0:
			messagebox.showinfo("Information","GAME OVER!\nTHE WORD WAS: {}".format(t))
			root.destroy()
		wrong_guesses(c)
	else:
		while c in word:
			i=word.index(c)
			Label(root, text=c,font=('Arial', 10, 'bold'), bg='#EEC170').place(x=(50*i)+170,y=40)
			word[i]=0
			if 	all(v==0 for v in word):
				messagebox.showinfo("Information","YOU WON!")
				root.destroy()


def wrong_guesses(c):
	w_guesses.append(c)
	Label(root, text=w_guesses, relief=SOLID, width=20, font=('Arial', 10), bg='#EEC170').place(x=425,y=120)



Label(root, text='_____',font=('Arial', 10, 'bold'), bg='#EEC170').place(x=160,y=50)
s=210
l=len(word)
for i in range(1,l):
	Label(root, text='_____',font=('Arial', 10, 'bold'), bg='#EEC170').place(x=s,y=50)
	s+=50

Label(root, text="Length", font=('Arial', 10), bg='#EEC170').place(x=15, y=120)
Label(root, text=len(word), relief=SOLID, width=5, font=('Arial', 10), bg='#EEC170').place(x=65, y=120)
Label(root, text="Guesses left", font=('Arial', 10), bg='#EEC170').place(x=150, y=120)
Label(root, text=g_left, relief=SOLID, width=5, font=('Arial', 10), bg='#EEC170').place(x=235, y=120)
Label(root, text="Wrong Guesses", font=('Arial', 10), bg='#EEC170').place(x=320, y=120)
Label(root, text=w_guesses, relief=SOLID, width=20, font=('Arial', 10), bg='#EEC170').place(x=425,y=120)

Button(root, text='A', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('A')).place(x=15, y=200)
Button(root, text='B', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('B')).place(x=75, y=200)
Button(root, text='C', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('C')).place(x=135, y=200)
Button(root, text='D', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('D')).place(x=195, y=200)
Button(root, text='E', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('E')).place(x=255, y=200)
Button(root, text='F', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('F')).place(x=315, y=200)
Button(root, text='G', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('G')).place(x=375, y=200)
Button(root, text='H', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('H')).place(x=435, y=200)
Button(root, text='I', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('I')).place(x=495, y=200)
Button(root, text='J', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('J')).place(x=555, y=200)
Button(root, text='K', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('K')).place(x=15, y=250)
Button(root, text='L', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('L')).place(x=75, y=250)
Button(root, text='M', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('M')).place(x=135, y=250)
Button(root, text='N', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('N')).place(x=195, y=250)
Button(root, text='O', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('O')).place(x=255, y=250)
Button(root, text='P', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('P')).place(x=315, y=250)
Button(root, text='Q', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('Q')).place(x=375, y=250)
Button(root, text='R', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('R')).place(x=435, y=250)
Button(root, text='S', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('S')).place(x=495, y=250)
Button(root, text='T', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('T')).place(x=555, y=250)
Button(root, text='U', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('U')).place(x=135, y=300)
Button(root, text='V', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('V')).place(x=195, y=300)
Button(root, text='W', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('W')).place(x=255, y=300)
Button(root, text='X', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('X')).place(x=315, y=300)
Button(root, text='Y', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('Y')).place(x=375, y=300)
Button(root, text='Z', bg='#F58549', font=('Arial', 10, 'bold'),width=5, command=lambda:update_guess_left('Z')).place(x=435, y=300)

root.mainloop()
