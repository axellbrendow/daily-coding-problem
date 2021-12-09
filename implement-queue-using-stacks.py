class MyQueue:
	def __init__(self):
		self._insertion_stack = []
		self._deletion_stack = []

	def push(self, val):
		while len(self._deletion_stack) > 0:
			self._insertion_stack.append(self._deletion_stack.pop())
		self._insertion_stack.append(val)

	def pop(self):
		if self.empty(): raise Exception('Queue is empty!')
		while len(self._insertion_stack) > 0:
			self._deletion_stack.append(self._insertion_stack.pop())
		return self._deletion_stack.pop()

	def peek(self):
		if self.empty(): raise Exception('Queue is empty!')
		while len(self._insertion_stack) > 0:
			self._deletion_stack.append(self._insertion_stack.pop())
		return self._deletion_stack[-1]

	def empty(self):
		return len(self._insertion_stack) == 0 and len(self._deletion_stack) == 0

queue = MyQueue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
assert queue.pop() == 1
queue.push(5)
assert queue.pop() == 2
assert queue.pop() == 3
assert queue.pop() == 4
assert queue.pop() == 5
