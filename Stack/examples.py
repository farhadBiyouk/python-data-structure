from stack import Stack


# Example 1
# converto decimal to binary

def decimal_to_binary(num):
	s = Stack()
	while num > 0:
		s.push(num % 2)
		num = num // 2
	
	msg = ''
	while not len(s.stack) <= 0:
		msg += str(s.pop())
	return msg


# Example 2
# reverse list item

def reverse_item(lst):
	s = Stack()
	for i in lst:
		s.push(i)
	
	for j in range(len(lst)):
		lst[j] = s.pop()
