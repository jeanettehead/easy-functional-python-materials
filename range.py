#!/usr/bin/python

import sys

#grab command line input
if len(sys.argv) > 1:
	argument = sys.argv[1];

	if argument == "1":
		print "range(5)"
		raw_input("press enter to evaluate...")
		print range(5)

	elif argument == "2":
		print "range(5, 10)"
		raw_input("press enter to evaluate...")
		print range(5, 10)

	elif argument == "3":
		print "range(10, 20, 2)"
		raw_input("press enter to evaluate...")
		print range(10, 20, 2)

	elif argument == "4":
		print "range(20, 8, -2)"
		raw_input("press enter to evaluate...")
		print range(20, 8, -2)

	elif argument == "10":
		for i in range(99, 0, -1):
			print('{0} bottles of beer on the wall, {0} bottles of beer!'.format(i))
			print('So take it down, pass it around, {0} more bottles of beer on the wall!'.format(i - 1))
			#could add an if statement to catch "1" and print bottle instead of bottles
	else:
		print "invalid argument"
else:
	print "please add an argument (ie python range.py 1)"

