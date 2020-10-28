#include<bits/stdc++.h>
using namespace std;

/* KthSmallest works from 1 
    Can handle duplicates */


class BIT {
public:
    int n;
    vector<int> bit;
    BIT(int size) {
        n = size;
        bit.assign(n+1, 0);
    }
    void update(int idx, int val) {
        while(idx <= n) {
            bit[idx] += val;
            idx += (idx&(-idx));
        }
    }
    int sum(int idx) {
        int ans = 0;
        while(idx > 0) {
            ans += bit[idx];
            idx -= (idx&(-idx));
        }
        return ans;
    }
    int sum(int l, int r) {
        return sum(r) - sum(l-1);
    }
    int KthSmallest(int k) {
        int l = 0, r = n;
        while(l < r) {
            int mid = l + (r-l)/2;
            if(k <= sum(mid)) {
                r = mid;
            }
            else {
                l = mid + 1;
            }
        }
        return l;
    }
    int rank(int x) {
        return sum(x);
    }
};

int32_t main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, q; cin >> n >> q;
    BIT bit(n);
    for(int i = 0; i < n; i ++) {
        int x;
        cin >> x;
        bit.update(x, 1);
    }
    int x = 10;
    // Delete
    bit.update(x, -1);

    // Kth Smallest
    bit.KthSmallest(1);

    // Tells count of numbers that are present
    int ans = 0;
    for(int i = 0; i <= n; i ++) {
        if(bit.sum(i, i) >= 1) {
            ans += 1;
        }
    }
    cout << ans << endl;
    return 0;
}