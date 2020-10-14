#include<bits/stdc++.h>
using namespace std;

int main(){
    long long int n,temp;
    cin>>n;
    long long int v[n]={0};
    long long int two=2,three=3,five=5;
    long long int i2=0,i3=0,i5=0;
    v[0]=1;
    for(int i=1;i<n;i++){
        temp = min(two,min(three,five));
        v[i]=temp;
        if(temp == two){
            i2++;
            two = v[i2]*2;
        }
        if(temp == three){
            i3++;
            three = v[i3]*3;
        }
        if(temp == five){
            i5++;
            five = v[i5]*5;
        }
    }
    cout<<v[n-1];

    return 0;
}