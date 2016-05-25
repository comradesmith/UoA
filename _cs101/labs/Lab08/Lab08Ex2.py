"""
Lab 8 Ex 2
Author:
This program reads in a file of palindromes and produces a summary of the word lengths of the palindromes.
"""
def main():
	palindromes_list = get_palindromes_list("palindromes.txt")
	word_length_dictionary = create_word_length_dictionary(palindromes_list)
	display_summary(word_length_dictionary)
	
def get_palindromes_list(filename):
	file = open(filename, "r")
	contents = file.read()
	contents = contents.split()
	file.close()
	return contents
	
def create_word_length_dictionary(palindromes_list):
	lengths_dict = {}
	
	for palindrome in palindromes_list:
		if len(palindrome) not in lengths_dict:
			lengths_dict[len(palindrome)] = [palindrome]
		else:
			lengths_dict[len(palindrome)] += [palindrome]


	return lengths_dict
			
def display_summary(word_length_dictionary):
		print("Palindromes Summary")
		print("===================")
		
		for key in word_length_dictionary.keys():
			print("Word length of ", key, ":", sep = "")
			for palindrome in word_length_dictionary[key]:
				print(palindrome, end=" ", sep="")
			print()
			print()
		
main()