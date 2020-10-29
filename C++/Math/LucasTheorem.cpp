#include<bits/stdc++.h>
using namespace std;
#define int long long int

const int mod = (1e6)+3;

class Lucas {
public:
    int p;
    vector<int> fact;
    Lucas(int n) {
        p = n;
        fact.assign(p+1, 1);
        preprocess();
    }
    void preprocess() {
        for(int i = 2; i <= p; i ++) {
            fact[i] = fact[i-1]*i;
            fact[i] %= mod;
        }
    }
    int power(int x, int y)
    {
        int res = 1;
        x = x % p;
        while (y > 0)
        {
            if (y & 1)
                res = (res * x) % p;
            y = y >> 1; 
            x = (x * x) % p;
        }
        return res;
    }

    int modInverse(int n)
    {
        return power(n, p - 2)%p;
    }

    int nCr(int n, int r, int mod) {
        int num = fact[n];
        int den = (modInverse(fact[r]) * modInverse(fact[n-r])) % mod;
        return (num*den)%mod;
    }
    int lucas(int n, int m, int p)
    {
        if (n == 0 && m == 0)
            return 1LL;
        int ni = n % p;
        int mi = m % p;
        if (mi > ni)
            return 0LL;
        return (lucas(n / p, m / p, p) % mod * (nCr(ni, mi, mod) % mod)) % mod;
    }
};

int32_t main() {
    Lucas lc(mod);
}
