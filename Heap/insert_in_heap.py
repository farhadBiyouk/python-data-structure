def insert_node(lst: list, new_data: int):
	global len_lst
	len_lst += 1
	lst.append(new_data)
	heapify(lst,len_lst -1)


def heapify(lst, item):
	r = int(((item -1 )/2))
	if lst[r] > 0:
		if lst[item] > lst[r]:
			lst[item], lst[r] = lst[r], lst[item]
			heapify(lst, r)


numbers = [45,35,23,27,21,22,4,19]
len_lst = len(numbers)

insert_node(numbers, 42)
for item in range(len_lst):
	print(numbers[item], end=' ')