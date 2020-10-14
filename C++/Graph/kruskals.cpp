#include<bits/stdc++.h>
using namespace std;

class Edge {
    public:
    int source;
    int dest;
    int weight;
};

bool compare(Edge e1,Edge e2){
    return e1.weight < e2.weight;
}

int findParent(int v,int* parent) {
    if(v == parent[v]) {
        return v;
    }
    return findParent(parent[v],parent);
}

void kruskals(Edge *input,int n,int e) {
    //1.sort the array according to weights
    sort(input,input+e,compare);
    Edge *output = new Edge[n-1]; //output to store the mst source,dest,weights
    int *parent = new int[n]; //union-find technique used,hence taken parent array
    for(int i=0;i<n;i++){
        parent[i] = i;
    }
    int count=0,i=0;
    while(count != n-1) {
        //take the current Edge
        Edge currentEdge = input[i];
        // check if we can add the edge in MST or not
        int sourceParent = findParent(currentEdge.source,parent);
        int destParent = findParent(currentEdge.dest,parent);
        if(sourceParent != destParent) {
            output[count] = currentEdge;
            count++;
            parent[sourceParent] = destParent;
        }
        i++;
    }
    //printing the MST and the cost
    cout<<"#########################################################"<<"\n";
    cout<<"Source"<<"\t"<<"Destination"<<"\t"<<"Weight"<<"\n";
    int cost = 0;
    for(int i=0;i<n-1;i++) {
        if(output[i].source < output[i].dest) {
            cout<<output[i].source<<"\t"<<output[i].dest<<"\t\t"<<output[i].weight<<"\n";
        }
        else{
            cout<<output[i].dest<<"\t"<<output[i].source<<"\t\t"<<output[i].weight<<"\n";
        }
        cost += output[i].weight;
    }
    cout<<"The cost of MST is "<<cost<<"\n";
}


int main() {
    int n,e;
    cin>>n>>e;
    Edge *input = new Edge[e];
    for(int i=0;i<e;i++) {
        int s,d,w;
        cin>>s>>d>>w;
        input[i].source = s;
        input[i].dest = d;
        input[i].weight = w;
    }
    kruskals(input,n,e);
}