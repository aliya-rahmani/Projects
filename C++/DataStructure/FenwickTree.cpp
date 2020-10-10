#pragma comment(linker, "/stack:200000000")
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#define _CRT_SECURE_NO_WARNINGS
#include<bits/stdc++.h>
using namespace std;
const double PI = acos(-1.0);
const double EPS = (1e-9);
typedef long long ll;
#define flush fflush(stdout), cout.flush()
#define all(v) ((v).begin()),((v).end())
#define rall(v) ((v).rbegin()),((v).rend())
#define rep(i,n) for(int(i)=0;(i)<(int)n;(i)++)
#define clr(v,idx) memset(v,idx,sizeof(v));
#define vi vector<int>
#define vll vector<ll>
#define endl '\n'
//const int dx[] = {1,-1,0,0,1,-1,1,-1};
//const int dy[] = {0,0,1,-1,1,-1,-1,1};

class FT {
private: vi ft;
public: FT(int n) { ft.assign(n + 1, 0); }
		int rsq(int b) {
			int sum = 0;
			for (; b; b -= (b&-b))sum += ft[b];
			return sum;
		}
		int rsq(int a, int b) {
			return rsq(b) - (a == 1 ? 0 : rsq(a - 1));
		}
		void adjust(int k, int v) {
			for (; k < (int)ft.size(); k += (k&-k))
				ft[k] += v;
		}
};
int main()
{
	int f[] = { 2,4,5,5,6,6,6,7,7,8,9 };
	FT ft(10);

	rep(i, 11)ft.adjust(f[i], 1);

	cout << ft.rsq(1, 6);
}
