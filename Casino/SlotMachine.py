import random
slotReelValues = ["BAR", "7", "777", "Cherry"]

def printSlots(randOne, randTwo, randThree):
	print("\n" + slotReelValues[randOne] + " | " + slotReelValues[randTwo] + " | " + slotReelValues[randThree])

def checkIfWinner(randOne, randTwo, randThree):
	if(slotReelValues[randOne] == slotReelValues[randTwo] and slotReelValues[randTwo] == slotReelValues[randThree]):
		print("\nWinner.")
	else:
		print("\nSorry, try again loser.")

def printMenu():
	print("\nSelect an option...")
	print("1. Spin")
	print("2. Exit")

userMenuChoice = 0
while(userMenuChoice >= 0 and userMenuChoice <= 1):
	printMenu()

	try:
		userMenuChoice = int(input("Your selection: "))
	except:
		print("Error converting input to int")
		userMenuChoice = 0

	# Spin the reels
	if(userMenuChoice == 1):
		reelValue_one = random.randrange(len(slotReelValues))
		reelValue_two = random.randrange(len(slotReelValues))
		reelValue_three = random.randrange(len(slotReelValues))

		printSlots(reelValue_one, reelValue_two, reelValue_three)
		checkIfWinner(reelValue_one, reelValue_two, reelValue_three)

	# Exit Program
	elif(userMenuChoice == 2):
		print("Thanks for playing")
	
	else:
		print("Unexpected User Input Error")
