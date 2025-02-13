class Graph:
	def __init__(self, size):
		self.size = size
		self.matrix = []
		
		self.matrix = [[0] * size for __ in range(size)]
	
	def add_edge(self, v1, v2):
		self.matrix[v1][v2] = 1
		self.matrix[v2][v1] = 1
	
	def remove_edge(self, v1, v2):
		self.matrix[v1][v2] = 0
		self.matrix[v2][v1] = 0
	
	def print_matrix(self):
		for row in self.matrix:
			for j in row:
				print(j, end='  '),
			print()


g = Graph(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,3)
g.print_matrix()