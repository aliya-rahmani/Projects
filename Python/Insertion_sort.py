def insertionSort(array):
   for index in range(1,len(array)):

     currentvalue = array[index]
     position = index

     while position>0 and array[position-1]>currentvalue:
         array[position]=array[position-1]
         position = position-1

     array[position]=currentvalue
     return array
