#alternative to for loop, maybe not used as much but is still helpful
#for i loop, you have a very clear start and finish determined
#while loop will not stop when it reaches the end of the list, it has to be explicitly told to stop
#might forget to give stopping place which is infinite and will crash program
#sentinel value will tell while loop to stop
#nums = list(range(1,100))

#while len(nums) > 0:
#	print(nums.pop())

#guessing game

def guessing_game():
	while True:
		print('What is your guess?')
		guess = input()

		if guess == '42':
			print('You correctly guessed it!')
			return False
		else:
			print(f'No, {guess} is not the answer, please try again\n')

guessing_game()			