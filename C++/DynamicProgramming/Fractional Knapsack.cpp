#include <bits/stdc++.h>
#include<vector>
using namespace std;
void fractional_knapsack(int item,float w[],float v[],int W)
{
    float x[100],profit=0.0;
    int i,j,weight=0;
    for(i=0;i<item;i++)
          x[i]=0;
    i=0;
    while(weight<W)
    {
      if(weight+w[i]<=W)
      {
          x[i]=1; 
          profit=profit+v[i];
          weight=weight+w[i];
          i++;
        }
      else
      {
          x[i]=(W-weight)/w[i];
          profit=profit+(x[i]*v[i]);
          weight=W;
       }
      }

    cout<<"X array is :"<<endl;
    for(int i=0;i<item;i++)
    {
        cout<<x[i]<<" ";
     }

    cout<<"\nMaximum Profit is:"<<profit;

}
int main()
{
    float w[100],v[100],vwratio[100];
    int i,j,item,temp,W;
    cout<<"Enter the number of Elements:";
    cin>>item;
    cout<<"Enter the weight and value of each
    item:"<<endl;
    for(i=0;i<item;i++)
    {
        cin>>w[i];
        cin>>v[i]; 
      }
    cout<<"Enter the Capacity:";
    cin>>W;
    for(i=0;i<item;i++)
    {
        vwratio[i]=v[i]/w[i];
      }
    for(i=0;i<item;i++)
    {
      for(j=i+1;j<item;j++)
      {
          if(vwratio[i]<vwratio[j])
          {
              swap(vwratio[i],vwratio[j]);
              swap(w[i],w[j]);
              swap(v[i],v[j]);
          }
      }
    }

    fractional_knapsack(item,w,v,W);
    return 0;

} 
