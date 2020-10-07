def countingSort(array, div):
    count = [0] * 10
    answer = array[:]
    for i in range(len(array)):
        count[(array[i] // div) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    for i in range(len(array)-1, -1, -1):
        count[(array[i] // div) % 10] -= 1
        answer[count[(array[i]//div) % 10]] = array[i]
    return answer


def radixSort(array):
    max_element = max(array)
    i = 1
    while max_element//i:
        array = countingSort(array, i)
        i *= 10
    return array


arr = [5, 8, 9, 2, 1, 2, 2, 3, 4, 5, 6, 7, 9, 10, 0, 0]
print(radixSort(arr))
print(arr)
arr.sort()
print(arr)
