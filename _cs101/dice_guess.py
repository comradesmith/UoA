""" Lecture 3 excercises
	Author: Cam Smith
"""

import random

def roll_dice(number):
	result = random.randrange(1,number * 6)
	return result

def get_guess(number):
	print("Rolling", number, "dice")
	result = int( input("Enter your guess ") )
	return result

number_to_roll = int( input("How many dice to roll: "))
user_guess = get_guess(number_to_roll)
roll = roll_dice(number_to_roll)
error_margin = abs(user_guess - roll)
print(number_to_roll, "dice were rolled. You guessed a sum of", user_guess, "The true sum was:", roll)
print("You were out by", error_margin)