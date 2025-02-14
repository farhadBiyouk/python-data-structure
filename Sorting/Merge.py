def merging(left, right):
	i = 0
	j = 0
	lst = []
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			lst.append(left[i])
			i += 1
		
		else:
			lst.append(right[j])
			j += 1
	
	lst += left[i:]
	lst += right[j:]
	return lst


def merge_sort(lst):
	if len(lst) <= 1:
		return lst
	mid = len(lst) // 2
	left = merge_sort(lst[:mid])
	right = merge_sort(lst[mid:])
	return merging(left, right)


numbers = [3, 5, 1, 2, 4, 6, 7]
print(merge_sort(numbers))
