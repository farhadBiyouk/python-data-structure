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


class BinaryTree:
	def __init__(self):
		self.in_order_list = []
		self.pre_order_list = []
		self.post_order_list = []
	
	def in_order(self, root):
		if root:
			self.in_order(root.left)
			self.in_order_list.append(root.data)
			self.in_order(root.right)
		return self.in_order_list
	
	def pre_order(self, root):
		if root:
			self.pre_order_list.append(root.data)
			self.pre_order(root.left)
			self.pre_order(root.right)
		return self.pre_order_list
	
	def post_order(self, root):
		if root:
			self.post_order(root.left)
			self.post_order(root.right)
			self.post_order_list.append(root.data)
		return self.post_order_list
	
	def count_nodes(self, root):
		left_node = 0
		right_node = 0
		
		if root.get_left():
			left_node = self.count_nodes(root.get_left())
		if root.get_right():
			right_node = self.count_nodes(root.get_right())
		
		return left_node + right_node + 1

	def count_leaf(self, root):
		if root is None:
			return 0
		if root.get_left() is None and root.get_right() is None:
			return 1
		return self.count_leaf(root.get_left()) + self.count_leaf(root.get_right())
		
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

bt = BinaryTree()
print(bt.post_order(root))
print(bt.count_nodes(root))
print(bt.count_leaf(root))