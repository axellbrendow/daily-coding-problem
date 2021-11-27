class MaxStack:
	def __init__(self):
		self._stack = []

	def empty(self):
		return len(self._stack) == 0

	def push(self, val):
		new_max = val if self.empty() else max(val, self._stack[-1][1])
		self._stack.append((val, new_max))

	def pop(self):
		if self.empty(): return None
		return self._stack.pop()[0]

	def max(self):
		if self.empty(): return None
		return self._stack[-1][1]

stack = MaxStack()
assert stack.max() == None
assert stack.pop() == None

stack.push(1)
assert stack.max() == 1

stack.push(2)
assert stack.max() == 2

stack.push(0)
assert stack.max() == 2

stack.pop()
stack.pop()
assert stack.max() == 1
