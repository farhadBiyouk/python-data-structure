def hanoi_rec(n, source, assistant, destination):
	if n == 1:
		print('Move', n, 'from', source, 'to', destination)
		return
	hanoi_rec(n-1, source, destination, assistant)
	print('Move', n, 'from', source, 'to', destination)
	hanoi_rec(n-1, assistant, source, destination)


hanoi_rec(3, 'A', 'B', 'C')