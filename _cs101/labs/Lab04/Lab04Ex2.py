"""
Lab 04 Exercise 4.2
Plays the "guess my number" game
"""
import random

def main():
	play_guessing_game()
	
def play_guessing_game():
	target = random.randrange(1, 101)
	guess = 0
	while guess != target:
		guess = get_guess_from_user()
		if guess > target:
			print(guess, "is too high")
		elif guess < target:
			print(guess, "is too low")
	print("Yes. Well done!!")
	
def get_guess_from_user():
	guess = int(input("Guess a number between 1 and 100: "))
	return guess
	
		
main()
	