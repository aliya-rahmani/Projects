#include <iostream>

using namespace std;

int binary_search(int array[], int size, int value)
{
    int begin = 0;
    int end = size - 1;

    int middle;

    while (begin <= end)
    {
        middle = (begin + end) / 2;

        if (value < array[middle])
        {
            end = middle - 1;
        }
        else if (value > array[middle])
        {
            begin = middle + 1;
        }
        else
        {
            return middle;
        }
    }

    return -1;
}

int main()
{
    int value;

    int array[] = {1, 4, 54, 87, 94, 21, 36, 45, 87, 98};
    int size = (sizeof(array) / sizeof(int));

    cout << "Number to search: " << endl;
    cin >> value;

    int result = binary_search(array, size, value);

    if (result >= 0)
    {
        cout << "The value " << array[result] << " was found";
    }
    else
    {
        cout << "The value " << value << " was not found";
    }
}