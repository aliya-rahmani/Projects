#include<bits/stdc++.h>
using namespace std;
#define vi vector<int>
#define rep(i,N) for(int (i)=0;i<int(N);i++)
const int OO = 1<<24;
struct unionFind {
	vi rank, parent,setSize;
	int forests;
	unionFind(int nodes) {
		rank.assign(nodes,0);
		parent.assign(nodes,0);
		setSize.assign(nodes,1);
		forests = nodes;	
		rep(i,nodes)parent[i] = i;
	}
	int find_parent(int x) {
		return parent[x]==x?x:find_parent(parent[x]);
	}
	void merge(int x, int y) {
		if (rank[x] > rank[y])swap(x, y);
		parent[x] = y;
		if (rank[x] == rank[y])rank[y]++;
	}
	bool union_set(int x, int y) {
		x = find_parent(x), y = find_parent(y);
		if (x != y) {
			merge(x, y);
			forests--;
			setSize[y] += setSize[x];
		}
		return x != y;
	}
	int sizeOfSet(int i){
	return setSize[find_parent(i)];
	}
};

int main(){
unionFind u(5);
u.union_set(0,1);
u.union_set(2,3);
u.union_set(4,3);
u.union_set(0,3);
cout<<u.sizeOfSet(2);
}
