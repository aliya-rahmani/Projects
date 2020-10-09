#include <iostream>

using namespace std;

int fibonnaci_function(int x) 
{
   if((x==1)||(x==0))
      {
        return(x);
      }else 
       {
         return(fibonnaci_function(x-1)+fibonnaci_function(x-2));
       }
}


int main() 
{
   int place , i=0;

   cout << "Enter the number of terms to print the series : "<<endl;
   cin >> place;

   cout << "Fibonnaci Series is : "<<endl;

   while(i < x) {

      cout <<" "<<fibonnaci_function(i);
      i++;
   }

   return 0;
}