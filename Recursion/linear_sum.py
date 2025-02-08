def linear_sum_of_list(lst, n):
	if n == 0:
		return 0
	return linear_sum_of_list(lst, n - 1) + lst[n - 1]


