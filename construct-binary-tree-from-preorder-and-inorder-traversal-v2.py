class Node:
	def __init__(self, val = 0, right = None, left = None) -> None:
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self) -> str:
		return str(self.val)

def reconstruct_binary_tree(pre_order, in_order):
	char_map = {character: i for i, character in enumerate(in_order)}
	def dfs(pre_order_index, in_order_start, in_order_end):
		if pre_order_index >= len(pre_order): return None
		index = char_map[pre_order[pre_order_index]]
		if not (in_order_start <= index <= in_order_end): return None
		node = Node(in_order[index])
		node.left = dfs(pre_order_index + 1, in_order_start, index - 1)
		left_size = index - in_order_start
		node.right = dfs(pre_order_index + left_size + 1, index + 1, in_order_end)
		return node
	return dfs(0, 0, len(in_order) - 1)

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
