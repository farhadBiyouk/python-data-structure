class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.previous = None


class DoubleLinkedList:
	def __init__(self):
		self.head = None
	
	def in_start(self, data):
		new = Node(1)
		new.next = self.head
		if self.head is not None:
			self.head.previous = new
		self.head = new
	
	def in_end(self, data):
		new = Node(data)
		temp = self.head
		
		if temp is None:
			self.head = new
			return
		while (temp.next):
			temp = temp.next
		
		temp.next = new
		new.previous = temp
	
	def in_after(self, pos, data):
		new = Node(data)
		new.next = pos.next
		new.previous = pos
		pos.next = new
		if new.next is not None:
			new.next.previous = new
	
	def remove_node(self, data):
		temp = self.head
		if temp.next is not None:
			if temp.data == data:
				temp.next.previous = None
				self.head = temp.next
				temp.next = None
				return
			else:
				while temp.next is not None:
					if temp.data == data:
						break
					temp = temp.next
				if temp.next:
					temp.previous.next = temp.next
					temp.next.previous = temp.previous
					temp.next = None
					temp.previous = None
				else:
					temp.previous.next = None
					temp.previous = None
				return
		
		if temp is None:
			return
	
	def display(self, num):
		while (num is not None):
			print(num.data, end=' <-> ')
			num = num.next
		print('Null')



dl = DoubleLinkedList()
dl.in_start(1)
dl.in_end(2)
dl.in_end(3)
dl.in_end(4)
dl.display(dl.head)