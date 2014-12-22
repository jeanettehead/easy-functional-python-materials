#problem: get a list of even numbers between 0 and 20

# print range(0, 20, 2)

# for i in range (0, 20):
# 	if i % 2 == 0:
# 		print i


# def isEven(n):
# 	return n % 2 == 0:

# # myList = range(20)
# # print myList
# # print filter(isEven, myList)

# print filter(isEven, range(20))


#a list of numbers between 0 and 20 
#that are divisible by 3 or by 5

threes = range(0,20,3)
fives = range(0,20,5)
print threes + fives


def isValid(n):
	if n%3 == 0 or n%5==0:
		return True
	else:
		return False

max = 15
myList = [233,211,2,3,54,"sunday"]

print filter(isValid, range(0,15))















