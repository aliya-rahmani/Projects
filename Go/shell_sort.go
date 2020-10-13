package main

func shellSort(items []int) []int {
	for d := int(len(items) / 2); d > 0; d /= 2 {
		for i := d; i < len(items); i++ {
			for j := i; j >= d && items[j-d] > items[j]; j -= d {
				items[j], items[j-d] = items[j-d], items[j]
			}
		}
	}
	return items
}
