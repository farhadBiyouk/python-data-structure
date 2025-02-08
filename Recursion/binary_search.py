def bin_search(lst, target, low, high):
	if low > high:
		return False
	else:
		mid = (low + high) // 2
		if target == lst[mid]:
			return lst.index(target)
		elif target < lst[mid]:
			return bin_search(lst, target, low, mid -1)
		else:
			return bin_search(lst , target, mid + 1, high)

numbers = [1,4,8,12,16,18,20,24,29,30,34,36,37,42,46]
print(bin_search(numbers, 39, 0, len(numbers)))