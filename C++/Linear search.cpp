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

void swap(int *x,int*y)
{
    int temp;
    temp=*x;
    *x=*y;
    *y=temp;
}

int LinearSearch(struct Array *arr,int key)
{
    int i;
    for(i=0;i<arr->length;i++)
    {
        if(key==arr->A[i])
        {
            swap(&arr->A[i],&arr->A[0]);
            return i;
        }
    }
    return -1;
}
int main()
{
    struct Array arr={{1,2,5,6,9},10,5};
    display(arr);
    cout<<"\nSearch element index:"<<LinearSearch(&arr,2);
    display(arr);
    
    return 0;
}
