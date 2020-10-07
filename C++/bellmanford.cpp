#include<iosstream>
#include<vector>
using namespace std;

vector<int> bellman_ford(int n, int src,vector<vector<int> > edges){
// Create vector 
      vector<int> dist(V+1, INT_MAX);
       dist[src]=0;
//relax all edges v-1 times
for( int i=0; i<V-1; i++)
{
    for( auto edge: edges)
    {
        int u = edge[0];
        int v= edge[1];
        int wt = edge[2];
       if(dist[u]! = INT_MAX and dist[u] + wt < dist[v])
       {
            dist[v] = dist[u] + wt;     
        }
    
    }
}
//Negative cycle wt
for( auto edge: edges)
{
    if(dist[u]! = INT_MAX and dist[u] + wt < dist[v]){
        cout << "Negative wt cycle found";
        exit(0);
    }
}
return dist;
}

int main()
{
    int n,m;
    cin>>n>>m;


//Edge list
vector<vector<int> > edges;      // (a,b,3) (c,d,5).......
 for(int i=0; i<m; i++){
     int u,v,wt;
     cin>>u>>v>>wt;
     edges.push_back({u,v,wt});
 }
 //bellman ford
  vector<int> distances = bellman_ford(n,1,edges);
  for(int i=1; i<=n; i++){
      cout<<"Node "<<i<<" is at dist"<<dist[i]<<endl; 
  }
   return 0;
}
