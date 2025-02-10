class Node:
	def __init__(self, data):
		self.data = data
		self.next = self


class RotatingLinkedList:
	def __init__(self):
		self.head = None
		self.count = 0
	
	def display(self):
		temp = self.head
		if temp is None:
			print('Empty')
			return
		while (True):
			print(temp.data, end='->')
			temp = temp.next
			if temp == self.head:
				break
	
	def insert(self, d, i):
		
		if (i > self.count) | (i < 0):
			print('Index out of range')
		if self.head == None:
			self.head = Node(d)
			self.count += 1
			return
		t = self.head
		for _ in range(self.count - 1 if i - 1 == -1 else i - 1):
			t = t.next
		a = t.next
		t.next = Node(d)
		t.next.next = a
		if (i == 0):
			self.head = t.next
		self.count += 1
		return
	
	def remove(self, i):
		if (i >= self.count) | (i < 0):
			print('Index out of range')
		if self.count == 1:
			self.head = None
			self.count = 0
			return
		t = self.head
		for _ in range(self.count - 1 if i - 1 == -1 else i - 1):
			t = t.next
		a = t.next.next
		t.next = a
		if (i == 0):
			self.head = a
		self.count -= 1
		return
	
	def size(self):
		return self.count
	
	def index(self, d):
		t = self.head
		for i in range(self.count):
			if (t.data == d):
				return i
			t = t.next
		return None
