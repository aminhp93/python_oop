# class Parent(object):
# 	def method_a(self):
# 		print "invoking Parent method_1"
# class Child(Parent):
# 	def method_a(self):
# 		print "invoking Child method_1"

# dad = Parent()
# son = Child()
# dad.method_a()
# son.method_a()

class Person(object):
	def pay_bill(self):
		raise NotImplementedError

class Millionaire(Person):
	def pay_bill(self):
		print "Here you go! Keep the change"

class GradStudent(Person):
	def pay_bill(self):
		print "Can I owe you ten buckes or do the dishes"

class Other(object):
	def override(self):
		print "Other overide()"
	def implicit(self):
		print "Other implicit()"
	def altered(self):
		print "Other altered()"

class Child(object):
	def __init__(self):
		self.other = Other()
	def implicit(self):
		self.other.implicit()
	def override(self):
		print "CHILD override()"
	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		self.other.altered()
		print "CHILD, AFTER OTHER altered()"

son = Child()
son.implicit()
son.override()
son.altered()

