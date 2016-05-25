""" COMPSCI 101 S1: ASSIGNMENT 2
	This ain't even my real assignment, but its good practice.
	Author: Cam Smith, csmi928, 706899195
"""
from random import randint

# CHECK IF THE GAME HAS FINISHED
def check_game_finished(game_string):
	first_four_symbols = game_string[0:4]
	if first_four_symbols == "$$$$":
		return True
	
	return False

# PLAY ONE GAME OF COIN STRIP
def play_one_game():
	player_num = 1
	
	game_finished = False
	game_string = create_game_string()
	
	while game_finished == False:
		display_game_string(game_string)
		position_num = get_user_position_num(player_num)
		move_num = get_num_to_move()
		game_string = move_dollar_to_the_left(game_string, position_num, move_num)
		game_finished = check_game_finished(game_string)
		
		if game_finished:
			display_game_string(game_string)
			congratulate_player(player_num)
		else:
			player_num = get_next_player_num(player_num)

def create_game_string():
	game_line = " $ $ $ $ "
	
	game_line = jumble_game_line(game_line)
	game_line = jumble_game_line(game_line)
	game_line = jumble_game_line(game_line)
	game_line = jumble_game_line(game_line)
	game_line = jumble_game_line(game_line)
	game_line = jumble_game_line(game_line)
	game_line = jumble_game_line(game_line)
	
	return game_line
	
def jumble_game_line(game_line):
	random_place = randint(0,8)
	game_line = game_line[:random_place] + game_line[random_place + 1:] + game_line[random_place] #taking a random number, concatenate the part of the string from before and after, then add to the end of the string
	return game_line

def display_game_string(game_string):
	print()
	print("","1 ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9",sep="    ")
	print("||","|","|","|","|","|","|","|","|","|",sep="     ")
	print("||",game_string[0],"|",game_string[1],"|",game_string[2],"|",game_string[3],"|",game_string[4],"|",game_string[5],"|",game_string[6],"|",game_string[7],"|",game_string[8],"|",sep="  ")
	print("||","|","|","|","|","|","|","|","|","|",sep="     ")
	print()
	
def get_user_position_num(player_num):
	print("PLAYER NUMBER:", player_num)
	print()
	position_num = int(input("Enter position number: "))
	return position_num
	
def get_num_to_move():
	move_num = int(input("Enter number to move: "))
	return move_num

def move_dollar_to_the_left(game_string, position_num, to_move):
	zero_to_target_pos = game_string[:position_num - to_move - 1]
	mid_to_old_pos = game_string[position_num - to_move -1: position_num -2]
	old_pos_to_end = game_string[position_num :]
	output = zero_to_target_pos + "$" + mid_to_old_pos + " " + old_pos_to_end
	print(output,)			#debugging only
	print(len(output))		#debugging only
	return output

def get_next_player_num(player_num):
	if player_num == 1:
		return 2
	else:
		return 1
	
def congratulate_player(player_num):
	print(("=" * 25))
	print("** Y O U H A V E W O N **")
	print((5 * " "), "PLAYER NUMBER: ", player_num, sep="")
	print("** Y O U H A V E W O N **")
	print(("=" * 25))
	
def display_menu():
	print()
	print(" 1. PLAY COIN STRIP")
	print(" 2. EXIT")
	user_choice = input("Enter selection: ")
	if user_choice == "1":
		play_one_game()
	
def main():
	play_one_game()
	display_menu()
	print()
	print("BYE FROM COIN STRIP")

main()
