### Check if there's a multiple of N in range [L,R]

> There's a multiple if (L-1) / N != R / N
```
You just have to look at what those folmula means
M / N is the largest integer K such that K * N <= M
which means K * N is the largest multiple of N equal or less than M
the formula is just checking whether largest multiple of N less than L-1 and R are equal or not
if they're NOT equal, the largest mutiple of N less than R must be in the range [L, R]
if they're equal, that means [L, R] contains no multiple of N

```
