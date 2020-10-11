int cap;
list<pair<int,int>>l;                                   //store the most recent in the front and least recent at the back.
unordered_map<int,list<pair<int,int>>::iterator>mp;     //for each key keep an iterator to its location in list for quick access.
LRUCache(int capacity) {
    cap = capacity;
}

int get(int key) {
    if(mp.find(key)==mp.end()) return -1;          //if the key is not present in map return -1.
    auto it = mp[key];
    int ans = (*it).second;
    l.erase(it);                                   //if it is already present then erase from the list and put it in the front or most recent.
    l.push_front({key,ans});                       //put it in the front.
    mp[key] = l.begin();                           //update the value in map also.
    return ans;
}

void put(int key, int value) {
    if(mp.find(key)!=mp.end())                     //if the key is already present in map then erase it and bring it to the front.
    {   
        auto it=mp[key];
        l.erase(it);
    }
    l.push_front({key,value});
    mp[key] = l.begin();            //after bringing to the front update the iterator in the map.
    if(l.size()>cap)                //if list size exceeds capacity then delete from the back (least recently used) and remove this key from the map.
    {
        auto x = l.back();
        mp.erase(x.first);
        l.pop_back();
    }
}
