import unittest
from bulb_classes import LightBulb, LightBulbFactory

class LightBulbTest(unittest.TestCase):
	# using setUp method to create an inital instance of the bulb_factory and a new light bulb
	def setUp(self):
		self.bulb_factory = LightBulbFactory()
		self.bulb = self.bulb_factory.create_bulb("GE")

	# testing if the created bulb is indded an instance of LightBulb
	def testNewBulbIsLightBulb(self):
		return self.assertIsInstance(self.bulb, LightBulb)

	# test the created bulb to make sure it has a brand on creation
	def testBulbHasBrand(self):
		return self.assertEqual('GE', self.bulb.brand)

	# testing the created bulb to make sure it is off by default
	def testBulbDefaultOff(self):
		return self.assertEqual(False, self.bulb.on_or_off())

	# testing to see if can switch the bulb on from the off status
	def testTurnOnBulb(self):
		self.bulb.switch_on()
		return self.assertEqual(True, self.bulb.on_or_off())

if __name__ == '__main__':
	unittest.main()