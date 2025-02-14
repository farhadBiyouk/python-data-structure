def insertion_sort(lst):
	for i in range(1, len(lst)):
		current_value = lst[i]
		position = i
		
		while position > 0 and lst[position - 1] > current_value:
			lst[position] = lst[position - 1]
			position = position - 1
		
		lst[position] = current_value


numbers = [3, 5, 1, 8, 2, 4, 6, 7]
insertion_sort(numbers)
print(numbers)
