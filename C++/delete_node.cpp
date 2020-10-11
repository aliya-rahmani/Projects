#include<bits/stdc++.h>
using namespace std;

class ListNode
{
    public:
    int val;
    ListNode *next;
    ListNode(int data)
    {
        val=data;
        next=NULL;
    }
};

ListNode* insert_node(ListNode* head,int data)
{
    ListNode *new_node = new ListNode(data);
    new_node->next=head;
    head=new_node;
    return head;
}

void print_list(ListNode *head)
{
    while(head)
    {cout<<head->val<<" ";
    head=head->next;}
    cout<<endl;
}



int main()
{
    ListNode *head;
    head = insert_node(head,1);
    head = insert_node(head,2);
    head = insert_node(head,3);
    head = insert_node(head,4);
    head = insert_node(head,5);

    print_list(head);

}