""" Compsci 101 S2; Assignment 2
	A program which plays a game of chance called Dicey.
	Author: Cam Smith, csmi928, 706899195
"""

import random

def main():
	round_number = 1
	player1_total_score = 0
	player2_total_score = 0
	player1_name = "Alan Turing" 
	player2_name = "Charles Babbage" 
	number_of_rounds = 3
	display_welcome()
	while round_number <= number_of_rounds:
		player1_total_score = player1_total_score + process_player_turn(player1_name)
		player2_total_score = player2_total_score + process_player_turn(player2_name)
		display_round_results(round_number, player1_name, player1_total_score, player2_name, player2_total_score)
		round_number = round_number + 1
	display_final_results(player1_name, player1_total_score, player2_name, player2_total_score)
	
def get_list_of_dice_rolls(number_of_rolls):
	result = []
	for roll in range(number_of_rolls):
		single_roll = random.randrange(1,7)
		result = result + [single_roll]
	return result

def get_score(list_of_dice):
	highest_match = get_max_number_of_matches(list_of_dice)
	if highest_match <= 2:
		score = 0
	else:
		score = highest_match
	return score
	
def process_player_turn(player_name):
	display_turn_info(player_name)
	turn_rolls = get_list_of_dice_rolls(5)
	display_dice(turn_rolls)
	matches = get_max_number_of_matches(turn_rolls)
	if matches == 2:
		matching_dice = []
		matching_dice = matching_dice + [get_dice_number_with_two_matches(turn_rolls)]
		matching_dice = matching_dice + [get_dice_number_with_two_matches(turn_rolls)]
		display_exactly_two_matches_message(matching_dice[0])
		turn_rolls = matching_dice + get_list_of_dice_rolls(3)
		display_dice(turn_rolls)
	score = get_score(turn_rolls)
	return score
	
def get_how_many_match(value_to_match, list_of_dice):
	count = 0
	for roll in list_of_dice:
		if roll == value_to_match:
			count = count + 1
	return count
	
def get_dice_number_with_two_matches(list_of_dice):
	for roll in list_of_dice:
		if get_how_many_match(roll, list_of_dice) == 2:
			return roll
	
def get_max_number_of_matches(list_of_dice):
	match_list = []
	for roll in range(1, 7):
		match_list = match_list + [get_how_many_match(roll, list_of_dice)]
	return max(match_list)
	
def display_welcome():
	print()
	print("Welcome to DICEY, written by csmi928")
	print()
	
def display_turn_info(player_name):
	turn_info = "  " + player_name + "'s turn"
	print(turn_info)
	
def display_dice(list_of_dice):
	print("    Dice:  ", end="")
	for roll in list_of_dice:
		print(roll," ", sep="", end="")
	print()
	
def display_exactly_two_matches_message(dice_number):
	message = "    Two " + str(dice_number) + "'s.  Roll the remaining 3 dice."
	print(message)
	
def display_round_results(round_number, player1_name, player1_score, player2_name, player2_score):
	player_1_section = player1_name + " has " + str(player1_score) + " points, and "
	player_2_section = player2_name + " has " + str(player2_score) + " points"
	round_results = "Round " + str(round_number) + " results: " + player_1_section + player_2_section
	print(round_results)
	print()
	
def display_final_results(player1_name, player1_score, player2_name, player2_score):
	is_tie_message = "The result is a tie"
	winner_player1_message = "Congratulations to " + player1_name
	winner_player2_message = "Congratulations to " + player2_name
	print()
	if player1_score == player2_score:
		print("*" * len(is_tie_message))
		print(is_tie_message)
		print("*" * len(is_tie_message))
	elif player1_score > player2_score:
		print("*" * len(winner_player1_message))
		print(winner_player1_message)
		print("*" * len(winner_player1_message))
	elif player2_score > player1_score:
		print("*" * len(winner_player2_message))
		print(winner_player2_message)
		print("*" * len(winner_player2_message))
	print()
	
main()