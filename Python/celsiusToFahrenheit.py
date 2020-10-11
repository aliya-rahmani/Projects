"""
    Description: Given temperature celsius converts to fahrenheit
"""

# function to convert fahrenheit to celsius
def fahrenheit_to_celsius(F):
    C = (F-32)/1.8
    print(str(temp) + "F is " + str(C) + "C")

# function to convert celsius to fahrenheit
def celsius_to_fahrenheit(C):
    F = C*1.8 + 32
    print(str(temp) + "C is " + str(F) + "F")

# input
temp = float(input("Enter temperature : "))
print ("\nChoose conversion option: \n1. Fahrenheit to Celsius \n2. Celsius to Fahrenheit")
ch = int(input())

if (ch == 1):
    fahrenheit_to_celsius(temp)
elif (ch == 2):
    celsius_to_fahrenheit(temp)
else:
    print("\nInvalid choice.")
