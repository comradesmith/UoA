""" Compsci 101 S2; Assignment 1 Question 5
	A simple game where users replace two characters of a word at a time.
	Author: Cam Smith, csmi928, 706899195
"""

def main():
	word = "frank"
	word_chain = word + "->"
	counter = 0
	print("Starting word: " + word)
	word = play_round(word, counter)
	counter = counter + 1
	word_chain = build_word_chain(word_chain,word)
	word = play_round(word, counter)
	counter = counter + 1
	word_chain = build_word_chain(word_chain,word)
	word = play_round(word, counter)
	counter = counter + 1
	word_chain = build_word_chain(word_chain,word)
	word = play_round(word, counter)
	counter = counter + 1
	word_chain = build_word_chain(word_chain,word)	
	border = len(word_chain) * "="
	print(border)
	print(word_chain)
	print(border)
	
	
def get_user_position():
	position = input("Position: ")
	return position

def get_user_letters():
	new_letters = input("Replacement letters: ")
	return new_letters

def change_word(word, user_letters, user_position):
	new_word = word[:user_position] + user_letters + word[user_position + 2:]
	return new_word

def build_word_chain(word_chain, word):
	result = word_chain + word + "->"
	return result

def play_round(word, counter):
	user_position = int(get_user_position())
	user_letters = get_user_letters()
	word = change_word(word, user_letters, user_position)
	print(str(counter) + " Word is now: " + word)
	return word

main()