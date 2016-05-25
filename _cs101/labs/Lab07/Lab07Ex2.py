"""
Lab 7 Ex 2
Author:
Date: September, 2015
This program generates and prints all the anagrams
of the word entered by the user.

"""
def main():
	words_list = get_words_list("words.txt")
	word = get_word_from_user()
	anagrams_tuple = get_anagrams(word, words_list)
	print(anagrams_tuple)
	
def get_words_list(filename):
	input_file = open(filename, "r")
	input_data = input_file.read()
	input_file.close()
	input_data = input_data.split()
	return input_data
	
def get_word_from_user():
	 word = input("Enter a word: ")
	 return word
	 
def convert_to_sorted_letters(word):
	letters = list(word)
	letters.sort()
	return letters
	
def get_anagrams(user_word, words_list):
	user_word_letters = convert_to_sorted_letters(user_word)
	anagrams = []
	for word in words_list:
		word_letters = convert_to_sorted_letters(word)
		if word_letters == user_word_letters:
			anagrams = anagrams + [word]
	anagrams = tuple(anagrams)
	return anagrams
	
main()    



