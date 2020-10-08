#include <iostream>
using namespace std;
class studData;
class student{
	string name;
	int roll_no;
	string cls;
	char* division;
	string dob;
	char* bloodgroup;
	static int count;
public:
	student(){       //default constructor
		name="";
		roll_no=0;
		cls="";
		division=new char;
		dob="dd/mm/yyyy";
		bloodgroup=new char[4];
	}
	~student(){
		delete division;
		delete[] bloodgroup;
	}
	static int getcount(){
		return count;
	}
	void getData(studData*);
	void dispData(studData*);
};
class studData{
	string contact_address;
	long int* teleno;
	long int* dlno;
	friend class student;

public:
	studData(){
		contact_address="";
		teleno=new long;
		dlno=new long;
	}
	~studData(){
		delete teleno;
		delete dlno;
	}
	void getstudData(){
		cout<<"Enter contact address: ";
		cin.get();
		getline(cin,contact_address);
		cout<<"Enter telephone number: ";
		cin>>*teleno;
		cout<<"Enter driving license number: ";
		cin>>*dlno;
	}
	void dispstudData(){
		cout<<"contact address: "<<contact_address<<endl;
		cout<<"Telephone number: "<<*teleno<<endl;
		cout<<"Driving license: "<<*dlno<<endl;
	}
};
inline void student::getData(studData*st){
	cout<<"Enter student name: ";
	getline(cin,name);
	cout<<"Enter roll number ";
	cin>>roll_no;
	cout<<"enter class: ";
	cin.get();
	getline(cin,cls);
	cout<<"Enter division: ";
	cin>>division;
	cout<<"Enter dob: ";
	cin.get();
	getline(cin,dob);
	cout<<"enter blood group: ";
	cin>>bloodgroup;
	st->getstudData();
	count++;

}
inline void student::dispData(studData*st1){
	cout<<"student name"<<name<<endl;
	cout<<"Roll number"<<roll_no<<endl;
	cout<<"class: "<<cls<<endl;
	cout<<"division: "<<division<<endl;
	cout<<"DOB"<<dob<<endl;
	cout<<"Blood group: "<<bloodgroup<<endl;
	st1->dispstudData();
}
int student::count;
int main(){
	student* stud1[100];
	studData* stud2[100];
	int n=0;
	char ch;
	do{
			stud1[n]=new student;
			stud2[n]=new studData;
			stud1[n]->getData(stud2[n]);
			n++;
			cout<<"Do you want to add another student?(Y/N): ";
			cin>>ch;
			cin.get();
	}while(ch=='y'||ch=='Y');
	for(int i=0;i<n;i++){
		cout<<"---------------------------"<<endl;
		stud1[i]->dispData(stud2[i]);
	}
	cout<<"-------------------------------"<<endl;
	cout<<"Total student: "<<student::getcount();
	cout<<"--------------------------------";
	for (int i = 0; i < n; i++)
	{
		delete stud1[i];
		delete stud2[i];
	}
	return 0;	
}
