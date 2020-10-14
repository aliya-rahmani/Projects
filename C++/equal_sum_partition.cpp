/* Problem statement  - Given a non-empty array containing only positive integers,
 find if the array can be partitioned into two subsets such that the sum of
  elements in both subsets is equal.

*/
#include<bits/stdc++.h>
using namespace std;


bool subset_sum(int arr[],int n,int w)
{
    bool t[n+1][w+1];

    //initialisation of matrix
    for(int i=0;i<n+1;i++)
    for(int j=0;j<w+1;j++)
    {
        if(i==0)
        t[i][j]=false;
        if(j==0)
        t[i][j]=true;
    }

    //main logic
    for(int i=1;i<n+1;i++)
    for(int j=1;j<w+1;j++)
    {
        if(arr[i-1]<=j)
        t[i][j]=(t[i-1][j-arr[i-1]])||(t[i-1][j]);
        else
        {
            t[i][j]=t[i-1][j];
        }
        
    }

    return t[n][w];


}

bool equal_sum(int arr[],int n)
{
    int sum=0;
    for(int i=0;i<n;i++)
    sum+=arr[i];
    if(sum%2!=0)
    return false;
    return subset_sum(arr,n,sum/2);

}
int main()
{
    int n=4;
    int arr[4]={1,5,11,3};
    cout<<equal_sum(arr,n)<<endl;

}