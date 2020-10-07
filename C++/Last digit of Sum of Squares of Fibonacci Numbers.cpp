#include <iostream>

int fibonacci_sum_naive(long long n) {
    n %= 60;

    if (n <= 1)
        return n;

    long long previous = 0, current = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = (tmp_previous + current);
    }

    return current % 10;
}

int fibonacci_sum_squares_naive(long long n) {
    int a = fibonacci_sum_naive(n), b = fibonacci_sum_naive(n+1);
    return (a * b) % 10;
}

int main() {
    long long n = 0;
    std::cin >> n;
    std::cout << fibonacci_sum_squares_naive(n);
}
