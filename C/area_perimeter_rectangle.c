/* 
	Descripton: This program calculates the perimeter and area of a rectangle and outputs the result.
	*Note: Can be used to calculate perimeter and area of square also
	(height and width needs to be same)
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
	// variable decalaration
    float height, width, area, perimeter;

	// calculating perimeter
    perimeter = 2 * (height + width);
	
	// calculating area
    area = height * width;

	// input prompt
	printf("Enter the height and width: ");
	scanf("%f %f",&height,&width);

	// output
    printf("\nThe perimeter of the rectangle is %f.",perimeter);
    printf("\nThe area of the rectangle is %f.",area);

    return 0;
}
