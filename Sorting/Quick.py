def partition_func(lst, first, last):
	position = lst[first]
	left = first + 1
	right = last
	done = False
	while not done:
		while left <= right and lst[left] <= position:
			left = left + 1
		
		while lst[right] >= position and right >= left:
			right = right - 1
		
		if right < left:
			done = True
		else:
			temp = lst[left]
			lst[left] = lst[right]
			lst[right] = temp
	
	temp = lst[first]
	lst[first] = lst[right]
	lst[right] = temp
	return right


def quick_sort(lst, first, last):
	if first < last:
		partition = partition_func(lst, first, last)
		quick_sort(lst, first, partition - 1)
		quick_sort(lst, partition + 1, last)


numbers = [3, 5, 1, 2, 4, 6, 7]
quick_sort(numbers, 0, len(numbers) - 1)
print(numbers)