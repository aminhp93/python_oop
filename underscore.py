class Underscore(object):
	def map(self, list, callback):
		result = []
		for i in list:
			result.append(callback(i))
		return result

	def reduce(self, list, callback):
		result = 0
		new_list = []
		for i in list:
			new_list.append(callback(i))
		for j in new_list:
			result += j
		return result

	def find(self, list, callback):
		for i in list:
			if callback(i) == True:
				return i
		else:
			return False

	def filter(self, list, callback):
		result = []
		for i in list:
			if callback(i) == True:
				result.append(i)
		return result

	def reject(self, list, callback):
		result = []
		for i in list:
			if callback(i) == False:
				result.append(i)
		return result

_ = Underscore()
evens = _.filter([1,2,3,4,5], lambda x: x%2 == 0)
print evens

total = _.reduce([1,2,3,4,5], lambda x: x)
print total

find = _.find([1,2,3,4,5], lambda x: x > 2)
print find

filter = _.filter([1,2,3,4,5], lambda x: x > 2)
print filter

reject = _.reject([1,2,3,4,5], lambda x: x > 2)
print reject