
ODD = 0xAAAAAAAAAAAA
EVEN = 0x55555555555  

def pairwise_swap(n):
	return (((n & ODD)>>1) | (n & EVEN)<<1)


import unittest
class Test(unittest.TestCase):
	def test_pairwise_swap(self):
		self.assertEqual(pairwise_swap(15),15)
		self.assertEqual(pairwise_swap(9),6)


if __name__ == '__main__':
	unittest.main()