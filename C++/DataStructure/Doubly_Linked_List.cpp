#include<iostream>
#include <cstdlib>
using namespace std;

struct node
{
	int data;
	node*llink;
	node*rlink;
};
struct node*head=NULL;
struct node*temp=NULL;

void create(int element)
{
	node*newnode=new node();
	newnode->data=element;
	newnode->llink=NULL;
	newnode->rlink=NULL;
	
	if(head==NULL)
	{
		head=newnode;
		temp=newnode;
		//cout<<"1";
	}
	
	else
	{
		//cout<<"2";
		temp->rlink=newnode;
		newnode->llink=temp;
		temp=newnode;
	}
}

void insert_at_head(int element)
{
	node*newhead=new node();
	newhead->data=element;
	newhead->llink=NULL;
	newhead->rlink=NULL;
	
	if(head==NULL)
	{
		head=newhead;
		temp=newhead;
	}
	
	else
	{
		head->llink=newhead;
		newhead->rlink=head;
		head=newhead;
	}
	
}

void insert_at_mid(int element,int elementafter)
{
	node*newmid=new node();
	newmid->data=element;
	newmid->llink=NULL;
	newmid->rlink=NULL;
	node*next=new node();
	temp=head;
	
	if(head==NULL)
	{
		head=newmid;
		temp=newmid;
	}
	
	else
	{
		while(temp->data!=elementafter)//user must enter vsalid element after which new ele should be inserted
		{
			temp=temp->rlink;
		}
		next=temp->rlink;
		next->llink=newmid;
		newmid->rlink=next;
		newmid->llink=temp;
		temp->rlink=newmid;
		
	}
	
}

void insert_at_end(int element)
{
	node*newtail=new node();
	newtail->data=element;
	newtail->llink=NULL;
	newtail->rlink=NULL;
	temp=head;
	
	if(head==NULL)
	{
		head=newtail;
		temp=newtail;
	}
	
	else
	{
		while(temp->rlink!=NULL)
		{
			temp=temp->rlink;
		}
		temp->rlink=newtail;
		newtail->llink=temp;
	}
	
}

void delete_at_head()
{
	node*del=new node();
	temp=head;
	
	if(head==NULL)
	{
		cout<<"DLL Empty";
	}
	else
	{
		del=head;
		head=head->rlink;
		head->llink=NULL;
		free(del);	
	}	
}

void delete_at_mid(int element)
{
	node*del=new node();
	node*prev=new node();
	node*next=new node();
	temp=head;
	
	if(head==NULL)
	{
		cout<<"DLL Empty";
	}
	
	else
	{
		while(temp!=NULL)
		{
			if(temp->data==element)
			{
				next=temp->rlink;
				prev=temp->llink;
				del=temp;
				prev->rlink=next;
				next->llink=prev;
				free(del);
			}
			else
			{
				temp=temp->rlink;
			}
		}
	}
}

void delete_at_end()
{
	node*del=new node();
	node*prev=new node();
	temp=head;
	
	if(head==NULL)
	{
		cout<<"DLL Empty";
	}
	else
	{
		while(temp->rlink!=NULL)
		{
			temp=temp->rlink;
		}
		cout<<temp->data<<" is deleted"<<endl;
		prev=temp->llink;
		prev->rlink=NULL;
		free(temp);
	}
	
}
void display()
{
	if(head==NULL)
	{
		cout<<"DLL Empty";
	}
	else
	{
		temp=head;
		
		while(temp!=NULL)
		{
			//cout<<"1";
			cout<<temp->data<<" ";
			temp=temp->rlink;
		}
		cout<<endl;
	}
}

int main()
{
    int n,a,i;
    cout<<"Enter the no of initial elements in the DLL (n):";
    cin>>n;
    cout<<"Enter the elements:";
    for(i=0;i<n;i++)
    {cin>>a;
    create(a);
    }
    display();
    
    insert_at_head(404);
    cout<<"The DLL after insertion at head is:";
    display();
    cout<<endl;
    
    insert_at_end(420);
    cout<<"The DLL after insertion at tail is:";
    display();
    cout<<endl;
    
    insert_at_mid(100,3);//3 is the element after which 100 will be inserted,NOT position
    cout<<"The DLL after insertion at mid is:";
    display();
    cout<<endl;
    
    delete_at_head();
    cout<<"The DLL after deletion at head is:";
    display();
    cout<<endl;
    
    delete_at_end();
    cout<<"The DLL after deletion at tail is:";
    display();
    cout<<endl;
    
    delete_at_mid(100);//ele to hbge deleted
    cout<<"The DLL after deletion at mid is:";
    display();
    cout<<endl;
}

/* REFER FOR CREATION OF FUNCTION FOR MULTI LIST USUAGE (L5P1DLL.CPP)
//For creation of DLL create(a,&head1);
void create(int element,node**head)
{
	node*newnode=new node();
	newnode->data=element;
	newnode->llink=NULL;
	newnode->rlink=NULL;

	if(*head==NULL)
	{
		*head=newnode;
		temp=newnode;
		//cout<<"1";
	}
	
	else
	{
		//cout<<"2";
		temp->rlink=newnode;
		newnode->llink=temp;
		temp=newnode;
	}
}*/
