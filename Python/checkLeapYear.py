"""
    Description: check if an year inputted is leap year or not
"""

# leap year check function
def leap_year_check(year):
    if (year % 4) == 0:     # if a year is divisible by 4 and 100 it is leap year  
       if (year % 100) == 0:  
           if (year % 400) == 0:  
               print(str(year) + " is a leap year")  
           else:  
               print(str(year) + " is not a leap year")  
       else:  
           print(str(year) + " is a leap year")  
    else:  
       print(str(year) + " is not a leap year")  

year = int(input("Enter a year to check: "))
leap_year_check(year)

