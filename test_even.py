# import unittest

# def isEven(n):
# 	return n % 2 == 0

# class IsEvenTests(unittest.TestCase):
# 	def testTwo(self):
# 		self.failUnless(isEven(2))
# 	def testThree(self):
# 		self.failIf(isEven(3))

# if __name__ == '__main__':
# 	unittest.main()

import unittest

class TruthTest(unittest.TestCase):
	def test_assert_true(self):
		my_value = True
		self.assertTrue(my_value)
	def test_assert_false(self):
		my_value = False
		self.assertFalse(my_value)

if __name__ == "__main__":
	unittest.main()