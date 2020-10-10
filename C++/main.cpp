#include <bits/stdc++.h>
using namespace std;
class Node{
public:
    int data;
    Node *left;
    Node *right;
};
Node *createNode(int val){
    Node *newnode = new Node();
    if(!newnode){
        cout<<"Memory error";
        return NULL;
    }
    newnode->data=val;
    newnode->left=newnode->right=NULL;
    return newnode;
}
Node *insertNode(Node *root,int val){
    if(root==NULL){
        root = createNode(val);
        return root;
    }
    queue <Node*> q;
    q.push(root);
    while(!q.empty()){
        Node *nx = q.front();
        q.pop();
        if(nx->left!=NULL)
            q.push(nx->left);
        else{
            nx->left=createNode(val);
            return root;
        }
        if(nx->right!=NULL)
            q.push(nx->right);
        else{
            nx->right=createNode(val);
            return root;
        }
    }
}
void inorder(Node *root){
    if(root==NULL)
        return;
    inorder(root->left);
    cout<<root->data<<" ";
    inorder(root->right);
}
int height(Node *root){
    if(root==NULL)
        return 0;
    int lh = height(root->left);
    int rh = height(root->right);
    return 1 + max(lh,rh);
}
bool childrenSum(Node *root){
    //root->left->data + root->right->data !=root->data :: return false
    if(root==NULL)
        return true;
    if(root->left==NULL && root->right==NULL){
        return true;
    }
    if(root->left==NULL && root->right!=NULL){
        if(root->right->data!=root->data)
            return false;
    }
    if(root->left!=NULL && root->right==NULL){
        if(root->left->data!=root->data)
            return false;
    }
    if(root->left!=NULL && root->right!=NULL){
        if(root->left->data+root->right->data!=root->data)
            return false;
    }
    bool left = childrenSum(root->left);
    bool right = childrenSum(root->right);
    bool res = left&&right;
    return res;
}
bool isBalanced(Node *root){
    if(root==NULL)
        return true;
    if(root->left==NULL&&root->right==NULL)
        return true;
    int ht_left = height(root->left);
    int ht_right = height(root->right);
    cout<<"\nLeft height: "<<ht_left<<"\nRight height: "<<ht_right<<"\n";
    if(max(ht_left,ht_right)-min(ht_left,ht_right) > 1)
        return false;
    else
        return isBalanced(root->left)&&isBalanced(root->right);
}
bool isBalanced_faster(Node *root,int *height){
    if(root==NULL){
        *height=0;
        return true;
    }
    int lh=0,rh=0;
    bool lb=isBalanced_faster(root->left,&lh);
    bool rb=isBalanced_faster(root->right,&rh);
    if(abs(lh-rh)>1)
        return false;
    *height = max(lh,rh)+1;
    return (lb&&rb);
}
void printK(Node *root,int k){
    if(root==NULL)
        return;
    if(k==0)
        cout<<root->data<<" ";
    printK(root->left,k-1);
    printK(root->right,k-1);
}
bool isBST(Node *root,Node *left,Node *right){
    if(root==NULL)
        return true;
    if(left!=NULL && root->data<=left->data)
        return false;
    if(right!=NULL && root->data>=right->data)
        return false;
    return (isBST(root->left,left,root)&&isBST(root->right,root,right));
}
int main()
{
    Node *root = createNode(10);
    root->left = createNode(5);
    root->right = createNode(3);
    root->right->right = createNode(4);
    //root->right->left = createNode(2);
    root->left->left=createNode(1);
    root->left->left->left=createNode(3);
    //root->left->right->left=createNode(3);
    //Node * root = createNode(10);
    //root->left=createNode(10);
    inorder(root);
    cout<<endl;
    int x = height(root);
    cout<<"Height is: "<<x<<endl;
    bool res = isBalanced_faster(root,&x);
    //bool res = isBalanced(root);
    if(res)
        cout<<"True";
    else
        cout<<"False";
    cout<<endl;
    printK(root,1);
    cout<<"\nChecking if a tree is BST: \n";
    bool out = isBST(root,NULL,NULL);
    if(out)
        cout<<"It's a binary tree.";
    else
        cout<<"It's not a binary tree.";

    return 0;
}
