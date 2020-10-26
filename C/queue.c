// JANVI VIJAY  19EJDML014
// Implementation of linear queue using array

#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#define MAX 5

int queue[MAX], front = -1, rear = -1;

void enQueue();
int deQueue();
void display();

void main(){
	int val, choice;
	
	while(1){
		printf("\n\n******MENU******\n");
		printf("1. Insert an element.\n");
		printf("2. Delete an element.\n");
		printf("3. Display the queue.\n");
		printf("4. EXIT\n");
		printf("Enter your choice : ");
		scanf("%d",&choice);
		switch(choice){
			case 1: enQueue();
					break;
			case 2: val = deQueue();
					if(val != -1)
						printf("\n The number deleted is : %d", val);
					break;
			case 3: display();
					break;
			case 4: exit(0);
			default: printf("\nPlease enter a valid option!");
		}		
	}
}

void enQueue(){
	int num;
	printf("\n Enter the number to be inserted in the queue : ");
	scanf("%d", &num);
	if(rear == MAX-1)
		printf("\n OVERFLOW");
	else{
		if(front == -1 && rear == -1)
			front = rear = 0;
		else
			rear++;
		queue[rear] = num;
		printf("\nInsertion successful!!!");
	}
}

int deQueue(){
	int val;
	if(front == -1 || front>rear){
		printf("\n UNDERFLOW");
		return -1;
	}
	else{
		val = queue[front];
		front++;
		if(front > rear)
		front = rear = -1;
		return val;
	}
}

void display(){
	int i;
	printf("\n");
	if(front == -1 || front > rear)
		printf("\n QUEUE IS EMPTY");
	else
	{
		for(i = front;i <= rear;i++)
		printf("%d\t", queue[i]);
	}
}



