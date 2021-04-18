import random

random_number = random.randint(1,10)

guess = None

while guess != random_number:
	guess = int(input("Guess a number between 1 and 10: "))
	if (guess < random_number):
		print("Too low, try again!")
		print(guess)
	elif (guess > random_number):
		print("Too high, try again!")
		print(guess)
	else:
		print("You guessed it! you won!")
		yorno = input("Do you want to keep playing? (y/n) ")
		if yorno == "y":
			random_number = random.randint(1,10)
			guess = None
		else:
			print("Thank you for playing!")
			break
			




