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



int main()
{

    int arr[5]={2,3,7,8,10};
    int n=5;
    int sum=100;
    cout<<subset_sum(arr,n,sum)<<endl;

}