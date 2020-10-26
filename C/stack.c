#include <stdio.h>
#include <stdlib.h>
#define SIZE 5

void push(int);
void pop();
void display();
int st[SIZE], top = -1;

void main(){
	int value,choice;
	while(1){
		printf("\n******MENU******\n");
		printf("1. Push\n2. Pop\n3. Display\n4. Exit");
		printf("\nEnter your choice : ");
		scanf("%d",&choice);
		switch(choice){
			case 1: printf("Enter the value to be inserted : ");
					scanf("%d",&value);
					push(value);
					break;
			case 2: pop();
					break;
			case 3: display();
					break;
			case 4: exit(0);
			default: printf("\nPlease enter a valid option!");
		}
	}
}

void push(int value){
	if(top == SIZE-1)
	{
		printf("\n STACK OVERFLOW");
	}
	else
	{
		top++;
		st[top] = value;
		printf("\nInsertion success!\n");
	}
}

void pop(){
	if(top == -1)
		printf("\n STACK UNDERFLOW");
	else
	{
		printf("\nDeleted : %d\n", st[top]);
		top--;
	}
}

void display(){
	int i;
	if(top == -1)
		printf("\n STACK IS EMPTY");
	else{
		printf("\nStack elements are:\n");
		for(i=top;i>=0;i--)
		printf("\n %d",st[i]);
	}
}

