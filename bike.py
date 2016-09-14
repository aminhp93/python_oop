class Bike(object):
	def __init__(self, price, max_speed, mile=0):
		self.price = price
		self.max_speed = max_speed
		self.mile = mile
	def displayInfo(self):
		# return [self.price, self.max_speed, self.mile]
		print 'Price is: $' + str(self.price)
		print 'Max speed: ' + str(self.max_speed) + 'mph'
		print 'Total miles: ' + str(self.mile) + 'miles'
	def ride(self):
		self.mile += 10
		print "Riding"
	def reverse(self):
		if self.mile >= 5:
			self.mile -= 5
		print "Reversing"

bike1 = Bike(100, 120)
bike2 = Bike(200, 140, 60)
bike3 = Bike(300, 160, 70)

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()


