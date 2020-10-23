#include <iostream>
#include <string>

using namespace std;

string cipher(string &);
string decipher(string &);

int main(){
    string str;
    cout<<"Enter String: ";
    getline(cin,str);
    int ty;
    cout<<"Enter 0 to Cipher // 1 to Decipher: ";
    cin>>ty;
    if(!ty){
        str=cipher(str);
    }else{
        str=decipher(str);
    }
    cout<<str<<endl;
    return 0;
}

string cipher(string &str){
    string cr_str="";
    for(char &i:str){
        if(int(i)>=65 && int(i)<=90){
            i+=13;
            if(int(i)>90){
                int tmp=int(i)-90;
                i=64+tmp;
            }
        }
        if(int(i)>=97 && int(i)<=122){
            i+=13;
            if(int(i)>122){
                int tmp=int(i)-122;
                i=96+tmp;
            }
        }
        cr_str+=i;
    }
    return cr_str;
}

string decipher(string &str){
    string cr_str="";
    for(char &i:str){
        if(int(i)>=65 && int(i)<=90){
            i-=13;
            if(int(i)<65){
                int tmp=65-int(i);
                i=91-tmp;
            }
        }
        if(int(i)>=97 && int(i)<=122){
            i-=13;
            if(int(i)<97){
                int tmp=97-int(i);
                i=123-tmp;
            }
        }
        cr_str+=i;
    }
    return cr_str;
}
