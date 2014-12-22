# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.
def add(x,y):
	print x, y
	return x * y

myList = filter(lambda n: n % 2 == 0 or n % 3 == 0, range(1, 10))

print myList
print reduce(add, myList)


# print reduce(lambda x, y: x + y, filter(lambda n: n % 2 == 0 or n % 3 == 0, range(100)))
