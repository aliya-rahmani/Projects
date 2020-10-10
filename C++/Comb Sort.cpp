//	Comb Sort using C++
 
#include<bits/stdc++.h> 
using namespace std; 
  
int calculate_gap(int temp) 
{ 
    temp = (temp*10)/13; 
  
    if (temp < 1) 
        return 1; 
    return temp; 
} 
  
void funtion_comb_sort(int a[], int size) 
{ 
    int distance = size; 
    bool temp = true; 
  
    while (distance != 1 || temp == true) 
    { 
        distance = calculate_gap(distance); 
  
        temp= false; 
  
        for (int i=0; i<size-distance; i++) 
        { 
            if (a[i] > a[i+distance]) 
            { 
                swap(a[i], a[i+distance]); 
                temp= true; 
            } 
        } 
    } 
} 
  
int main() 													// Driver program 
{
	int size;												// Input no. of elements required in array

	cout<<"Enter the size of the array: ";
	cin>>size;
	cout<<"\n";

	int a[size];

	cout<<"Enter the elements of the array: \n";			// Input elements in the array
	for (int i = 0; i < size; i++)
		cin>>a[i];
  
    funtion_comb_sort(a, size); 
  
    cout<<"Sorted array: \n"; 
    for (int i=0; i<size; i++) 
        cout<<a[i]<<" "; 
  
    return 0; 
} 
