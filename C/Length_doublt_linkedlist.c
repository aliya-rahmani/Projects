

#include <stdio.h>
#include <stdlib.h>

struct node 
{
    int data;
    struct node *next;
    struct node *prev;
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



void length(struct node *p)
{int len=0;
    while(p!=NULL)
    {
        len++;
        p=p->next;
    }
    printf("\nlength is = %d",len);
}

int main()
{   struct node *p;
    int a[]={1,2,3,4,5,6};
    
    p=create(a,6);
    display(head);
    length(p);
    return 0;
}
