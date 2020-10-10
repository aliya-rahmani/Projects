#include<bits/stdc++.h>
using namespace std;

// implementing avl tree (self balancing binary search tree)
struct node {
	int data;
	node* right;
	node* left;
	int height;
};

// function finding the height of the tree
int height(node* n) {
	if (n == NULL)
		return 0;
	else
		return n->height;
}

// returning the balance factor of the tree
int getBalance(node* n) {
	if (n == NULL)
		return 0;
	else
		return (height(n->left) - height(n->right));
}

//utility function to implement the right-rotate case
node* right_rotate(node* y) {
	node* x = y->left;
	node* t2 = x->right;

	x->right = y;
	y->left = t2;

	x->height = 1 + max(height(x->left), height(x->right));
	y->height = 1 + max(height(y->left), height(y->right));

	return x;
}

//utility function to implement the left rotate case
node* left_rotate(node* x) {
	node* y = x->right;
	node* t1 = y->left;

	y->left = x;
	x->right = t1;


	x->height = 1 + max(height(x->left), height(x->right));
	y->height = 1 + max(height(y->left), height(y->right));

	return y;
}

//utility function to implement insertion
node* insert(node* root, int data) {
	node* ptr = new node;
	ptr->data = data;
	ptr->right = ptr->left = NULL;
	ptr->height = 1;

	// implementing simple bst operations
	if (root == NULL) {
		root = ptr;
		return root;
	}
	if (data < root->data) {
		root->left = insert(root->left, data);
	}
	else if (data > root->data) {
		root->right = insert(root->right, data);
	}
	else
		return root;

	root->height = 1 + max(height(root->left), height(root->right));
	int balance = getBalance(root);

	// left left case
	if (balance > 1 && data < root->left->data)
		return right_rotate(root);
	if (balance < -1 && data > root->right->data)
		return left_rotate(root);
	if (balance > 1 && data > root->left->data)
	{
		root->left = left_rotate(root->left);
		return right_rotate(root);
	}
	if (balance < -1 && data < root->right->data) {
		root->right = right_rotate(root->right);
		return left_rotate(root);
	}

	return root;
}
node* minVal(node* n) {
	node* curr = n;
	while (curr->left != NULL)
		curr = curr->left;
	return curr;
}
// utility funcion for node deletion
node* delete_avl(node* root, int data) {
	if (root == NULL)
		return NULL;
	if (data < root->data) {
		root->left = delete_avl(root->left, data);
	}
	else if (data > root->data) {
		root->right = delete_avl(root->right, data);
	}
	// if the data == root->data

	else {
		// if the node has no child or 1 child
		if ((root->left == NULL) || (root->right == NULL))
		{
			node* temp = root->left ? root->left : root->right;
			if (temp == NULL)
			{
				temp = root;
				root = NULL;
				delete(temp);
			}
			else {
				*root = *temp;
				delete(temp);
			}
		}
		// node has both the children
		else {
			node* inord_succ = minVal(root->right);
			root->data = inord_succ->data;

			root->right = delete_avl(root->right, inord_succ->data);
		}
	}
	if (root == NULL)
		return root;

	root->height = 1 + max(height(root->left), height(root->right));
	int balance = getBalance(root);

	// left left case
	if (balance > 1 && getBalance(root->left) >= 0)
		return right_rotate(root);
	if (balance < -1 && getBalance(root->right) <= 0)
		return left_rotate(root);
	if (balance > 1 && getBalance(root->left) < 0)
	{
		root->left = left_rotate(root->left);
		return right_rotate(root);
	}
	if (balance < -1 && getBalance(root->right) > 0) {
		root->right = right_rotate(root->right);
		return left_rotate(root);
	}

	return root;
}

void preorder(node* root) {
	if (root == NULL)
		return;
	else {
		cout << root->data << " ";
		preorder(root->left);
		preorder(root->right);
	}
}
signed main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	node* root = new node;
	root = NULL;

	root = insert(root, 6);
	root = insert(root, 7);
	root = insert(root, 8);

	preorder(root);
	cout << "\n";
	root = delete_avl(root, 6);

	preorder(root);
	return 0;
}
