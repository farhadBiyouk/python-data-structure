class Queue:
	"""front refer to first item on queue and rear refer to last item """
	
	def __init__(self, length):
		self.length = length
		self.queue = [None] * length
		self.front = -1
		self.rear = -1
	
	def enqueue(self, data):
		"""added new item to queue if queue not full"""
		if self.rear + 1 == self.length:
			print('queue is full')
		elif self.front == -1:
			self.front = 0
			self.rear = 0
			self.queue[self.rear] = data
		
		else:
			self.rear += 1
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
			self.front += 1
			return self.queue[self.front]
	
	def display(self):
		if self.front == -1:
			print('queue is empty')
		
		for i in range(self.front, self.rear + 1):
			print(self.queue[i], end=' ')


q1= Queue(3)
q1.enqueue(1)
q1.display()
