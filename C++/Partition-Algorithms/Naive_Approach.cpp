// Naive Solution to Implement Partition Algorithm

#include <bits/stdc++.h>
using namespace std;

void partition(int* arr, int l, int h, int p) {
    int temp[h-l+1], index = 0;

    for (int i = 0; i <= h; i++) {
        if (arr[i] <= arr[p])
            temp[index++] = arr[i];
    }

    for (int i = 0; i <= h; i++) {
        if (arr[i] > arr[p])
            temp[index++] = arr[i];
    }

    for (int i = l; i <= h; i++) {
        arr[i] = temp[i - l];
    }

} 

int main () {

    int arr[] = {5,13,6,9,12,11,8};
    int l = 0;
    int h = sizeof(arr)/sizeof(int);
    int p = 6;

    partition(arr, l, h, p);

    for (int i = 0; i < h; i++) {
        cout << arr[i] << " ";
    }

    cout << "\n";

    return 0;
}