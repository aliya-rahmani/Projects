#include<iostream>
using namespace std;

void BubbleSort(int A[],int n)
{
    for(int i=0;i<n-1;i++)
    {
        for(int j=0;j<n-i-1;j++)
        {
            if(A[j]>A[j+1])
                swap(A[j],A[j+1]);
        }
    }
}

int main()
{
    int n;
    cout<<"Enter the size of Array:"<<endl;
    cin>>n;
    int a[n];
    cout<<"Enter the Array elements:"<<endl;
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    BubbleSort(a,n);
    cout<<"After Bubble Sorting:"<<endl;
    for(int i=0;i<n;i++)
        cout<<a[i]<<" ";
        
    return 0;
    
}
