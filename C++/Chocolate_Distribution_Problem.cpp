// Chocolate Distribution Problem

/*
    In this problem the Packets of different sizes are need to be
     distributed among childrens so that each child gets exactly one packet
*/

#include <iostream>
#include <algorithm>
using namespace std;

// m : No. of children
int chocolate_distribution_problem(int arr[], int n, int m) {

    if (m > n) return -1;

    sort(arr, arr+n);

    int res = arr[m-1] - arr[0];

    for (int i = 1; (i + m - 1) < n; i++)
        res = min(res, (arr[i+m-1] - arr[i]));

    return res;
}

int main() {

    int arr[] = {7,3,2,4,9,12,56};
    int n = sizeof(arr)/sizeof(arr[0]);

    cout << chocolate_distribution_problem(arr, n, 3) << "\n";

    return 0;
}