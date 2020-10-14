package main

func selectionSort(items []int) []int {

	for i := 0; i < len(items); i++ {
		min := i
		for j := i + 1; j < len(items); j++ {
			if items[j] < items[min] {
				min = j
			}
		}

		tmp := items[i]
		items[i] = items[min]
		items[min] = tmp
	}
	return items
}
