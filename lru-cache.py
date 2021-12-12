class Node:
	def __init__(self, key = None, val = None, left = None, right = None):
		self.key = key
		self.val = val
		self.left = left
		self.right = right

class LRUCache:
	def __init__(self, max_size):
		self._size, self._max_size = 0, max_size
		self._node_map = {}
		self._head = Node()
		self._tail = Node(None, None, self._head)
		self._head.right = self._tail

	def _remove_node(self, node: Node):
		left = node.left
		right = node.right
		left.right = right
		right.left = left
		del self._node_map[node.key]
		self._size -= 1

	def _remove_LRU(self):
		if self._size == 0: return
		self._remove_node(self._tail.left)

	def _add_in_the_front(self, key, val):
		left = self._head
		right = self._head.right
		node = Node(key, val, left, right)
		self._node_map[key] = node
		left.right = node
		right.left = node
		self._size += 1

	def put(self, key, value):
		if key in self._node_map:
			self._remove_node(self._node_map[key])
		else:
			if self._size == self._max_size: self._remove_LRU()
		self._add_in_the_front(key, value)

	def get(self, key):
		if not key in self._node_map: return -1
		node = self._node_map[key]
		self._remove_node(node)
		self._add_in_the_front(key, node.val)
		return node.val

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
assert cache.get(2) == -1
cache.put(4, 4)
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4

cache = LRUCache(2)
cache.put(2, 1)
cache.put(1, 1)
cache.put(2, 3)
cache.put(4, 1)
assert cache.get(1) == -1
assert cache.get(2) == 3
