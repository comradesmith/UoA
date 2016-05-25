"""
Lab 6 Ex 2
Author:
This program generates sentences made up of randomly selected words.
"""

import random

def main():
	adjectives_list = get_words_list("adjectives.txt")
	nouns_list = get_words_list("nouns.txt")
	adverbs_list = get_words_list("adverbs.txt")
	verbs_list = get_words_list("verbs.txt")
	sentence = create_sentence(adjectives_list, nouns_list, adverbs_list, verbs_list)
	print(sentence)

def get_words_list(filename):
	file = open(filename, "r")
	words = file.read()
	file.close()
	
	return words.split()
	
def create_sentence(adjectives_list, nouns_list, adverbs_list, verbs_list):
	adjective_1 = get_random_word(adjectives_list).capitalize() + " "
	adjective_2 = get_random_word(adjectives_list) + " "
	noun_1 = get_random_word(nouns_list) + " "
	noun_2 = get_random_word(nouns_list) + "."
	adverb_1 = get_random_word(adverbs_list) + " "
	verb_1 = get_random_word(verbs_list) + " "
	
	sentence = adjective_1 + noun_1 + adverb_1 + verb_1 + adjective_2 + noun_2
	
	return sentence
	

def get_random_word(words_list):
	position = random.randrange(len(words_list))
	
	return words_list[position]
	

main()
	
	

