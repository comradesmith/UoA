"""
Lab 8 Ex 3
Author:
This program translates words into radio telephone language.
"""
def main():
	radio_telephone_alphabet = ('Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot',
		'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 
		'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'X-ray', 'Yankee', 'Zulu', ' ', ',', '?', '!', '.')
	radio_telephone_dictionary = create_radio_telephone_dict(radio_telephone_alphabet)
	word = get_word_from_user()
	display_translation(word, radio_telephone_dictionary)
	
def create_radio_telephone_dict(radio_telephone_alphabet):
	dictionary = {}
	for word in radio_telephone_alphabet:
		intial_letter = word[0]
		dictionary[intial_letter] = word
		
	return dictionary
	
def get_word_from_user():
	return input("Enter the word to be translated: ")

def display_translation(word, rt_dictionary):
	word = word.upper()
	for character in word:
		print(rt_dictionary[character], end=" ")
		
	
main()