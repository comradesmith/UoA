"""
Lab 8 Ex 1
Author:
This program produces a letter count summary of the sentence entered by the user.
"""
def main():
	sentence = get_sentence_from_user()
	sentence = sentence.lower()
	letter_counts_dict = count_letter_occurrences(sentence)
	print(letter_counts_dict)
	
def get_sentence_from_user():
	return input("Enter a sentence: ")
	
def count_letter_occurrences(sentence):
	counts = {}
	sentence = sentence.lower()
	for char in sentence:
		if char.isalpha():
			if char in counts:
				counts[char] += 1
			else:
				counts[char] = 1
	return counts
	
	
main()