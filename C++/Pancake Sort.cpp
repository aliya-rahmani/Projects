#include<bits/stdc++.h>
using namespace std;
int maximumNumber(int arr[], int curr_size)
{
  int max =0, index =0;
      for (int i = 0; i < curr_size; i++)
      {
        if (arr[i]>max)
        {
          max = arr[i];
          index = i;
        }
      }
  return index;
}

int flip(int arr[], int max) 
{  
  int temp;
      for(int i = 0; i< max; i++)
      {
        temp = arr[i];
        arr[i] = arr[max];
        arr[max] = temp;
        max--;
      } 
}

int PancakeSort(int arr[], int number)
{
  for (int curr_size = number; curr_size > 1 ; curr_size--)
  {
    int max = maximumNumber(arr, curr_size);
        if (max != curr_size -1)
        {
          flip(arr, max);             
          flip(arr, curr_size-1);       
        }
  }
  cout<<"The sorted array is :  ";
  for (int i = 0; i < number; ++i)
      cout<<arr[i]<<" ";
  }

int main()
{
    int number;
    cin>>number;
    int arr[number];                          
    for (int i = 0; i < number; ++i)         
        cin>>arr[i];
    PancakeSort(arr,number);
    return 0;
}
