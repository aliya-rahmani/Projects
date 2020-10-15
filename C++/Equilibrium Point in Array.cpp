#include <bits/stdc++.h>
using namespace std ;

int   equilPoint(int *arr , int n )
{
	
	int sum=0, lowsum=0;

    for (int i=0; i<n; i++){
    	sum += arr[i];
	}
    for (int i=0 ; i<n ; i++)
    {    	
        sum -= arr[i];

        if (lowsum == sum)
			return i;
			
		lowsum += arr[i];
    }
    return -1  ;
}

int main ()
{
    int n ;
    cin >> n ;
    int *arr = new int [n]  ;
    for (int i=0 ; i<n ;i++)
    {
        cin >> arr[i] ;
    }
    int result = equilPoint(arr , n ) ;
    cout << result ;
    delete[] arr ;
    return 0 ;
}
