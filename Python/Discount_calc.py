import math 
import random 
import os

def final_price():
    final_price = (org_price - (org_price * (disc_perc/100)))
    return int(final_price)
   
org_price = int(input("Enter the original price: "))
disc_perc = int(input("Enter the dicount %:  \n"))


print("The final price after discount is: " , final_price())
    
    