"""
Author: csmi928, Cameron Smith, 706899195
Date-written: August 2015
Lab 5 Exercise 5.2
Outputs words which are less than 3 letters long
"""

def main():
	words_list = ["piano", "hat", "hello", "egg", "good", "he", "aeroplane", "a", "the"]
	short_letter_words_list = create_short_letter_words_list(words_list)
	print(short_letter_words_list)
	
def create_short_letter_words_list(words_list):
	short_words_list = []
	for word in words_list:
		if len(word) <4:
			short_words_list = short_words_list + [word]
	return short_words_list
			
main()