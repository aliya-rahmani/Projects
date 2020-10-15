#include <iostream>

using namespace std;

//Time complexity - O(log N)

//GCD
int GCD(int x,int y)
{
    if (x==0)
    {
        return y;
    }
    return GCD(y%x,x);
}


int main()
{
    int a,b;
    cout<<"Enter the value of a and b:";
    cin>>a>>b;
    int c = GCD(a,b);
    cout<<"GCD of two numbers:"<<c<<endl;
    return 0;
}
