class QueueRotating:
	def __init__(self, length):
		self.length = length
		self.queue = [None] * length
		self.front = -1
		self.rear = -1
	
	def enqueue(self, data):
		if (self.rear + 1) % self.length == self.front:
			print('queue is full')
		elif self.front == -1:
			self.front = 0
			self.rear = 0
			self.queue[self.rear] = data
		
		else:
			self.rear = (self.rear + 1) % self.length
			self.queue[self.rear] = data
	
	def dequeue(self):
		"""delete item from queue if not empty"""
		if self.front == -1:
			print('queue is empty')
		
		elif self.front == self.rear:
			self.front = -1
			self.rear = -1
			return self.queue[self.front]
		else:
			self.front = (self.front + 1) % self.length
			return self.queue[self.front]
	
	def display(self):
		if self.front == -1:
			print('queue is empty')
		elif self.front <= self.rear:
			for i in range(self.front, self.rear + 1):
				print(self.queue[i], end=' ')
			print()
		
		else:
			for i in range(self.front, self.length):
				print(self.queue[i], end=' ')
			for i in range(0, self.rear + 1):
				print(self.queue[i], end=' ')
			print()



q1 = QueueRotating(5)
q1.enqueue(1)
q1.enqueue(12)
q1.enqueue(13)
q1.enqueue(14)
q1.enqueue(15)
q1.dequeue()
q1.enqueue(20)
q1.dequeue()
q1.enqueue(21)
q1.display()
