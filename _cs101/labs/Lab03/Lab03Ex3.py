"""
Lab 3 Ex 3
Author: Cameron Smith
upi: csmi928
"""

def main():
	sentence = get_sentence_from_user()
	number_of_words = count_words(sentence)
	print_number_of_words(sentence, number_of_words)
	
def get_sentence_from_user():
	sentence = input("Enter a sentence: ")
	return sentence
	
def count_words(sentence):
	if len(sentence) == 0:
		return 0
	count = 1
	for letter in sentence:
		if letter == " ":
			count += 1
	return count
	
def print_number_of_words(words, number_of_words):
	print("There are " + str(number_of_words) + " words in the sentence '" + words + "'.")	
	
main()