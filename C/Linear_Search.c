#include<stdio.h>
void main()
{
	int array[10],i,num,keynum,found=0;
	printf("\nEnter the value of Number");
	scanf("%d",&num);
	printf("The element one by one\n");
	for(i=0;i<num;i++)
	{
		scanf("%d",&array[i]);
	}
	printf("Input array is \n");
	for(i=0;i<num;i++)
	{
		printf("%d\n",array[i]);
	}
	printf("Enter the element to be searched");
	scanf("%d",&keynum);
	for(i=0;i<num;i++)
	{
		if(keynum==array[i])
		{
			found=1;
			break;
		}
	}
	if(found==1)
	{
		printf("The number is present in the array\n");
	}
	else
	{
		printf("The number is not present in the array\n");
	}
}
