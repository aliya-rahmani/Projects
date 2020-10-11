

#include <stdio.h>
#include <stdlib.h>

struct node 
{
    struct node *prev;
    int data;
    struct node *next;
};
struct node *head=NULL;

struct node* create(int a[],int n)
{
  struct node *t,*newnode;
  int i;
  newnode=(struct node*)malloc(sizeof(struct node)); 
  head=newnode;
  newnode->data=a[0];
  newnode->next=NULL;
  newnode->prev=NULL;
  t=head;
  
  for(i=1;i<n;i++)
  {
      newnode=(struct node*)malloc(sizeof(struct node));
      newnode->data=a[i];
      newnode->prev=t;
      t->next=newnode;
      t=t->next;
      newnode->next=NULL; 
  }
  return head;
}

void display(struct node *p)
{
    while(p!=NULL)
    {
        printf("%d ",p->data);
        p=p->next;
    }
}

void displayrev(struct node *p)
{
    while(p!=NULL)
    {
        printf("%d ",p->data);
        p=p->prev;
    }
}


void reverse(struct node *p)
{
    while(p->next!=NULL)
    {
        p=p->next;
    }
    displayrev(p);
}

int main()
{   struct node *p;
    int a[]={1,2,3,4,5,6};
    
    p=create(a,6);
    display(head);
    printf("\n");
    reverse(p);
    return 0;
}
