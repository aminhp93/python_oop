import random
class Human(object):
	def __init__(self, clan=None):
		print "New Humnan"
		self.health = 100
		self.clan = clan
		self.strength = 3
		self.intelligence = 3
		self.stealth = 3
	def taunt(self):
		print "Your want a piece of me"
	def attack(self):
		self.taunt()
		luck = round(random.random() * 100)
		if luck > 50:
			if luck * self.stealth > 150:
				print 'attacking'
				return True
			else:
				print 'attack failed'
				return False
		else: 
			self.health -= self.strength
			print 'acttacked failed'
			return False