#define MOD 1000000007
typedef long long ll;

ll power(ll x, ll y) 
{ 
    ll res = 1; 
  
    x = x % MOD; 
  
    while (y > 0) 
    { 
        if (y & 1) res = (res*x) % MOD; 
          y = y>>1;
        x = (x*x) %MOD;   
    } 
    return res; 
} 
