# Python program for implementation of QuickSort with imporoved partition3 algorithm
def partition3(A,l,r):
    pivot = A[l] # Taking leftmost element as pivot element
    m1 = l
    m2 = r
    i = l
    while i<=m2:
        if A[i]==pivot:
            i+=1
        elif A[i]<pivot:
            A[i],A[m1] = A[m1],A[i]
            m1+=1
        elif A[i]>pivot:
            A[i],A[m2] = A[m2],A[i]
            m2-=1
    return m1,m2 # m1,m2 are the start and end position of the pivot element in array
    
    
def quickSort(A,l,r):
    if l>=r:
        return
    m1,m2 = partition3(A,l,r) 
    quickSort(A,l,m1-1) # sort left part of the pivot
    quickSort(A,m2+1,r) # sort right part of the pivot


# driver code to test the above code 
if __name__ == '__main__': 
    n = int(input())
    A = [int(j) for j in input().split()]
    quickSort(A,0,n-1)
    print(*A)
