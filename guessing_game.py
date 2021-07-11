#import random
from random import randint

guessNumber = int(input("Enter a number between 1 to 5 :"))
randomNumber = randint(1,5)

if guessNumber == randomNumber:
	print("You have won")
else:
	print("You lost")