#   CodeChef Problem
#   https://www.codechef.com/problems/ERROR
#   Using Regex search

import re
Pat1=r"010"
Pat2=r"101"
t=int(input())
while(t):
    x=input()
    if(re.search(Pat1,x) or re.search(Pat2,x)) :
        print("Good")
    else :
        print("Bad")
    t=t-1