"""
This program is used to test the six part 1 functions.
Complete the six functions.
The expected output is shown in the comment at the bottom of this file.
Author: Adriana Ferraro
"""

#----------------------------------------------------------
# Main function - Testing Part 1 of assignment 2
#----------------------------------------------------------
def main():
	print("display_welcome()")
	display_welcome()
	print("---------------------------")
	print("---------------------------")
	print("display_turn_info()")
	display_turn_info("Harry")
	display_turn_info("Joe")
	print("---------------------------")
	print("---------------------------")
	print("display_dice()")
	display_dice([2, 2, 4, 6, 3])
	display_dice([3, 6, 4, 3, 5])
	display_dice([2, 6, 4, 6])
	print("---------------------------")
	print("---------------------------")
	print("display_exactly_two_matches_message()")
	display_exactly_two_matches_message(4)
	display_exactly_two_matches_message(1)
	print("---------------------------")
	print("---------------------------")
	print("display_round_results()")
	display_round_results(2, "Adriana", 6, "Bruno", 7) 
	display_round_results(1, "Jim", 4, "Jill", 3) 
	print("---------------------------")
	print("---------------------------")
	print("display_final_results()")
	display_final_results("Fred", 9, "Hilbert", 10)
	display_final_results("Erica", 9, "Edward", 9)
	display_final_results("Jerry", 15, "Jordan", 0)
	print("---------------------------")
	print("---------------------------")
#----------------------------------------------------------
# All the functions which print information to the 
# standard output window.  
# Complete the following 6 functions below.
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
EXPECTED OUTPUT FOR PART 1
display_welcome()

Welcome to DICEY, written by afer023

---------------------------
---------------------------
display_turn_info()
  Harry's turn
  Joe's turn
---------------------------
---------------------------
display_dice()
    Dice:  2 2 4 6 3
    Dice:  3 6 4 3 5
    Dice:  2 6 4 6
---------------------------
---------------------------
display_exactly_two_matches_message()
    Two 4's. Roll the remaining 3 dice.
    Two 1's. Roll the remaining 3 dice.
---------------------------
---------------------------
display_round_results()
Round 2 results: Adriana has 6 points, and Bruno has 7 points

Round 1 results: Jim has 4 points, and Jill has 3 points

---------------------------
---------------------------
display_final_results()

**************************
Congratulations to Hilbert
**************************


*******************
The result is a tie
*******************


************************
Congratulations to Jerry
************************

---------------------------
---------------------------
"""
