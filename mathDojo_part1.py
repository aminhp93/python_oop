class MathDojo(object):
	def __init__(self):
		self.value = 0

	def add(self, x=0, y=0):
		self.value += x + y
		return self

	def subtract(self, x=0, y=0):
		self.value = self.value - x - y 
		return self

	def result(self):
		print "Result: " + str(self.value)

md = MathDojo().add(2,5).subtract(4,2).result()
print md

