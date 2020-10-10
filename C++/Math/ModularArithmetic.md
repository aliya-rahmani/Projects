> Facts
+ a % n (for +ve)
+ (a % n + n) % n (for +ve,-ve)
+ when -ve result => result = (result + n) % n
+ if a % n = b % n => (a - b) % n = 0
+ largest n such that a % n = b % n is n = b - a
+ (a % n) % n = a % n
+ (n ^ x) % n = 0 for any x >= 0
+ (a + b) % n = (a % n + b % n) % n
+ (a * b) % n = (a % n * b % n) % n
+ x % (a + b) != x % a + a % b
+ (a ^ b) % n = ((a % n) ^ b) % n
+ (a ^ b) % n = ((a ^ x) % n * (a ^ x) % n) % n where x = b / 2
+ (a % 2 ^ n) = a & (n - 1)
+ bool isOdd(int n) { return n & 1; } cuz n % 2 =-1 if n < 0
+ powers of 2 has cycles in the last m digits [google it]
