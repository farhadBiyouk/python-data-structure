class Stack:
	def __init__(self):
		self.stack = []
		self.limit = 10
	
	def is_empty(self):
		return len(self.stack) <= 0
	
	def is_full(self):
		return len(self.stack) >= self.limit
	
	def push(self, data):
		if self.is_full():
			return -1
		else:
			self.stack.append(data)
	
	def pop(self):
		if self.is_empty():
			return -2
		else:
			return self.stack.pop()
	
	def peek(self):
		if self.is_empty():
			return -2
		else:
			return self.stack[len(self.stack) - 1]



