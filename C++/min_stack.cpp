vector<int>s;
MinStack() {
    vector<int>s;
}

void push(int x) {
    s.push_back(x);
}

void pop() {
    s.resize(s.size()-1);
}

int top() {
    return s[s.size()-1];
}

int getMin() {
    return *min_element(s.begin(),s.end());
}




//gfg
stack<int> s; 
    int minEle; 
int _stack :: getMin()
{
    if (s.empty()) 
            return -1; 
  
    // variable minEle stores the minimum element 
    // in the stack. 
    else
    return minEle; 
   //Your code here
}

/*returns poped element from stack*/
int _stack ::pop()
{
    if (s.empty()) 
        { 
            return -1; 
        } 
  
        int t = s.top(); 
        s.pop(); 
        if (t < minEle) 
            { 
                int tt=minEle;
                minEle = 2*minEle - t;
                
                return tt;
            } 

        else
            return t; 
   //Your code here
}

/*push element x into the stack*/
void _stack::push(int x)
{
     if (s.empty()) 
        { 
            minEle = x; 
            s.push(x);  
            return; 
        } 
  
        // If new number is less than minEle 
        if (x < minEle) 
        { 
            s.push(2*x - minEle); 
            minEle = x; 
        } 
  
        else
           s.push(x); 
}
