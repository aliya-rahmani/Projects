#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

long long first(int n) {
    long long binary = 0;
    int remainder, i = 1;
    while (n != 0) {
        remainder = n % 2;
        n /= 2;
        binary += remainder * i;
        i *= 10;
    }
    return binary;
}

int second(long long n) {
    int decimal = 0, i = 0, remainder;
    while (n != 0) {
        remainder = n % 10;
        n /= 10;
        decimal += remainder * pow(2, i);
        ++i;
    }
    return decimal;
}

int third(int decimal)
{
    int octal = 0, i = 1;

    while (decimal != 0)
    {
        octal += (decimal % 8) * i;
        decimal /= 8;
        i *= 10;
    }

    return octal;
}

long long fourth(int octal)
{
    int decimal = 0, i = 0;

    while(octal != 0)
    {
        decimal += (octal%10) * pow(8,i);
        ++i;
        octal/=10;
    }

    i = 1;

    return decimal;
}

long fifth(int n,int base)
{
int remainder, j,i = 0;
char hexadecimal[100];
while (n != 0)
	{
	remainder = n % base;
	if( remainder < 10 )
	{
	hexadecimal[i] = remainder + 48;
	i++;
	}
	else
	{
	hexadecimal[i] = remainder +55;
	i++;
	}
	n /= base;
	}
	cout<<"Decimal to Hexadecimal: ";
	for( j=i-1; j>=0; j--)
	{
	cout<<hexadecimal[j];
	}
	return 0;
}


void sixth()
{
char hexadecimal[20];
long decimal, place;
int i = 0, temp, length;
cout<<"Enter Hexadecimal number: ";
cin>>hexadecimal;
length = strlen(hexadecimal);
decimal = 0;
place = length - 1;
for(i=0; i < length; i++)
	{
	if(hexadecimal[i]>='0' && hexadecimal[i]<='9')
	{
	temp = hexadecimal[i] - 48;
	}
	else if(hexadecimal[i]>='A' && hexadecimal[i]<='F')
	{
	temp = hexadecimal[i] - 65 + 10;
	}
	decimal += temp * pow(16, place);
	place--;
	}
	cout<<"Hexadecimal to Decimal: ";
	cout<<decimal<<endl;
}


int main() {
	int n, cases;
	
	do{
		
    cout<<"\n\n Conversion: \n\n 1.Decimal to Binary\n 2.Binary to Decimal\n 3.Decimal to Octal\n 4.Octal to Decimal\n 5.Decimal to Hexadecimal\n 6.Hexadecimal to Decimal\n 7.Exit\n\n Enter your choice: ";
    cin>>cases;
    cout<<"\n";
    
    switch(cases){
    	case 1:
    		cout<<"Enter a decimal number: ";
    		cin>>n;
			cout<<"Decimal to Binary: ";
			cout<<first(n);
			break;
			
		case 2:
			cout<<"Enter a binary number: ";
    		cin>>n;
			cout<<"Binary to Decimal: ";
			cout<<second(n);
			break;
			
		case 3:
			cout<<"Enter a decimal number: ";
    		cin>>n;
			cout<<"Decimal to Octal: "<<third(n);
			break;
			
		case 4:
			cout<<"Enter a Octal number: ";
    		cin>>n;
			cout<<"Octal to Decimal: "<<fourth(n);
			break;
			
			
		case 5:
			
			cout<<"Enter a decimal number: ";
			cin>>n;
			fifth(n,16);
			cout<<"\n\n";
			break;
			
		case 6:
			sixth();
			cout<<"\n\n";
			break;
		
		case 7:
			exit(0);
			
		default:
			cout<<"Error\n";
			break;
	}
}
while(cases<=7);

    return 0;
}


