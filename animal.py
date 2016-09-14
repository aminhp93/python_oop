class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print "Name: " + str(self.name)
		print "Health: " + str(self.health)

animal = Animal('Patria')
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150
		self.name = name

	def pet(self):
		self.health += 5
		return self

dog = Dog('Reck')
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon,self).__init__(name)
		self.health = 170
		self.name = name

	def fly(self):
		self.health -= 10
		return self

	def displayHealth(self):
		super(Dragon, self).displayHealth()
		print "This is a dragon"
		print "Name: " + str(self.name)
		print "Health: " + str(self.health) 

dragon = Dragon('Kevin')
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
