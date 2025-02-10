class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None
	
	def display(self):
		temp = self.head
		while temp is not None:
			print(temp.data, end='-> ')
			temp = temp.next
		print('Null')
	
	def in_start(self, data):
		new = Node(data)
		new.next = self.head
		self.head = new
	
	def in_end(self, data):
		temp = self.head
		new = Node(data)
		if temp is None:
			self.head = new
			return
		while (temp.next):
			temp = temp.next
		
		temp.next = new
	
	def in_after(self, pos, data):
		new = Node(data)
		new.next = pos.next
		pos.next = new
	
	def remove_node(self, data):
		temp = self.head
		if temp is not None:
			if temp.data == data:
				self.head = temp.next
				return
		
		while (temp is not None):
			if temp.data == data:
				break
			
			pointer = temp
			temp = temp.next
		if temp is None:
			return
		pointer.next = temp.next
		temp = None


