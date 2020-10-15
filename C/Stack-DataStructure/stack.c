/*
Stack Implimentation using Static Array,
Operations: 1. Insert 2. Delete(pop) 3. Traverse(display) 4. Peak(top_element) 5. Length ...
*/
#include <stdio.h>
#include <stdlib.h>
#define SIZE 100

// function decleration ...
void insert(int);
void pop(void);
void display(void);
void peak(void);
int length(void);
int isFull(void);
int isEmpty(void);

// Global variables
int stack[SIZE];
int top = -1;


int main(){
	int choise,ele;	
	printf("--- Stack Implimentation using Static Array ---\n");
	while(1){
		printf("\n");
		printf("1. Insert\n");
		printf("2. Delete(pop)\n");
		printf("3. Traverse(display)\n");
		printf("4. Peak(top_element)\n");
		printf("5. Length\n");
		printf("6. Exit\n");

		scanf("%d",&choise);
		printf("--------------------------------------------\n");
		switch(choise) {
			case 1:	if(isFull()){
					 	printf("You can not insert, because the Stack is overflow/filled ...\n");
						break;
					}
					else{
						printf("Enter the New Element :\n");
					 	scanf("%d",&ele);
					 	insert(ele);
						break;
					}
			case 2:	pop();
				 	break;
			case 3:	display();
				 	break;
			case 4:	peak();
				 	break;
			case 5:	printf("The length of the Stack is : %d\n",length());
				 	break;
			case 6:	exit(0);
			
			default:printf("Invalid input !!!\n");
		}
	}

	return 0;
}


void insert(int ele){
//	check if stack is full ...
	if(isFull()){
		printf("The stack is overflow/filled ...\n");
	}
	else{
		top++;
		stack[top] = ele;
		printf("%d inserted successfully ...\n",ele);
	}
}


void pop(){
//	check if stack is empty or not ...
	if(isEmpty()){
		printf("The stack is Empty ...\n");
	}
	else{
		printf("%d deleted successfully ...\n",stack[top]);
		top--;
	}
}


void display(){
//	check if stack is empty or not ...
	if(isEmpty()){
		printf("The stack is Empty ...\n");
	}
	else{
		printf("The stack\'s elements are ...\n");
		int i;
		for(i=0;i<=top;i++){
			printf("%d \t",stack[i]);
		}
		printf("\n");
	}
}


void peak(){
//	check if stack is empty or not ...
	if(isEmpty()){
		printf("The stack is Empty ...\n");
	}
	else{
		printf("The top most element of stack is : %d ...\n",stack[top]);
	}
	
}


int length(){	
	return (top+1);
}


int isFull(){
	if(top == (SIZE-1)){
		return 1;
	}
	
	return 0;
}


int isEmpty(){
	if(top == -1){
		return 1;
	}
	
	return 0;
}


