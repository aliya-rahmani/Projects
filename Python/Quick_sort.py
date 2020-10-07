def QuickSort(array):

    elements = len(array)
    
    
    if elements < 2:
        return array
    
    current_position = 0 

    for i in range(1, elements): 
         if array[i] <= array[0]:
              current_position += 1
              temp = array[i]
              array[i] = array[current_position]
              array[current_position] = temp

    temp = array[0]
    array[0] = array[current_position] 
    array[current_position] = temp 
    
    left = QuickSort(array[0:current_position]) 
    right = QuickSort(array[current_position+1:elements]) 

    array = left + [array[current_position]] + right
    
    return array