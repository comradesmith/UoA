"""
Author: csmi928, Cameron Smith, 706899195
Date-written: August 2015
Lab 5 Exercise 5.4
Outputs a list of words that contain a particular letter.
"""

def main():
	selected_words = get_selected_words("a", "The road was long and winding")
	print("List of words containing a:", selected_words)
	selected_words = get_selected_words("e", "The quick brown fox jumps over the lazy dog")
	print("List of words containing e:", selected_words)
	
def get_selected_words(letter, sentence):
	sentence = sentence.lower()
	word_list = sentence.split()
	result_list = []
	for word in word_list:
		if letter in word and not word in result_list:
			result_list = result_list + [word]
	return result_list
			
main()