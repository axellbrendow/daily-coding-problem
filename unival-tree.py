class Node:
	def __init__(self, val = 0, right = None, left = None) -> None:
		self.val = val
		self.left = left
		self.right = right

def is_unival(root):
	def is_unival_rec(node):
		if not node: return True, 0
		unival_left, count_left = is_unival_rec(node.left)
		unival_right, count_right = is_unival_rec(node.right)
		count = count_left + count_right
		if (
			unival_left and unival_right and
			(not node.left or node.left.val == node.val) and
			(not node.right or node.right.val == node.val)
		):
			return True, count + 1
		else:
			return False, count

	return is_unival_rec(root)[1]

assert is_unival(None) == 0

assert is_unival(
	Node(0)
) == 1

assert is_unival(
	Node(
		0,
		Node(0),
	)
) == 2

assert is_unival(
	Node(
		0,
		Node(0),
		Node(0),
	)
) == 3

assert is_unival(
	Node(
		0,
		Node(
            0,
            Node(0),
            Node(1),
        ),
		Node(
            1,
            Node(1),
            Node(1),
        ),
	)
) == 5
