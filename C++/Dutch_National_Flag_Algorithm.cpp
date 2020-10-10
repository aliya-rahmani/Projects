/*
    Dutch National Flag Algorithm is used to
    Sort an Array of three types of Elements.

    1. Sort an array of 0's, 1's, 2's
    2. There way partition hen multiple occurence of a pivot
    3. Partitioning around a range.

*/

#include <iostream>
using namespace std;

void sort(int arr[], int n) {

    int lo = 0, mid = 0, hi = n - 1;

    while (mid <= hi) {
        switch (arr[mid])
        {
        case 0:
            swap(arr[mid], arr[lo]);
            mid++;
            lo++;
            break;
        
        case 1: 
            mid++;
            break;

        case 2:
            swap(arr[mid], arr[hi]);
            hi--;
            break;

        }
    }

}

int main() {

    int arr[] = {0,1,2,1,1,0,0,2};
    int n = sizeof(arr)/sizeof(arr[0]);

    sort(arr, n);

    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    
    cout << "\n";

    return 0;
}