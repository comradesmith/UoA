"""
Author: csmi928, Cameron Smith, 706899195
Date-written: August 2015
Lab 5 Exercise 5.3
Finds the biggest word in a list of words
"""

def main():
	words_list = ["pig", "country", "short", "bye", "shorthand", "cat", "elephant", "at", "bye", "hello" ]
	biggest_word = get_biggest_word(words_list)
	print('"' + biggest_word + '"' + " is the biggest word in the list.")
	
def get_biggest_word(words_list):
	biggest_word = words_list[0]
	for word in words_list:
		if len(biggest_word) < len(word):
			biggest_word = word
	return biggest_word
			
main()