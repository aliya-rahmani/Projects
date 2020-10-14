/*
	Description: Code to take input of two numbers from standard input(stdin)- keyboard and print their sum
*/

// adding header for i/o operations
#include <stdio.h>

int main()
{
	// variable declaration
	int first_num, second_num;

	// input prompt
	printf("Enter two integer numbers: ");
	// scanning input using scanf
	scanf("%d %d",&first_num, &second_num);

	// adding first_num and second num and printing their sum
	printf("\nThe sum of the numbers is: %d", first_num + second_num);

return 0;
}
