# A simple Rock Paper Scissor Game written in python
# Contributed by Parjanya HK

import random
print("The Rules of Rock paper scissor game will be follows: \n"
+"Rock vs paper --> paper wins \n"
+"Rock vs scissor --> Rock wins \n"
+"paper vs scissor --> scissor wins \n")

while True:
print("Now please enter your choice no. \n 1. Rock \n 2. paper \n 3. scissor \n")
ch = int(input("Now Your turn: "))
while ch> 3 or ch< 1:
   ch = int(input("Enter your valid input here: "))
if ch == 1:
   choice_name = 'Rock'
elifch == 2:
   choice_name = 'paper'
else:
   choice_name = 'scissor'

   print("Your choice is: " + choice_name)
print("\nNow its computer turn to initiate.......")

comp_choice = random.randint(1, 3)

while comp_choice == ch:
comp_choice = random.randint(1, 3)

if comp_choice == 1:
   comp_choice_name = 'Rock'
elifcomp_choice == 2:
   comp_choice_name = 'paper'
else:
   comp_choice_name = 'scissor'
   print("So computer choice is: " + comp_choice_name)
	
print(choice_name + " V/s " + comp_choice_name)
   # condition for winning the game
if((ch == 1 and comp_choice == 2) or
   (ch == 2 and comp_choice ==1 )):
print("paper wins => ", end = "")
   final_result = "paper"
elif((ch == 1 and comp_choice == 3) or
   (ch == 3 and comp_choice == 1)):
print("Rock wins =>", end = "")
   final_result = "Rock"
else:
   print("scissor wins =>", end = "")
   final_result = "scissor"

if final_result == choice_name:
   print("<== You are the winner ==>")
else:
   print("<== Computer wins ==>")
      print("Do you want to play again? (Y/N)")
      ans = input()

if ans == 'n' or ans == 'N':
   break
print("\nThanks for Playing!")
