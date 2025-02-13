class Node:
	def __init__(self, data):
		self.vertex = data
		self.next = None


class Graph:
	def __init__(self, n):
		self.V = n
		self.graph = [None] * self.V
	
	def add_edge(self, s, d):
		n = Node(d)
		n.next = self.graph[s]
		self.graph[s] = n
		m = Node(s)
		m.next = self.graph[d]
		self.graph[d] = m
	
	def show(self):
		for i in range(self.V):
			print(i, ": head", end=' ')
		t = self.graph[i]
		while t:
			print("-> {}".format(t.vertex), end=' ')
			t = t.next
		print("\n")


g = Graph(5)

g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.show()
