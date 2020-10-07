def countingSort(array):
    n = len(array)
    count = [0] * (max(array) + 1)
    answer = [0] * n
    for i in range(n):
        count[array[i]] += 1
    for i in range(1, len(count)):
        count[i] += count[i-1]
    for i in range(n-1, -1, -1):
        count[array[i]] -= 1
        answer[count[array[i]]] = array[i]
    return answer


arr = [5, 8, 9, 2, 1, 2, 2, 3, 4, 5, 6, 7, 9, 10, 0, 0]
print(countingSort(arr))
