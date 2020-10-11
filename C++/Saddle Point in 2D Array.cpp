#include <bits/stdc++.h> 
using namespace std; 
  
const int MAX = 100; 
  
bool findSaddlePoint(int mat[MAX][MAX], int n) 
{ 
    for (int i = 0; i < n; i++) 
    { 
        
        int min_row = mat[i][0], col_ind = 0; 
        for (int j = 1; j < n; j++) 
        { 
            if (min_row > mat[i][j]) 
            { 
                min_row = mat[i][j]; 
                col_ind = j; 
            } 
        } 
  
        int k; 
        for (k = 0; k < n; k++) 
  
            if (min_row < mat[k][col_ind]) 
                break; 
  
        if (k == n) 
        { 
           cout << "Value of Saddle Point " << min_row; 
           return true; 
        } 
    } 
  
    return false; 
} 
  
int main() 
{ 
    int mat[MAX][MAX]; 
    int n;
    cout<<"Enter the order of square matrix: ";
    cin>>n;
    cout<<"Enter the elements: \n";
    for (int i=0; i<n; i++)
    {
    	for (int j=0; j<n; j++)
    		cin>>mat[i][j];
	}
    if (findSaddlePoint(mat, n) == false) 
       cout << "No Saddle Point "; 
    return 0; 
}

