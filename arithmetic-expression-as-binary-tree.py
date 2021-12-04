class Node:
	def __init__(self, val = 0, right = None, left = None) -> None:
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self) -> str:
		return str(self.val)

def evaluate_expression(tree):
	def dfs(node):
		if type(node.val) == int: return node.val
		left_result = dfs(node.left)
		right_result = dfs(node.right)
		if node.val == '+': return left_result + right_result
		if node.val == '-': return left_result - right_result
		if node.val == '*': return left_result * right_result
		if node.val == '/': return left_result / right_result
	return dfs(tree)

tree = Node(
	'*',
	right=Node(
		'+',
		right=Node(5),
		left=Node(4),
	),
	left=Node(
		'+',
		right=Node(2),
		left=Node(3),
	)
)
output = 45
evaluate_expression(tree) == output
