#include<iostream>
using namespace = std;
int main()
{
      int n;
      int sum = 0;

     //It stops when n=0
     while (n>0 || sum>9)
     {
          if (n==0)
          {
               n=sum;
               sum=0;
          }
           sum +=n % 10;
           n /= 10;
     }
     //Return true if sum becomes 1
     return (sum==1);
}
//Driver code
int main()
{
    int n = 1234;
    if (isMagic(n))
         cout<< "Magic Number";
    else 
         cout<<"Not a magic number";
    return 0 ;
}
