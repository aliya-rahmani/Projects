#include<bits/stdc++.h>
using namespace std;

int getKey()
{
    int n = -1;
    cin >> n;
    n = n%26;
    if(n < 0)
        n = 26 + n;
    return n;
}

vector< string > getRotatedText(vector< string > text, int key, bool decipher)
{
    string s;
    vector< string > rotatedText;

    for(int iter = 0; iter < text.size(); iter++){
        s = text[iter];
        for(int i=0; i<s.length(); i++){
            if(s[i] >= 'A' && s[i] <= 'Z')
                s[i] = ((s[i] - 'A' + key)%26) + 'A';
            else if(s[i] >= 'a' && s[i] <= 'z')
                s[i] = ((s[i] - 'a' + key)%26) + 'a';
            else if(s[i] >= '0' && s[i] <= '9'){
                if(decipher)
                    s[i] = ((s[i] - '0' - (26 - key))%10) < 0 ? (((s[i] - '0' - (26 - key))%10) + 10) + '0': ((s[i] - '0' - (26 - key))%10) + '0';
                else
                    s[i] = ((s[i] - '0' + key)%10) + '0';
            }
        }
        rotatedText.push_back(s);
    }
    return rotatedText;
}

void encipherment(string str, int key, bool decipher = false)
{
    if(decipher)
        key = 26-key;

    vector<string> text;
    text.push_back(str);

    vector< string > rotatedText = getRotatedText(text, key, decipher);
    for(int i=0; i<rotatedText.size(); i++){
        cout << rotatedText[i] << endl;
    }
    return;
}

int main()
{
	int choice,key;
	bool isRunning = true;
	string text;

	cout << "********PROGRAM TO IMPLEMENT CEASER CIPHER********\n\n";

	while(isRunning){

        cout << "Enter the operation to be performed:\n";
        cout << "1.Convert Plain Text to Cipher Text.\n";
        cout << "2.Convert Cipher Text to Plain Text.\n";
        cout << "3.Quit\n";
        cin >> choice;

        switch(choice)
        {
            case 1:
                cout << "Enter the value of key Between 1 and 25 included:";
                key = getKey();
                cout << "\n*******************************************\n";
                cout << "Enter the plain text: \n";
                cin.ignore();
                getline(cin, text);
                encipherment(text, key);
                cout << "*****CIPHERTEXT GENERATED SUCCESSFULLY*****\n\n";
                break;

            case 2:
                cout << "Enter the value of key Between 1 and 25 included:";
                key = getKey();
                cout << "\n*******************************************\n";
                cout << "Enter the cipher text: \n";
                cin.ignore();
                getline(cin, text);
                encipherment(text, key, true);
                cout << "*****PLAINTEXT GENERATED SUCCESSFULLY*****\n\n";
                break;

            case 3:
                isRunning = false;
                break;

            default:
                printf("No such operation available.\n");
                break;
        }
	}
	return 0;
}
