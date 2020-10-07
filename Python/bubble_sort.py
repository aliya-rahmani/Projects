'''
bubble sort
Comparison sort
complexity:  О(n2)
'''
def bubble_sort(number_list):
    value_exchange =0
    for index,value in enumerate(number_list):
        if index != len(number_list)-1 and value > number_list[index+1] :
            number_list[index]=number_list[index+1]
            number_list[index+1]=value
            value_exchange=1

    if not value_exchange:
         print(number_list)
         return

    bubble_sort(number_list)  



number_list = [23,45,231,767,8,342,24,67,232,5,67,2]    

bubble_sort(number_list) 