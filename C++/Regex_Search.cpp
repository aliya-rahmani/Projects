//Implementation of Regex Search in C++
//Codechef Problem Solving
//Link: https://www.codechef.com/problems/ERROR

#include<bits/stdc++.h>
using namespace std;
const int M = 1e9 + 7;
#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);
#define int long long int
#define pb push_back
#define mp make_pair
#define d(x) cout<<x<<"\n"


regex b("101");
regex c("010");

int32_t main(void)
{
    int t;
    cin >> t;

    while (t--)
    {
        string x;
        cin >> x;
        smatch m;
        if (regex_search(x, m, b) || regex_search(x, m, c))
            cout << "Good" << endl;
        else
            cout << "Bad" << endl;

        cout << flush;
    }
    return 0;
}