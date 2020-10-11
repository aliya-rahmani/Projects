#include <stdio.h>
#include <stdlib.h>
#define SIZE 20

void sort(int[], int);
void insertElementInSortedArray(int[], int*, int);

int main(){
	int arr[SIZE],len,element,i,st;
	printf("Enter Array Size :\n");
	scanf("%d",&len);
	printf("Enter the Array Elements :\n");
	for(i=0;i<len;i++){
    	scanf("%d",&arr[i]);
	}
//	sorting of array
	sort(arr,len);
	printf("Given Sorted Array is :\n");
	for(i=0;i<len;i++){
    	printf("%d\t",arr[i]);
	}
	printf("\n");
	while(1){
	printf("\n1. Insert Element\n2. Exit\n");
	scanf("%d",&st);
	switch(st){
		case 1: //	insertion of new element in array
			 	printf("\nEnter New Element You want to insert :\n");
				scanf("%d",&element);
				insertElementInSortedArray(arr,&len,element);
				printf("\nAfter inserting %d, New Array is :\n",element);
				for(i=0;i<len;i++){
			    	printf("%d\t",arr[i]);
				}
			 	break;
			 	
		case 2: exit(0);
		
		default:printf("Invalid input !!!");
	}
	}
	return 0;
}


void insertElementInSortedArray(int arr[], int *len, int element){
	int i;
	for(i=*len-1;i>=0;i--){
		if(arr[i] > element){
			arr[i+1] = arr[i];
		}
		else{
			break;
		}
	}
	arr[i+1] = element;
	*len += 1;
}


// bubble sorting
void sort(int arr[], int len){
	int i,j;
	for(i=0;i<len-1;i++){
		for(j=0;j<len-1-i;j++){
			if(arr[j]>arr[j+1]){
				arr[j] = arr[j] + arr[j+1];
				arr[j+1]= arr[j] - arr[j+1];
				arr[j] = arr[j] - arr[j+1];
			}
		}
	}
}
