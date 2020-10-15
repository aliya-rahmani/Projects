/* 
    Hoare Partition
    Time Complexity: O(N)
    AUX Space: O(1)

*/ 
#include <iostream>
using namespace std;

int hoare_partition(int arr[], int l, int h) {
    int pivot = arr[l];
    int i = l - 1;
    int j = h + 1;

    while (true) {
        do {
            i++;
        } while (arr[i] < pivot);

        do {
            j--;
        } while (arr[j] > pivot);

        if (i >= j) return j;

        swap(arr[i], arr[j]);

    }
}

int main() {

    return 0;
}