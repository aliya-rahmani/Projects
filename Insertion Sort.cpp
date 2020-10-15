#include<iostream>

using namespace std;

//Insertion Sort in the ascending order

/*Performing Insertion Sort - We take first element in the array as sorted sublist
others are unsorted sublist and first element in the unsorted sublist,
we take it as temporary value and we compare it with all elements in the sorted sublist
if temporary value is less than last element in the sorted list we move that last element to
the temporary value with in that we take it as sorted sublist and we insert temp value in the sorted sublist*/

int Insertion_Sort(int arr[],int n)
{
    for(int i=1;i<n;i++)
    {
        //temporary value to perform insertion sort
        int temp = arr[i];

        //limit to check all the elements in the sorted sublist
        int j = i-1;

        //It checks the elements in the sorted sublist if last value in the sorted sublist is less than temp then it enters in to the loop
        while(j>=0 && arr[j]>temp)
        {
            //To move the value which is greater than temp value
            arr[j+1] = arr[j];

            //Decrementing to check all the elements in the sorted sublist
            j--;
        }

        //If while loop condition(arr[j] > temp) fails then it take till temp as sorted sublist
        arr[j+1] = temp;
    }

    //Printing all the elements in the array After performing Insertion Sort
    cout<<"\nAfter performing Insertion Sort\n";
    for(int j=0;j<n;j++)
    {
       cout<<arr[j]<<" ";
    }
    cout<<"\n";

}


int main()
{
    int arr[50],size;
    cout<<"Enter the size of array:\n";
    cin>>size;

    //Array input
    for(int i=0;i<size;i++)
    {
        cin>>arr[i];
    }

    //Printing all the elements in the array Before performing Insertion Sort
    cout<<"\nBefore performing Insertion Sort\n";
    for(int j=0;j<size;j++)
    {
        cout<<arr[j]<<" ";
    }

    //for newline
    cout<<"\n";

    Insertion_Sort(arr,size);

    return 0;


}
