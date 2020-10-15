#include<iostream>
using namespace std;
struct Array
{
    int A[10];
    int size;
    int length;
    
};
void display(struct Array arr)
{
    int i;
    cout<<"\nElements are"<<endl;
    for(i=0;i<arr.length;i++)
    {
        cout<<arr.A[i]<<" ";
    }
}

int BinarySearch(struct Array arr,int key)
{
    int l,mid,h;
    h=arr.length-1;
    while(l<=h)
    {
        mid=(l+h)/2;
        if(key==arr.A[mid])
            return mid;
        else if(key<arr.A[mid])
            h=mid-1;
        else
            l=mid+1;
    }
    return -1;
}

int main()
{
    struct Array arr={{1,2,5,6,9},10,5};
    cout<<"\nSearch element index:"<<BinarySearch(arr,2);
    display(arr);
    
    return 0;
}
