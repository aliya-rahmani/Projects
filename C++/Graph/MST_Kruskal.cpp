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

struct edge {
	int from, to, w;
	edge(int from, int to, int w) :from(from), to(to), w(w) {};
	bool operator < (const edge & e)const {
		return e.w < w;
	}
};

bool comp(edge a, edge b) {
	return a.w < b.w;
}

bool inMST[10000];
pair<int,vector<edge> > MST_kruskal(vector<edge>list, int nodes) {
	unionFind uf(nodes);
	vector<edge>edges;
	int mstCost = 0;
	rep(i,list.size()) {
		edge e = list[i];
		if (uf.union_set(e.from, e.to))
			mstCost += e.w, edges.push_back(e),inMST[i]=1;
	}
	if (uf.forests != 1)return make_pair( -OO,vector<edge>());
	return{ mstCost,edges };
}

int second(vector<edge>list,int nodes,int skip) {
	unionFind u(nodes);
	int cost = 0,taken=0;
	rep(i, list.size()) {
		if (i != skip && u.union_set(list[i].from, list[i].to))
			cost += list[i].w,taken++;
	}
	if (u.forests != 1)return OO;
	return cost;
}
int main(){


}
