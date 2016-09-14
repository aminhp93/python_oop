class Bike(object):
	def __init__(self, price, max_speed, mile=0):
		self.price = price
		self.max_speed = max_speed
		self.mile = mile
	def displayInfo(self):
		print 'Price is: $' + str(self.price)
		print 'Max speed: ' + str(self.max_speed) + 'mph'
		print 'Total mile: ' + str(self.mile) + 'miles'
	def ride(self):
		self.mile += 10
		print str(self.mile)
		print "Riding"
		return self
	def reverse(self):
		if self.mile >= 5:
			self.mile -= 5
		print "Revesring"
		return self

bike1 = Bike(100, 120)
bike2 = Bike(200, 140, 60)
bike3 = Bike(300, 160, 70)

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()