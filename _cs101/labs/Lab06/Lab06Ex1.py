"""
Lab 6 Ex 1
Author: Cam Smith, csmi928, 706899195
This program creates a file of palindromes.
"""

def main():
	words_list = get_words_list("words.txt")
	create_file_of_palindromes(words_list, "palindromes.txt")

def get_words_list(filename):
	file = open(filename, "r")
	words = file.read()
	file.close()
	
	return words.split()

def create_file_of_palindromes(words_list, output_filename):
	file = open(output_filename, "w")
	
	for word in words_list:
		if word == word[::-1]:
			file.write(word + "\n")
	
	file.close()
	
main()
	
	

