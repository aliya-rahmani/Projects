# Python code that implements the bogosort sorting algorithm which has a worst-case complexity of O((n+1)!)
# Author: @incarnadined

import random

def check_sorted(data):
    for i in data:
        if i<data[data.index(i)-1] and data.index(i) != 0:
            return False
    return True

def bogosort(data):
    random.shuffle(data)
    while not check_sorted(data):
        random.shuffle(data)
    return data

data = bogosort(random.sample(range(300), 10))
print(f"Sorted data is: {data}")
