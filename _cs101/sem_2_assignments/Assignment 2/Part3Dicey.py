"""
This program is used to test the three part 3 functions.
Complete the three functions.
The expected output is shown in the comment at the bottom of this file.

*** MAKE SURE YOU COPY YOUR PART 1 AND PART 2 FUNCTIONS INTO THIS PROGRAM ***
Author: Adriana Ferraro
"""

import random

#----------------------------------------------------------
# Main function - Testing Part 3 of assignment 2
#----------------------------------------------------------
def main():
	print("get_list_of_dice_rolls()")
	print("Note:  the dice values are random so your output will be different.")
	print()
	dice_rolls1 = get_list_of_dice_rolls(3) 
	dice_rolls2 = get_list_of_dice_rolls(1) 
	dice_rolls3 = get_list_of_dice_rolls(5) 
	dice_rolls4 = get_list_of_dice_rolls(4) 
	print("Should be a list of 3 random dice values:", dice_rolls1)
	print("Should be a list of 1 random dice value:", dice_rolls2)
	print("Should be a list of 5 random dice values:", dice_rolls3)
	print("Should be a list of 4 random dice values:", dice_rolls4)
	print("---------------------------")
	print("---------------------------")
	print("get_score()")
	score1 = get_score([4, 6, 6, 6, 6]) 
	score2 = get_score([4, 5, 6, 5, 6]) 
	score3 = get_score([6, 6, 2, 2, 2]) 
	score4 = get_score([5, 5, 6, 5, 5]) 
	score5 = get_score([6, 6, 6, 6, 6]) 
	score6 = get_score([6, 5, 1, 3, 2]) 
	print(score1, score2, score3, score4, score5, score6)
	print("---------------------------")
	print("---------------------------")
	print("Note:  the dice values are random so your output will be different.")
	print("Check that the scores are correct for the dice which are rolled.")
	print()
	print("process_player_turn()")
	player_score1 = process_player_turn("Adriana")
	print("Player score: ", player_score1)
	print()
	player_score2 = process_player_turn("Joe")
	print("Player score: ", player_score2)
	print("---------------------------")
	print("---------------------------")
#----------------------------------------------------------
# Functions which process a player's turn.
# Complete the following 3 functions below.
#----------------------------------------------------------
def get_list_of_dice_rolls(number_of_rolls):
	result = []
	for i in range(number_of_rolls):
		single_roll = random.randrange(1,7)
		result = result + [single_roll]
	return result

def get_score(list_of_dice):
	matches = get_max_number_of_matches(list_of_dice)
	if matches <= 2:
		score = 0
	else:
		score = matches
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
	get_score(turn_rolls)
#----------------------------------------------------------
# Functions from part 2
# which obtain the maximum number of matches and
# the dice number if there are exactly two matches
#----------------------------------------------------------
def get_how_many_match(value_to_match, list_of_dice):
	count = 0
	for i in list_of_dice:
		if i == value_to_match:
			count += 1
	return count
	
def get_dice_number_with_two_matches(list_of_dice):
	match_list = []
	match_list = match_list + [get_how_many_match(1, list_of_dice)]
	match_list = match_list + [get_how_many_match(2, list_of_dice)]
	match_list = match_list + [get_how_many_match(3, list_of_dice)]
	match_list = match_list + [get_how_many_match(4, list_of_dice)]
	match_list = match_list + [get_how_many_match(5, list_of_dice)]
	match_list = match_list + [get_how_many_match(6, list_of_dice)]
	for index in range(len(match_list)):
		if match_list[index] == 2:
			return index + 1
	
def get_max_number_of_matches(list_of_dice):
	match_list = []
	match_list = match_list + [get_how_many_match(1, list_of_dice)]
	match_list = match_list + [get_how_many_match(2, list_of_dice)]
	match_list = match_list + [get_how_many_match(3, list_of_dice)]
	match_list = match_list + [get_how_many_match(4, list_of_dice)]
	match_list = match_list + [get_how_many_match(5, list_of_dice)]
	match_list = match_list + [get_how_many_match(6, list_of_dice)]
	return max(match_list)
	
#----------------------------------------------------------
# Functions from part 1
#----------------------------------------------------------	
def display_welcome():
	print()
	print("Welcome to DICEY, written by csmi928")
	print()
	
def display_turn_info(player_name):
	turn_info = "  " + player_name + "'s turn"
	print(turn_info)
	
def display_dice(list_of_dice):
	print("    Dice:  ", end="")
	for element in list_of_dice:
		print(element," ", sep="", end="")
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

"""
EXPECTED OUTPUT FOR PART 3
get_how_many_match()
3 2 0 3 1
---------------------------
---------------------------
get_dice_number_with_two_matches()
5 4 3 2 4
---------------------------
---------------------------
get_max_number_of_matches()
2 2 1 2 3
---------------------------
---------------------------
MineDevelopment:511 % python3 Part3Dicey.py 
get_list_of_dice_rolls()
Note:  the dice values are random so your output will be different.

Should be a list of 3 random dice values: [6, 4, 2]
Should be a list of 1 random dice value: [6]
Should be a list of 5 random dice values: [1, 4, 3, 5, 3]
Should be a list of 4 random dice values: [2, 1, 3, 3]
---------------------------
---------------------------
get_score()
4 0 3 4 5 0
---------------------------
---------------------------
Note:  the dice values are random so your output will be different.
Check that your scores are correct for the dice which are rolled.

process_player_turn()
  Adriana's turn
    Dice:  6 2 3 4 5
Player score:  0

  Joe's turn
    Dice:  5 2 6 1 2
    Two 2's. Roll the remaining 3 dice.
    Dice:  2 2 6 4 6
Player score:  0
---------------------------
---------------------------
"""

