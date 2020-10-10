//Program to convert a Binary number to its Decimal form and vice-versa

#include<iostream>
#include<math.h>

using namespace std;

int main() {
 int a,g,h,s=0,i=0,d,b,ch;
 cout<<endl<<"Enter the choice-"<<endl<<"1: Binary to Decimal"<<endl<<"2: Decimal to Binary"<<endl;
 cin>>ch;                                                         //Enter choice
 
 switch(ch) {
 
   case 1: cout<<"Enter the Binary Digit"<<endl;                  //Converting Binary to Decimal
           cin>>b;                                                //Enter Binary number
           while(b>0) {
            a=b%10;
            s=s+a*(pow(2,i));
            i=i+1;
            b=b/10;
           }
           cout<<"Answer ="<<s<<endl;
           break;
          
   case 2: cout<<"Enter the Decimal"<<endl;                      //Converting Decimal to Binary
           cin>>d;                                               //Enter Decimal number
           while(d>0) {
            a=d%2;
            a=a*pow(10,i);
            s=s+a;
            i=i+1;
            d=d/2;
           }
           cout<<"Answer ="<<s<<endl;
           break;
          
   default: cout<<"Wrong choice"<<endl;
            break;
  }
  
  return 0;
 } 
