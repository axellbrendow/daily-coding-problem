class Node:
	def __init__(self, val = 0, right = None, left = None) -> None:
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self) -> str:
		return str(self.val)

def find_left_child(pre_order, pre_order_i, node_i, parents, in_order):
	child = in_order.index(pre_order[pre_order_i])
	for i in range(node_i - 1, -1, -1):
		if i in parents: return -1
		if i == child: return child
	return -1

def find_right_child(pre_order, pre_order_i, node_i, parents, in_order):
	child = in_order.index(pre_order[pre_order_i])
	for i in range(node_i + 1, len(in_order)):
		if i in parents: return -1
		if i == child: return child
	return -1

def reconstruct_binary_tree(pre_order, in_order):
	pre_order_i = 1
	root = Node(pre_order[0])
	parents = []
	def dfs(node, node_i, parent_i):
		nonlocal pre_order_i
		if not node: return
		if pre_order_i >= len(pre_order): return
		parents.append(parent_i)
		left = find_left_child(pre_order, pre_order_i, node_i, parents, in_order)
		if left != -1:
			node.left = Node(in_order[left])
			pre_order_i += 1
			dfs(node.left, left, node_i)
		if pre_order_i >= len(pre_order): return
		right = find_right_child(pre_order, pre_order_i, node_i, parents, in_order)
		if right != -1:
			node.right = Node(in_order[right])
			pre_order_i += 1
			dfs(node.right, right, node_i)
		parents.pop()
	dfs(root, in_order.index(pre_order[0]), -1)
	return root


pre_order = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
in_order = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
root = reconstruct_binary_tree(pre_order, in_order)
assert root.val == 'a'
assert root.left.val == 'b'
assert root.left.left.val == 'd'
assert root.left.right.val == 'e'
assert root.right.val == 'c'
assert root.right.left.val == 'f'
assert root.right.right.val == 'g'
