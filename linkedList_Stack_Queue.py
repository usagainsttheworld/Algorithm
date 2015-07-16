class Node:
	def __init__(self):
		self.value = None
		self.next = None

class Stack:
	def __init__(self):
		self.head = Node()

	def push(self, node):
		"""
		function takes a node and add it to a stack
		"""
		if self.head == None:
			self.head = node
		else:
			node.next = self.head
			self.head = node
	
	def pop(self):
		"""
		function remove the LAST added node from a stack
		"""
		if self.head == None:
			return None
		elif self.head.next == None:
			pop_node = self.head
			self.head = None
		else:
			pop_node = self.head
			self.head = self.head.next
		return pop_node

class Queue:
	def __init__(self):
		self.head = Node()
		self.tail = Node()
	def push (self, node):
		"""
		function takes a node and add to a queue
		"""
		if self.head.value == None and self.tail.value == None:
			self.head = node
			self.tail = node
		else:
			self.tail = node
			self.next = node
	def pop(self):
		"""
		function that removes the FIRST added node from a queue
		"""
		pop_node = self.head
		self.head = self.head.next
		return pop_node

#Tests
n1 = Node()
n1.value = 1
n2 = Node()
n2.value = 2
n1.next = n2
n3 = Node()
n3.value = 3
n4 = Node()
n4.value = 4
#test = Stack()
test = Queue()
test.push(n1)
test.push(n2)
test.pop()
test.pop()
test.pop()
print test.head






		



