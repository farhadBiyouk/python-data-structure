class Node:
	def __init__(self, data):
		self.right = None
		self.left = None
		self.data = data
	
	def get_left(self):
		return self.left
	
	def get_right(self):
		return self.right
	
	def get_data(self):
		return self.data

def search(root, data):
	if root is None or root.data == data:
		return root
	if data > root.data:
		return search(root.get_right(), data)
	return search(root.get_left(), data)

def insert(root, data):
	if root is None:
		return Node(data)
	if data < root.data:
		root.left = insert(root.left, data)
	else:
		root.right = insert(root.right, data)
	return

def min_value_node(root):
	temp = root
	while (temp.left is not None):
		temp = temp.left
	return temp

def max_value_node(root):
	temp = root
	
	while (temp.right is not None):
		temp = temp.right
	return temp

def in_order(root):
	if root is not None:
		in_order(root.left)
		print(root.data, end=' ')
		in_order(root.right)


root = None
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 6)
root = insert(root, 5)
root = insert(root, 7)
root = insert(root, 1)

print(in_order(root))
