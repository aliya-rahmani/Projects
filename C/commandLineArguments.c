/* 
	Description: Takes command line arguments and prints the first argument which is the name of the program and the second is the argument given
	*Note: Only two arguments are printed, whatever may be the number of arguments provided
*/

// including i/o header
#include<stdio.h>

	// argc and argv are the parameters, argc stores number of arguments and argv stores the list of arguments given as command line
int main(int argc, char *argv[])
{
    // variable initialization
	// number of arguments is assigned the value of argc
    int numberOfArguments = argc;
	// character pointer argument1 is set to point to arv[0] and character pointer argument2 is set to point to argv[1] 
    char *argument1 = argv[0];
    char *argument2 = argv[1];

	// printing the output
    printf("\nNumber of Argument: %d", numberOfArguments); // prints the number of arguments given
    printf("\nArgument 1 is the program name: %s", argument1); // first argument is the name of the program, so program name is printed
    printf("\nArgument 2 is the command line argument: %s", argument2); // second argument is the command line argument

    return 0;
}
