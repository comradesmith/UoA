""" Compsci 101 S2; Assignment 1 Question 2
	Simulates bank account activity
	Author: Cam Smith, csmi928, 706899195
"""

import random

def main():
	balance = 11568
	display_intial_balance(balance)
	working_balance = random_transaction(balance, 1)
	working_balance = random_transaction(working_balance, 2)
	working_balance = random_transaction(working_balance, 3)
	working_balance = random_transaction(working_balance, 4)
	sum_of_transactions(balance, working_balance)


def display_intial_balance(initial_balance):
	initial_message = "Initial balance: $" + str(initial_balance)
	print(initial_message)
	
def random_transaction(initial_balance, transaction_number):
	random_number = random.randrange(100, 151)
	random_multiplier = random.randrange(-1, 2, 2)
	new_balance = initial_balance + (random_number * random_multiplier)
	transaction_message = str(transaction_number) + ": $" + str(new_balance) + "  (" + str(random_number * random_multiplier) + ")"
	print(transaction_message)
	return new_balance

def sum_of_transactions(initial_balance, current_balance):
	balance_difference = current_balance - initial_balance
	sum_message = "Sum of transactions: $" + str(balance_difference)
	print("=" * 26, sep="")
	print(sum_message)
	print("=" * 26, sep="")

main()