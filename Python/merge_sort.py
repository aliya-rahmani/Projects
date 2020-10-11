def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
		
	# Finding the middle point and partitioning the array into two halves
    middle = len(unsorted_list) // 2
    left = unsorted_list[:middle]
    right = unsorted_list[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

#Merging the sorted halves
def merge(left,right):

    res = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            res.append(left[0])
            left.remove(left[0])
        else:
            res.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        res = res + right
    else:
        res = res + left
    return res

input_list = list(map(int,input("Enter unsorted input list: ").split()))

print("Unsorted Input: ", input_list)
print("Sorted Output: ", merge_sort(input_list))