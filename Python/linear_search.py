#linear search program
#returns the index number of the element you wish to find in an array

def linear_search(array, element): 
    
    #traverse through the array
    for i in range(len(array)): 
        
        #checks if the element is at the ith position in the array
        #if true, then returns the position
        if array[i] == element: 
            return i 
        
    #returns -1 if the element is not in the array
    return -1


m = int(input('Enter the number of elements in the array: '))
mylist = []

for i in range(0,m):
    num = int(input('Enter element: '))
    mylist.append(num)
    
x = int(input('Enter the element whose position you want to find: '))

linear_search(mylist,x)
