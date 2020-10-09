#include <bits/stdc++.h>
using namespace std;
class Node{
public:
    int data;
    Node *left,*right;
    bool rightThread;
};
Node *createNode(int val){
    Node *newnode = new Node();
    if(!newnode){
        cout<<"memory error";
        return NULL;
    }
    newnode->data=val;
    newnode->left=newnode->right=NULL;
    return newnode;
}
Node *leftmost(Node *n){
    if(n==NULL)
        return NULL;
    while(n->left!=NULL){
        n=n->left;
    }
    return n;
}
void inOrder_threaded(Node *root){
    Node *curr = leftmost(root);
    while(curr!=NULL){
        cout<<curr->data<<" ";
        if(curr->rightThread)
            curr=curr->right;
        else
            curr=leftmost(curr->right);
    }
}
int main()
{
    Node *root = createNode(10);
    root->left = createNode(5);
    root->right = createNode(15);
    root->left->right=root;
    root->left->rightThread=true;
    root->right->left = createNode(12);
    root->right->right = createNode(30);
    root->right->left->right=root->right;
    root->right->left->rightThread=true;
    inOrder_threaded(root);
    return 0;
}
