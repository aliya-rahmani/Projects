def partition(array, low, high):
    i = (low - 1)
    pivot = array[high]
 
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
 
    array[i+1], array[high] = array[high], array[i+1]
    return (i + 1)
 
def quickSort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        part = partition(array, low, high)
        quickSort(array, low, part - 1)
        quickSort(array, part + 1, high)

array = []
while 1:
    try:
        x = input("Enter a number (To exit write something tha is not a number): ")
    except:
        break
    array.append(x)

quickSort(array, 0, len(array) - 1)
print("Sorted array using Quicksort:")
for i in range(len(array)):
    print("%d" % array[i]),