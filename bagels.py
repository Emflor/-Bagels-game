import random
NUM_DIGITS = 3
MAX_GUESS = 10

def main():
	print('''Bagels, a deductive logic game. 
		By Emil Flores emilf.jobs@gmail.com

		I am thinking of a digit 3-digit number with no repeated digits.
		Try to guess what it is. Here are some clues...
		When I say:		That means:
		Pico			One digit is correct but in the wrong position.
		Fermi			One digit is correct and in the right position.
		Bagels			No digits are correct. 
	''')

	while True:
		secretNum = getSecretNum()
		print("I have thought of a number.")
		print("You have {} guesses to get it.".format(MAX_GUESS))

		numGuesses = 1
		while numGuesses <= MAX_GUESS:
			guess = ''
			#Keep looping until user enters a valid guess
			while len(guess) != NUM_DIGITS or not guess.isdecimal():
				print("Guess #{}: ".format(numGuesses))
				guess = input("> ")


			clues = getClues(guess, secretNum)
			print(clues)
			numGuesses += 1


			if guess == secretNum:
				break #They guessed it so break out of this loop
			if numGuesses > MAX_GUESS:
				print("You ran out of guesses.")
				print("The answer was {}.".format(secretNum))


		#Ask if user wants to play again
		print("Do you want to play again? (yes or no)")
		if not input('> ').lower().startswith('y'):
			break
	print("Thanks for playing!")

def getSecretNum():
	"""Returns a string made up of NUM_DIGIST unique random digits"""
	numbers = list("0123456789") #create a list of digits 0-9
	random.shuffle(numbers) #shuffle them into random order

	#Get the first NUM_DIGITS digits in the list for the secret number:
	secretNum = ''
	for i in range(NUM_DIGITS):
		secretNum += str(numbers[i])
	return secretNum

def getClues(guess, secretNum):
	"""Returns a string with the pico, fermi, bagels clues for a guess and secret number pair"""
	if guess == secretNum:
		return "You've got it!"


	clues = []

	for i in range(len(guess)):
		if guess[i] == secretNum[i]:
			# A correct digit is in the correct place.
			clues.append('Fermi')
		elif guess[i] in secretNum:
			# A correct digit is in the incorrect place.
			clues.append('Pico')
	if len(clues) == 0:
		return 'Bagels' #There are not correct digits at all.
	else:
		#sort the clues into alphabetical order so their original order 
		#doesnt give information away.
		clues.sort()
		#Make a single string from the list of string clues
		return ' '.join(clues)

if __name__ == '__main__':
	main()
