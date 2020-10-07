#binary search (Recursive program)
#This algorithm uses recursion to find the given element in an array via binary search method

def binary_search(lst, e, start, end):
    #Assuming the list lst is sorted in ascending order

    if start > end:
        return False        

    mid = (start + end) // 2 # mid point of range to search
    
    if lst[mid] == e:
        return True
    
    if lst[mid] > e: # is element in the first half ?
        return binary_search(lst, e, start, mid-1)
    
    else: # element in the second half
        return binary_search(lst, e, mid+1, end)
    
m = int(input('Enter the number of elements in the array: '))
mylist = []

for i in range(0,m):
    num = int(input('Enter element: '))
    mylist.append(num)
    
x = int(input('Enter the element that you wish to find: '))

binary_search(mylist,x,0,m)
