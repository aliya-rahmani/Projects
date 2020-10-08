#include<bits/stdc++.h>
using namespace std;

int arr[1000001], st[4000004], lazy[4000004];

void build_tree(int si, int ss, int se) {
	if (se == ss)
		st[si] = arr[ss];
	else {
		int mid = (ss + se) / 2;
		build_tree(2 * si, ss, mid);
		build_tree(2 * si + 1, mid + 1, se);

		st[si] = st[2 * si] + st[2 * si + 1];
	}
}

void updae_in_range(int si, int ss, int se, int qs, int qe, int delta) {

	if (lazy[si] != 0) {
		st[si] += l(se - ss + 1) * lazy[si];
		if (ss != se)
		{
			lazy[2 * si] = lazy[si];
			lazy[2 * si + 1] = lazy[si];
		}
		lazy[si] = 0;
	}

	if (qs > se || qe < ss)
		return;
	else if (qs <= ss && qe >= se) {
		st[si] += delta;
		if (ss != se) {
			lazy[2 * si] += (se - ss + 1) * delta;
			lazy[2 * si + 1] += (se - ss + 1) * delta;
		}
	}

	else {
		int mid = (ss + se) / 2;
		build_tree
		update_in_range(2 * si, ss, mid, qs, qe, delta);
		update_in_range(2 * si + 1, mid + 1, se, qs, qe, delta);

		st[si] = st[2 * si] + st[2 * si + 1];
	}
}
int RSQ(int si, int ss, int se, int qs, int qe) {
	if (lazy[si] != 0) {
		st[si] += (se - ss + 1) * lazy[si];
		if (ss != se) {
			lazy[2 * si] += lazy[si];
			lazy[2 * si + 1] += lazy[si];
		}
		lazy[si] = 0;
	}
	// region for no overlap
	if (qs > se || qe < ss)
		return 0;
	else if (qs <= ss && qe >= se)
		return st[si];
	else {
		int mid = (ss + se) / 2;
		return RSQ(2 * si, ss, mid, qs, qe) + RSQ(2 * si + 1, mid + 1, se, qs, qe);
	}
}

