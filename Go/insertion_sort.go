package main

func insertionSort(items []int) []int {
	for currentIndex := 1; currentIndex < len(items); currentIndex++ {
		temporary := items[currentIndex]
		iterator := currentIndex
		for ; iterator > 0 && items[iterator-1] >= temporary; iterator-- {
			items[iterator] = items[iterator-1]
		}
		items[iterator] = temporary
	}
	return items
}