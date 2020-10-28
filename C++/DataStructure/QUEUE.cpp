

#include <bits/stdc++.h>

using namespace std;

int main()
{
    queue<int>q;
    q.push(10);
    q.push(23);
    q.push(45);
    q.push(4);
    q.push(-8);
    q.push(80);
    cout <<"QUEUE SIZE : "<< q.size() << endl;
    cout << "ELEMENTS IN QUEUE : " << endl;
    while(!q.empty()){
        cout << q.front() << endl;
        q.pop();
    }
    return 0;
}
