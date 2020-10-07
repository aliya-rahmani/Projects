#include <iostream>

using namespace std;

int main()
{
    int i, j, k, n;

    cout << "how much dude? ";
    cin >> n;
    cout << endl;

    for (i = 1; i <= n; i++)

    {
        for (j = 0; j < (n - i); j++)
            cout << "  ";
        for (j = 1; j <= i; j++)
            cout << " *";
        for (k = 1; k < i; k++)
            cout << " *";
        cout << "\n";
    }
    for (i = n - 1; i >= 1; i--)
    {
        for (j = 0; j < (n - i); j++)
            cout << "  ";
        for (j = 1; j <= i; j++)
            cout << " *";
        for (k = 1; k < i; k++)
            cout << " *";
        cout << "\n";
    }
    return 0;
}
