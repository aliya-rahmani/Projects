# Python code for Selection Sort
def selection_sort(L):
    for i in range(len(L)-1):
        min_index = i
        for j in range(i+1, len(L)-1):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
        
# Running a test case
L = [3, 1, 41, 59, 26, 53, 59]
print(L)
selection_sort(L)
print(L)        
