def bubble_sort(lst):
	for i in range(len(lst) - 1, 0, -1):
		for j in range(i):
			if lst[j] > lst[j + 1]:
				temp = lst[j]
				lst[j] = lst[j + 1]
				lst[j + 1] = temp


numbers = [3, 5, 1, 2, 4, 6, 7]
bubble_sort(numbers)
print(numbers)