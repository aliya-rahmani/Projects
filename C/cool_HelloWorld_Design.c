/*
	Description: 	Most programming starts with the two words Hello World, so here it is but in a little different way, instead of simply printing Hello World, it prints Hello World in a more cool and unconventional way.
				This code prints Hello World.

 This is a multiline comment and can span over many lines
*/
	// This is a  comment, comments are ignored by the compiler or won't be executed

// including header for input and output functions
#include <stdio.h>

// main function, every program starts executing from these function in C
// int is the return type
int main()
{	
	// printf is used to print output to the standard output device, screen
	// whatever is printed within the double quotes are strings and will be printed to the screen
      	printf("	)|    |(   )|====   [)        )]        <====>             [|       //      =====    ||===       [|        |||)	 \n");
       	printf(" 	||    ||   ||       ||        ||       ((    ))            ||  ___ //     //    //   ||   ))     ||        ||  ))	 \n");
	printf(" 	||====||   ||==>    ||        ||       ||    ||            || //||//     //    //    ||===|)     ||        ||   ))  \n");
	printf(" 	||    ||   ||       ||        ||       ((    ))            ||// ||/     //    //     ||    |)    ||        ||  ))    \n");
	printf(" 	)|    |(   )|====   [|====>   )|====>   <====>             |/   |/       =====       |/     |)   [|====>   |||) \n");
	
	// \n is used to goto the add a new line or goto next line
	// \ is escape sequence, used to print escape sequences like \n and to escape a characeter when printing a character

	// return is to return or send a value from a function, here return 0 signifies the program has  ended successfully
	return 0;
}
