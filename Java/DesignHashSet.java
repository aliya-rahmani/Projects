/*
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 

contains(value) : Return whether the value exists in the HashSet or not.

remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Constraints

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.

Example

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

*/
import java.util.*;
class MyHashSet {

    /** Initialize your data structure here. */
    HashMap map = new HashMap();

    /**  To instantiate the object that is created. */
    public MyHashSet() {
        
    }
    private static final Object PRESENT = new Object();
    
    
    public void add(int key) {
        
        if (map.put(key, PRESENT) == null)
        {
            map.put(key,PRESENT);
        }
        
    }
    
    public void remove(int key) {
        
        map.remove(key);
        
    }
    
    /** Returns true if this set contains the specified element */
    public boolean contains(int key) {
        
        return map.containsKey(key);
        
    }
}
class DesignHashSet
{
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        // Taking the input of the element to be added to the HashSet
        int key = sc.nextInt();
        
        // Creating an object of MyHashSet
        MyHashSet obj = new MyHashSet();

        // Adding the element
        obj.add(key);

        // Deleting the element 
        obj.remove(key);

        // Checking whether the element is present or not.
        System.out.println(obj.contains(key));
    }
}



