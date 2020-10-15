//		Write a program to implement following operations on Deque:
//		1. Insert at front 
//		2. Insert at rear 
//		3. Delete from front 
//		4. Delete from rear


#include<stdio.h>			//Used for standard input and output
#include<stdlib.h>			//Used for memory allocation, process control, conversions

# define MAX 5

int deque[MAX];
int front=-1;
int rear=-1;

void insert_at_front();		//Function declaration
void insert_at_rear();		//Function declaration
void delete_at_front();		//Function declaration
void delete_at_rear();		//Function declaration
void display_queue();		//Function declaration

void main(){
	int choice;
	do{	
		printf("\nM.E.N.U\n");				//Menu driven 
		printf("1.Insert at front\n");
		printf("2.Insert at rear\n");
		printf("3.Delete from front\n");
		printf("4.Delete from rear\n");
		printf("5.Display\n");
		printf("6.Exit\n\n");
		printf("Enter your choice: ");
		scanf("%d",&choice);
		printf("\n");
		switch(choice){
			
			case 1 :
				insert_at_front();
				break;
	 		case 2:
				insert_at_rear();
				break;
			case 3:
				delete_at_front();
				break;
			case 4:
				delete_at_rear();
				break;
			case 5:
				display_queue();
				break;
			case 6:
				exit(0);
			default:
				printf("Sorry, wrong choice\n");
		}
		}	
}

void insert_at_front()									//Insert an element at front
{
	int add_item;
	
	if((front==0 && rear==MAX-1)||(front==rear+1))
	{
		printf("Queue Overflow \n");
		return;	
	}
	
	
	if(front==-1)
	{
		front=0;
		rear=0;	 
	}
	else
	{
		if(front==0)
			front=MAX-1;
		else
			front=front-1;
	
	}
	
	printf("Element to add at front: ");
	scanf("%d",&add_item);
	deque[front]=add_item;	
}
	

void insert_at_rear()									//Insert an element at rear
{
	int add_item;
	
	if((front==0 && rear==MAX-1)||(front==rear+1))
	{
		printf("Queue Overflow\n");
		return;
	}
	
	
	if(front==-1)
	{
		front=0;
		rear=0;
	}
	else
	{
		if(rear==MAX-1)
			rear=0;
		else
			rear+=1;	
	}

	printf("Element to add at rear: ");
	scanf("%d",&add_item);
	deque[rear]=add_item ;
}



void delete_at_front()									//Delete an element at front
{
	if(front==-1)
	{
		printf("Queue Underflow\n");
		return;
	}
	
	printf("Deleted element: %d\n",deque[front]);
	
	
	if(front==rear)
	{
		front=-1;
		rear=-1;
	}
	else
	{
		if(front==MAX-1)
			front=0;
		else
			front+=1;
	}
		
}



void delete_at_rear()									//Delete an element at rear
{
	if(front==-1)
	{
		printf("Queue Underflow\n");
		return ;
	}
	
	printf("Deleted element: %d\n",deque[rear]);
	
	
	if(front==rear)
	{
		front=-1;
		rear=-1;
	}
	else
	{
		if(rear==0)
			rear=MAX-1;
		else
			rear=rear-1;
	}
}


void display_queue()									//Display queue elements
{
	int position_front=front,position_rear=rear;
	
	if(front==-1)
	{
		printf("Queue is empty\n");
		return;	 
	}
	
	printf("Queue elements: ");
	
	if(position_front<=position_rear)
	{
		while(position_front<=position_rear)
		{
			printf("%d ",deque[position_front]);
			position_front++;
		}
	}
	else
	{	
		while(position_front<=MAX-1)
		{
			printf("%d ",deque[position_front]);
			position_front++;	
		}
		
		position_front=0;
		
		while(position_front<=position_rear)
		{
			printf("%d ",deque[position_front]);
			position_front++;
		}
	}
	printf("\n");
}
