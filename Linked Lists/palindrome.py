class Node:
	def __init__(self,data,next):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def palindromeStack(self,head):
		slow = head
		fast = head	
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next	
		stack = []
		while slow:
			stack.append(slow.data)
			slow = slow.next
		while stack :
			if head.data!=stack.pop():
				return False
			head = head.next
		return True

	def palindromeInPlace(self,head):
		slow  = head
		fast = head
		rev = None
		while fast and fast.next:
			slow = slow.next
			rev = slow
			rev.next = rev

			fast = fast.next.next
		if fast:
			slow = slow.next

		while rev and rev.data == slow.data:
			rev = rev.next 
			slow = slow.next

		return True			

import unittest
class Test(unittest.TestCase):
	def test_palindromeStack(self):
		head = Node(1,Node(2,Node(3,Node(2,Node(1,None)))))
		obj = LinkedList()
		self.assertTrue(obj.palindromeStack(head))
		self.assertTrue(obj.palindromeStack(Node(1,Node(2,Node(2,Node(2,Node(1,None)))))))
		self.assertFalse(obj.palindromeStack(Node(1,Node(5,Node(3,Node(2,Node(1,None)))))))

	def test_palindromeInPlace(self):
		head = Node(1,Node(2,Node(3,Node(2,Node(1,None)))))
		obj = LinkedList()
		self.assertTrue(obj.palindromeStack(head))
		self.assertTrue(obj.palindromeStack(Node(1,Node(2,Node(2,Node(2,Node(1,None)))))))
		self.assertFalse(obj.palindromeStack(Node(1,Node(5,Node(3,Node(2,Node(1,None)))))))



if __name__ == '__main__':
	unittest.main()
	