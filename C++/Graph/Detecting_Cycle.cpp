bool cycle;
 
void dfs(int u){
    vis[u] = 1;
    for(int nxt : adj[u]){
        if(!vis[nxt]){
            dfs(nxt);
        }else if(vis[nxt] == 1){
            cycle = true;
        }
    }
    vis[u] = 2;
}
