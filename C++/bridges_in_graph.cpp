#include<bits/stdc++.h>
using namespace std;
typedef long long ll;


vector<int> arr[300005];
vector<bool> vis(100005, false);
vector<int> in(100005, 0), low(100005, 0);
vector<pair<int, int>> ans;
int timer;
bool flag = false;


void bridge(int node, int par) {
	vis[node] = true;
	in[node] = low[node] = timer++;

	for (auto child : arr[node]) {
		if (child == par)	continue;

		else if (vis[child] == true) {
			low[node] = min(low[node], in[child]);
			if (in[node] > in[child])
			{
				ans.push_back({node, child});
			}
		}

		else {
			bridge(child, node);
			if (in[node] < low[child])
			{
				flag = true;
				return;
			}

			ans.push_back({node, child});
			low[node] = min(low[node], low[child]);
		}
	}
}

void add_edge(int u, int v) {
	arr[u].push_back(v);
	arr[v].push_back(u);
}
signed main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int n, m;
	cin >> n >> m;

	while (m--) {
		int u, v;
		cin >> u >> v;

		add_edge(u, v);
	}

	bridge(1, -1);

	if (flag == 1)
		cout << 0 << endl;
	else {
		for (pair<int, int> p : ans)	cout << p.first << " " << p.second << endl;
	}
	return 0;
}
