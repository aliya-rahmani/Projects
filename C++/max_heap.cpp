// using complete binary tree.
// A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible. 
// insert,removing - O(log(n)),get min/max - O(1)
// We can use a vector or an array for this.
// A[(2*i)+1] -> Left child 
// A[(2*i)+2] -> Right Child
// A[(i-1)/2] -> Parent node
// To check for valid max-heap 1)It should be a complete binary tree 2)The root value should be greater than child value

#include<bits/stdc++.h>
using namespace std;

void swap(int *x,int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

class MaxHeap {
    int *heap;
    int heap_size;
    int capacity;
    public:
    // constructor
    MaxHeap(int cap) {
        heap_size = 0;
        capacity = cap;
        heap = new int[cap];
    }
    // get parent index of a particular child
    int getParent(int i) {
        return (i-1)/2;
    }
    // get left child index of a particular parent
    int getLeftChild(int i) {
        return (2*i)+1;
    }
    // get right child index of a particular parent
    int getRightChild(int i) {
        return (2*i)+2;
    }
    // insert value in a heap
    void insertValue(int x) {
        if(heap_size == capacity) {
            cout<<"Maximum Size Reached "<<"\n";
            return;
        }
        // insert the value in heap
        heap_size++;
        int i = heap_size-1;
        heap[i] = x;
        // rearrage heap if condition violated
        while(i!=0 && heap[getParent(i)]<heap[i]) {
            swap(&heap[getParent(i)],&heap[i]);
            i = getParent(i);
        }
    }
    // get maximum value of the heap and pop
    int getMaxValue() {
        if(heap_size <= 0){
            return INT_MIN;
        }
        if(heap_size == 1){
            heap_size--;
            return heap[0];
        }
        int root = heap[0];
        heap[0] = heap[heap_size-1];
        // remove the min value 
        heap_size--;
        // max-heapify the tree taking the root element
        MaxHeapify(0);
        return root;
    }
    // a recurrsive function to max-heapify the tree
    void MaxHeapify(int i) {
        // get left child index
        int l = getLeftChild(i);
        // get right child index
        int r = getRightChild(i);
        // assuming greatest index is i and then balance if condition violated
        int greatest = i;
        if(l<heap_size && heap[l]>heap[i]){
            greatest = l;
        } 
        if(r<heap_size && heap[r]>heap[i]){
            greatest = r;
        }
        if(greatest != i) {
            swap(&heap[i],&heap[greatest]);
            MaxHeapify(greatest);
        }
    }
    // increase the value to a particular value
    void increaseValue(int i,int newValue) {
        heap[i] = newValue;
        while(i!=0 && heap[getParent(i)]<heap[i]) {
            swap(&heap[getParent(i)],&heap[i]);
            i = getParent(i);
        }
    }
    // delete a particular value in a heap
    // approach is to maximize the value of the element which is to be deleted and remove that
    void deleteValue(int i) {
        increaseValue(i,INT_MAX);
        getMaxValue();
    }
};


int main() {
    MaxHeap h(7);
    h.insertValue(5);
    h.insertValue(15);
    h.insertValue(10);
    h.insertValue(18);
    h.insertValue(16);
    cout<<"The maximum element of heap is : "<<h.getMaxValue()<<"\n";
    // cout<<"The maximum element of heap is : "<<h.getMaxValue()<<"\n";
    // cout<<"The maximum element of heap is : "<<h.getMaxValue()<<"\n";
    h.deleteValue(16);
    cout<<"Afeter deleting maximum element of heap is : "<<h.getMaxValue()<<"\n";
}