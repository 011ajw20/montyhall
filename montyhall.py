#This program is a simulation of the monty hall problem, with 3 doors.
#Aron Wiley
#March 23rd 2019

import random
import math
global times
times = 10000.0

#This function is for when the player swaps what door they choose when offered
#to after having one goat revealed.
def swap(choice):
	#Define the doors, the first door always has the car.
	doors = {'0':1, '1':0, '2':0}
	#If the choice is the first door or the second door
	if (choice == 0 or choice == 1):
		doors.pop('2') #'show' the 3rd door.
		#Swap what door they have.
		if (choice == 0):
			choice = 1
		elif (choice == 1):
			choice = 0
	#If the choice is the first or third door
	elif (choice == 0 or choice == 2):
		doors.pop('1') #'show' the 2nd door.
		#Swap what door they have.
		if (choice == 0):
			choice = 2
		elif (choice == 2):
			choice = 0
	#If they choose one with a goat, show a goat and swap them to a car.
	elif (choice == 1 or choice == 2):
		choice = 0
	#Return 1 or 0, this is used for our average
	if (choice == 0):
		return 1
	elif (choice == 1 or choice == 2):
		return 0

#This one just checks to see if they got the door with the car.
def keep(choice):
	if (choice == 0):
		return 1
	else:
		return 0
	
def main(args):
	#these are just starting vaiables.
	x = 0
	totalKeep = 0
	totalChange = 0
	#run for 'times'
	while (x < times):
		#choose a random number (0-2)
		choice = random.randint(0,2)
		#swap doors and keep doors then add to total.
		if (keep(choice) == 1):
			totalKeep = totalKeep + 1
		if (swap(choice) == 1):
			totalChange = totalChange + 1
		x = x + 1
	#find the average
	keepAverage = (float(float(totalKeep)/times)*100.0)
	changeAverage = (float(float(totalChange)/times)*100.0)
	#print it out.
	print ("When you don't change doors you about a " + str(keepAverage) + "% chance to get the car.\n\n")
	print ("When you change doors you have about a " + str(changeAverage) + "% chance to get the car.")
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
