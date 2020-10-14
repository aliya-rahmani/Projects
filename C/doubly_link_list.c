#include<stdio.h>
#include<stdlib.h>
struct node
{
    struct node *prev;
    int data;
    struct node *next;
};
struct node* begin_add(struct node* head,int data)
{
    struct node *temp;
    temp=(struct node*)malloc(sizeof(struct node));
    temp->prev=NULL;
    temp->data=data;
    temp->next=head;
    return temp;
}
struct node* middle_add(struct node* head,int data,int n)
{
    struct node *temp;
    temp=(struct node*)malloc(sizeof(struct node));
    temp->prev=NULL;
    temp->data=data;
    temp->next=NULL;
    int i=1;
    struct node* p=head;
    while(i<n-1)
    {
        p=p->next;
        i++;
    }
    temp->next=p->next;
    p->next->prev=temp;
    p->next=temp;
    temp->prev=p;
    return head;
}
struct node* end_add(struct node* head,int data)
{
    struct node* temp;
    temp=(struct node*)malloc(sizeof(struct node));
    temp->prev=NULL;
    temp->data=data;
    temp->next=NULL;
    struct node* p=head;
    while(p->next!=NULL)
      p=p->next;
    p->next=temp;
    temp->prev=p;
    return head;
}
void print_link_list(struct node* head)
{
    struct node* temp=head;
    printf("\nData stored in the link list are\n");
    while(temp!=NULL)
    {
        printf("%d ",temp->data);
        temp=temp->next;
    }
    printf("\n\n");
}
struct node* begin_del(struct node* head)
{
    struct node* temp;
    temp=head;
    head=head->next;
    head->prev=NULL;
    free(temp);
    return head;
}
struct node* middle_del(struct node* head,int n)
{
    struct node* temp;
    struct node* temp1;
    temp=head;
    int i=1;
    while(i<n-1)
    {
        temp=temp->next;
        i++;
    }
    temp1=temp->next;
    temp->next=(temp->next)->next;
    temp1->next->prev=temp;
    free(temp1);
    return head;
}
struct node* end_del(struct node* head)
{
    struct node* temp=head;
    while((temp->next)->next!=NULL)
    {
        temp=temp->next;
    }
    struct node* temp1=temp->next;
    free(temp1);
    temp->next=NULL;
    return head;
}
int main()
{
    struct node* head=NULL;
    int c;
    int data;
    int n;
    do
    {
       printf("\n********INSERTING MENU********\n");
       printf("Enter 1 for adding node in the begining\n");
       printf("Enter 2 for adding node in the middele at nth position\n");
       printf("Enter 3 for adding node in the end\n");
       printf("Enter 4 for stop inserting\n");
       scanf("%d",&c);
       if((c==1)||(c==2)||(c==3))
       {
           printf("Enter the new data : ");
           scanf("%d",&data);
       }
       switch(c)
       {
           case 1:head=begin_add(head,data);
                break;
           case 2:
                printf("Enter the location at which you want to enter the data : ");
                scanf("%d",&n);
                head=middle_add(head,data,n);
                break;
            case 3:head=end_add(head,data);
                break;
            case 4:printf("Exiting inserting process\n");
                break;
            default:printf("Please enter a valid number\n");
       }
       print_link_list(head);
    }while(c!=4);

    do
    {
       printf("\n********DELETION MENU********\n");
       printf("Enter 1 for deleting node in the begining\n");
       printf("Enter 2 for deleting node in the middele at nth position\n");
       printf("Enter 3 for deleting node in the end\n");
       printf("Enter 4 for stoping delection process\n");
       scanf("%d",&c);
       switch(c)
       {
           case 1:head=begin_del(head);
                break;
           case 2:
                printf("Enter the location at which you want to enter the data : ");
                scanf("%d",&n);
                head=middle_del(head,n);
                break;
            case 3:head=end_del(head);
                break;
            case 4:printf("Exiting deletion process\n");
                break;
            default:printf("Please enter a valid number\n");
       }
       print_link_list(head);
    }while(c!=4);
    return 0;
}
