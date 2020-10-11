#include <iostream>

using namespace std;

//Time Complexity - O(N)

int Recursive_Function(int a)
{
    if(a==0)
    {
        return 1;
    }
    else
    {
        return (a*Recursive_Function(a-1));
    }
}

int main()
{
    int N;
    cout<<"Enter the value of N:";
    cin >>N;
    int Factorial = Recursive_Function(N);
    cout<<"Factorial of "<<N<<" is "<<Factorial;
    return 0;
}
