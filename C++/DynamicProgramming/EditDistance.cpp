#include<bits/stdc++.h>
using namespace std;

int Min(int a, int b, int c) {
    return min(a, min(b, c));
}

int editDistance(string& s1, string& s2) {
    int n = s1.size();
    int m = s2.size();
    vector<vector<int>> dp(2, vector<int>(m+1, 0));
    for(int i = 0; i <= n; i ++) {
        for(int j = 0; j <= m; j ++) {
            if(i == 0) {
                dp[i%2][j] = j;
            }
            else if(j == 0) {
                dp[i%2][j] = i;
            }
            else if(s1[i-1] == s2[j-1]) {
                dp[i%2][j] = dp[(i-1)%2][j-1];
            }
            else {
                dp[i%2][j] = 1 + Min(dp[i%2][j-1], dp[i%2][j-1], dp[(i-1)%2][j-1]);
            }
        }
    }
    return dp[n%2][m];
}

int main(){
    string s1 = "food";
    string s2 = "money";
    cout << editDistance(s1, s2) << endl;
    return 0;
}
