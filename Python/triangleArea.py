"""
	Description: find the area of triangle, given breadth and height
"""

# function definition of areatriangle
def areatriangle(breadth,height):
	return (breadth*height)/2;


# input breadth and height
b = int(input("Enter the breadth of triangle: "))
h = int(input("Enter teh height of triangle: "))
print("The area of the triangle is: " + str(areatriangle(b,h)))

