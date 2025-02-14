def binary_search(lst, target, first, last):
	if first> last:
		return False
	else:
		mid = (first + last) // 2
		if target == lst[mid]:
			return True
		elif target < lst[mid]:
			return  binary_search(lst, target, first, mid-1)
		else:
			return binary_search(lst, target, mid+1, last)
		
numbers = [1,4,8,12,16,18,20,24,29,30,34,36,37,42,46]
print(binary_search(numbers, 24, 0, len(numbers)))
