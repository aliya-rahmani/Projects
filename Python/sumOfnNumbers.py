"""
    Description: Calculate and print the sum of frist n natural numbers
"""

# sum_n function calcualtes sum upto n
def sum_n(n):
    i = 1 # starts from 1
    sum_n = 0 # initialising sum to 0
    while i <= n:
        sum_n += i
        i += 1
    print ("The sum of first " + str(n) + " numbers is " + str(sum_n))

# input prompt
n = int(input("Enter the range to which to calculate sum: "))
# calling sum_n function with n as argument
sum_n(n)
