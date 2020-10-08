#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *next;
};
struct node* begin_add(struct node* head,int data)
{
    struct node *temp;
    temp=(struct node*)malloc(sizeof(struct node));
    temp->data=data;
    temp->next=head;
    return temp;
}
struct node* middle_add(struct node* head,int data,int n)
{
    struct node *temp;
    temp=(struct node*)malloc(sizeof(struct node));
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
    p->next=temp;
    return head;
}
struct node* end_add(struct node* head,int data)
{
    struct node* temp;
    temp=(struct node*)malloc(sizeof(struct node));
    temp->data=data;
    temp->next=NULL;
    struct node* p=head;
    while(p->next!=NULL)
      p=p->next;
    p->next=temp;
    return head;
}
void print_link_list(struct node* head)
{
    struct node* temp=head;
    printf("\nData stored in the singly link list are\n");
    while(temp!=NULL)
    {
        printf("%d ",temp->data);
        temp=temp->next;
    }
    printf("\n\n");
}
struct node* concatenate(struct node* head1,struct node* head2)
{
    struct node* temp=head1;
    while(temp->next!=NULL)
       temp=temp->next;

    temp->next=head2;
    return head1;
}
int main()
{
    struct node* head1=NULL;
    int c;
    int data;
    int n;

    printf("Enter nodes in link list 1\n");
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
           case 1:head1=begin_add(head1,data);
                break;
           case 2:
                printf("Enter the location at which you want to enter the data : ");
                scanf("%d",&n);
                head1=middle_add(head1,data,n);
                break;
            case 3:head1=end_add(head1,data);
                break;
            case 4:printf("Exiting inserting process\n");
                break;
            default:printf("Please enter a valid number\n");
       }
       print_link_list(head1);
    }while(c!=4);

    printf("Enter nodes in link list 2\n");
    struct node* head2=NULL;
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
           case 1:head2=begin_add(head2,data);
                break;
           case 2:
                printf("Enter the location at which you want to enter the data : ");
                scanf("%d",&n);
                head2=middle_add(head2,data,n);
                break;
            case 3:head2=end_add(head2,data);
                break;
            case 4:printf("Exiting inserting process\n");
                break;
            default:printf("Please enter a valid number\n");
       }
       print_link_list(head2);
    }while(c!=4);

    printf("Concatenating linklist 2 at the end of list list 1\n");
    head1=concatenate(head1,head2);

    printf("\nfinal link list after concatenating is as follows");
    print_link_list(head1);

     return 0;
}
