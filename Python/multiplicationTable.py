"""
    Description: Display multiplication table of a number
"""

# function to print the table
def table(n):   # n is taken as parameter
    i = 1 # table starts from 1
    while i <=10: # prints 10 iterations or upto 10
        print (str(n) + " X " + str(i) + " = " + str(n*i))
        print("\n") # new line
        i += 1 # incrementing i


n = int(input("Enter a number to display its multiplication table: "));
table(n)    # calling function table with n as parameter
