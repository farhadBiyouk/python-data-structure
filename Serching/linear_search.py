def linear_search(lst, target):
	for i in range(len(lst)):
		if lst[i] == target:
			return f'{target} in index {i}'
	
	return -1


numbers = [1,57,8,91,3,66,44,55,11,2,5,789,4]
print(linear_search(numbers, 5))