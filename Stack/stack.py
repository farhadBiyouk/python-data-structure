class Stack:
	def __init__(self):
		self.stack = []
		self.limit = 10
	
	def push(self, data):
		if len(self.stack) >= self.limit:
			return -1
		else:
			self.stack.append(data)
	
	def pop(self):
		if len(self.stack) <= 0:
			return -2
		else:
			return self.stack.pop()
	
	def peek(self):
		if len(self.stack) <= 0:
			return -2
		else:
			return self.stack[len(self.stack) - 1]


# Example 1
# converto decimal to binary

def decimal_to_binary(num):
	s = Stack()
	while num > 0:
		s.push(num % 2)
		num = num // 2
	
	msg = ''
	while not len(s.stack) <= 0:
		print(s.pop())
	return msg


# Example 2
# reverse list item

def reverse_item(lst):
	s = Stack()
	for i in lst:
		s.push(i)
	
	for j in range(len(lst)):
		lst[j] = s.pop()
