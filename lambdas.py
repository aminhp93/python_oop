def square(num):
	x = num ** 2
	return x

num = 3
adder = lambda num: num**2
print adder

99
'hello'
[11, 'cat', ("i'm", "a", "tuple")]
2 + 5
"hello" + "world"
True
False
lambda x: x+2

x = 25
# if hungry == True:
	# pass
# for i in (1..4):
	# pass
while True:
	break

my_list = ['test_string', 99, lambda x:x**2]
print my_list[2]
print my_list[2](5)

def invoker(callback):
	print callback(2)

invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)

add10 = lambda x: x + 10
add10(2)
add10(98)

def incrementor(num):
	start = num
	return lambda x: num + x

my_att = [1,2,3,4,5]
def square(num):
	return num ** 2

print map(square, my_att)
print map(lambda x: x ** 2, my_att)