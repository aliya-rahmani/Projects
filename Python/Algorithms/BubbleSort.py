# Python program for implementation of Bubble Sort 
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

# Driver code to test above 
alist = [64, 34, 25, 12, 22, 11, 90] 

bubbleSort(alist) 

print ("Sorted array is:") 
for i in range(len(alist)): 
	print ("%d" %alist[i]), 
