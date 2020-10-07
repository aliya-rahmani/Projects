# Initialize method to perform binary search
def binary_search(list, n):
    lower_index = 0
    upper_index = len(list)-1

    while lower_index <= upper_index:
        mid_index = (lower_index + upper_index) // 2 # Double divide sign(//) gives integer value as output

        if list[mid_index] == n:
            globals()['position'] = mid_index
            return True
        
        else:
            if list[mid_index] < n:
                lower_index = mid_index + 1
            
            else:
                upper_index = mid_index - 1
    return False            

list = [2,4,6,18,25,50] # List can have any number of elements but should be sorted
n = 6

if binary_search(list, n):
    print(f"{n} is found at {position+1} position of your list" )
else:
    print(f"{n} is not found")

# Algorithm found in https://www.youtube.com/watch?v=DE-ye0t0oxE