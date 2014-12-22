def isValidMonth (m):
	months =["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	if m in months:
		return True
	return False


invalidListOfMonths = ["asdf", "June", "octavius", "best month ever", "March", "july"];

print filter(isValidMonth, invalidListOfMonths)


# #lambdas
# def isEven(n):
# 	return n % 2 == 0

# print isEven(5)
# print isEven(6)
# g = lambda n: n % 2 == 0

# print g(5)

# # problem: get a list of n numbers between 0 and 20 that are multiples of 3 or 5
# print range(0, 20, 3)
# print range(0, 20, 5)

# for i in range (0, 20):
# 	if i % 3 == 0 or i % 5 == 0:
# 		print i

# def isValid(n):
# 	return n % 3 == 0 or n % 5 == 0;

# print filter(isValid, range(20))

# print filter(lambda n: n % 3 == 0 or n % 5 == 0, range(20))


