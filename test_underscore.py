import unittest
from underscore_tdd2 import Underscore

class UnderscoreTest(unittest.TestCase):
	def setUp(self):
		#create an instance of the Underscore mdule we created
		self._ = Underscore()
		# initialize a list to run our test on 
		self.test_list = [1,2,3,4,5]
		self.testmap = [1,4,9,16,25]

	def plus(self, memo, list):
		for i in list:
			memo += i
		return memo

	def testMap(self):
		return self.assertEqual(self.testmap, self._.map(self.test_list, lambda x: x**2))

	def testReduce(self):
		return self.assertEqual(20, self._.reduce(self.test_list, lambda y, x: x + y, 5))

	def testFind(self):
		return self.assertEqual(3, self._.find(self.test_list, lambda x: x > 2))

	def testFilter(self):
		return self.assertEqual([3,4,5], self._.filter(self.test_list, lambda x: x > 2) )

	def testReject(self):
		return self.assertEqual([1,2], self._.reject(self.test_list, lambda x: x > 2))

if __name__ == "__main__":
	unittest.main()