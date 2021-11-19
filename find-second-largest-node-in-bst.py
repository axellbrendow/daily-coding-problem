class Node:
	def __init__(self, val = 0, right = None, left = None):
		self.val = val
		self.right = right
		self.left = left

def find_greatest_node(node):
	parent = None
	while node.right:
		parent = node
		node = node.right
	return parent, node

def find_second_largest_node_in_bst(root):  # This code assumes the tree has at least 2 nodes
	parent, greatest_node = find_greatest_node(root)
	if not greatest_node.left: return parent.val
	parent, greatest_node = find_greatest_node(greatest_node.left)
	return greatest_node.val

tree = Node(
	11,
	None,
	Node(5)
)
assert find_second_largest_node_in_bst(tree) == 5

tree = Node(
	11,
	Node(25),
	Node(5)
)
assert find_second_largest_node_in_bst(tree) == 11

tree = Node(
	11,
	Node(15)
)
assert find_second_largest_node_in_bst(tree) == 11

tree = Node(
	11,
	Node(
		15,
		Node(22)
	)
)
assert find_second_largest_node_in_bst(tree) == 15

tree = Node(
	11,
	Node(
		25,
		None,
		Node(22)
	),
	Node(5)
)
assert find_second_largest_node_in_bst(tree) == 22

tree = Node(
	11,
	Node(
		25,
		None,
		Node(
			22,
			Node(24)
		)
	),
	Node(5)
)
assert find_second_largest_node_in_bst(tree) == 24
