// Program to perform Lamuto Partition
// Time Complexity: O(N)
// Aux Space: O(1)

#include <iostream>
using namespace std;

#define foo(i, n) for(int i = 0; i < n; i++)


// If the pivot element is the last element
void lamuto_partition(int arr[], int l, int h) {
    int pivot = arr[h];
    int i = l - 1;

    for (int j = l; j <= h - 1; j++ ) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }

    swap(arr[i + 1], arr[h]);
}

// If the pivot element is not the last element
void lamuto_partition(int arr[], int l, int h, int p) {
    swap(arr[p], arr[h]);
    lamuto_partition(arr, l, h);
}


int main() {

    int arr[] = {10, 80, 30, 90, 40, 50, 70};
    int n = sizeof(arr)/sizeof(int);

    int l = 0;
    int h = n - 1;

    foo(i, n) {
        cout << arr[i] << " ";
    }

    cout << "\n";

    cout << "After Partitioning...\n";

    lamuto_partition(arr, l, h);

    foo(i, n) {
        cout << arr[i] << " ";
    }

    cout <<"\n";

    foo(i, n) {
        cout << arr[i] << " ";
    }

    cout << "\n";

    cout << "After Partitioning...\n";

    lamuto_partition(arr, l, h, 3);

    foo(i, n) {
        cout << arr[i] << " ";
    }

    cout <<"\n";

    return 0;
}