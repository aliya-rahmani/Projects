#include <iostream>


using namespace std;


class items{


    int code[50];
    int price[50];
    int count;


public:

    items();
    int add();
    int remove();
    void display();
    float value();
    int check(int id);


};



int items::add(){


    cout<<"\nEnter code : ";
    cin>>code[count];
    cout<<"Enter price : ";
    cin>>price[count];
    count++;

}

int items::check(int id){

    int temp=0;
    for(int i=0; i<count;i++){

       if(code[i]==id){
            temp=1;
            return i;
       }
    }
    if(temp==0){
        return -1;
    }

}

int items::remove(){

    int id,output;
    cout<<"\nEnter code : ";
    cin>>id;

    output=check(id);
    if (output!=-1){

        code[output]=0;
        price[output]=0;
        
    }
    else{
        cout<<"\nItem not found! "<<endl;
    }

}



float items::value(){

    float total=0;
    for(int i=0;i<count;i++){

       total=total+price[i];

    }
    cout<<"\nTotal value : "<<total<<endl;

}


void items::display(){

    cout<<"\nCode\tPrice\n"<<endl;
    for (int i=0;i<count;i++){

        if(code[i]!=0){
            cout<<code[i]<<"\t"<<price[i]<<endl;
        }

    }


}


items::items(){

    count=0;

}



int main(){

    int choice;
    items order;

    do{
    	cout<<"\n\n1.Add\n2.Delete item\n3.Total Value\n4.Display list\n5.Exit"<<endl;
    	cout<<"-------------------------------------------\n";
        cout<<"\nYour Choice : ";
        cin>>choice;
        
        switch(choice){

        case 1:
            order.add();
            break;
        case 2:
            order.remove();
            break;

        case 3:
            order.value();
            break;

        case 4:
            order.display();
            break;
            
        case 5:
        	exit(0);
        	
        default:
        	cout<<"Error!";

        }

    }while(choice<6);

}



