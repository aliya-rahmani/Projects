/*** Kosarju's Algorithm ---- Count Strongly connected components in the graph ***/

/*  
    step 1: do dfs taking each node and after finishing pust that node in the stack.
    step 2: transpose the graph(ie reverse the direction of the edges).
    step 3: again fill the visited array to false for second traveral(ie traversal on reversed graph).
    step 4: traverse each element of the  reversed graph and for each dfs made increse the count of strongly connected components.
    Time Complexity O(V+E)
*/

#include<bits/stdc++.h>
using namespace std;

// https://leetcode.com/problems/course-schedule/discuss/249688/Different-O(V%2BE)-solution-using-Kosaraju%27s-algorithm


class Solution {
private:
    vector<vector<int>>graph;
    vector<vector<int>>rgraph;
    stack<int>s;
    vector<bool>visited;
    
    void dfs1(int node){
        visited[node] = true;
        for(auto child:graph[node]){
            if(!visited[child]) dfs1(child);
        }
        s.push(node);
    }
    
    int dfs2(int u){
        visited[u] = true;
        int x = 1;
        for(auto child: rgraph[u]){
            if(!visited[child]){
                x += dfs2(child);
            }
        }
        return x;
    }
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        int n = numCourses;
        graph.resize(n);
        rgraph.resize(n);
        visited.resize(n,false);
        for(int i = 0 ; i < prerequisites.size(); ++i)
        {
            int v = prerequisites[i][0];
            int u = prerequisites[i][1];
            graph[u].push_back(v);
            rgraph[v].push_back(u);
        } 
        for(int i=0;i<n;i++){
            if(!visited[i]) dfs1(i);
        }
        fill(visited.begin(), visited.end(), false);
        while(!s.empty()){
            int u = s.top();
            s.pop();
            if(!visited[u]){
                int size = dfs2(u);
                if(size > 1) return false;
            }
        }
        return true;
    }
};