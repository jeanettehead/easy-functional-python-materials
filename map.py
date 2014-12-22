#map

def square(x):
	return x**2

print square(5)

#print square of every number between 0 and 10

print map(square, range(10))

print map(lambda n: n**2, range(10))


#print square of every number that is a multiple of 3 or 5 between 0 and 20

print map(lambda n: n**2, filter(lambda n: n%3==0 or n%5==0, range(20)))