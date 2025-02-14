def selection_sort(lst):
	for i in range(len(lst) - 1, 0, -1):
		position = 0
		for j in range(1, i + 1):
			if lst[j] > lst[position]:
				position = j
		
		temp = lst[i]
		lst[i] = lst[position]
		lst[position] = temp


numbers = [3, 5, 1, 2, 9, 4, 6, 7, 8]
selection_sort(numbers)
print(numbers)
