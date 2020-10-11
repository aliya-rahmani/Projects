#include<bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    Node*left;
    Node*right;
    Node(int x)
    {
        data=x;
        left=NULL;
        right=NULL;
    }
};
struct cmp{
  bool operator()( Node*a, Node*b) {
      return a->data>b->data;
  } 
};
void print(Node*root,string s){
    if(root->left==NULL && root->right==NULL){
        cout<<s<<" ";
        return;
    }
    print(root->left,s+"0");
    print(root->right,s+"1");
}
int main(){
    int t,n;cin>>t;string str;
    while(t--){
        cin>>str;
        n=str.length();int arr[n];
        priority_queue<Node*,vector<Node*>,cmp>pq;
        for(int i=0;i<n;i++){
            cin>>arr[i];
            Node*newnode=new Node(arr[i]);
            pq.push(newnode);
        }
        while(pq.size()!=1){
            Node* m1=pq.top();
            pq.pop();
            Node* m2=pq.top();
            pq.pop();
            Node* temp=new Node(m1->data+m2->data);
            temp->left=m1;
            temp->right=m2;
            pq.push(temp);
        }
       Node* root=pq.top();
        string str="";
        print(root,str);
        cout<<endl;
    }
}
