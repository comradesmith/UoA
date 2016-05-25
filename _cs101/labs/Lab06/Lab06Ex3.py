"""
Lab 6 Ex 3
Author:
This program reads in a file of proverbs and
creates a new file by removing all the vowels.
"""
def main():
	proverbs = read_proverbs("Proverbs.txt")
	create_abbreviated_file(proverbs, "abbreviated-proverbs.txt")
	
def read_proverbs(filename):
	file = open(filename, "r")
	proverbs = file.read()
	file.close()
	
	return proverbs
	
def create_abbreviated_file(proverbs, filename):
	file = open(filename, "w")
	
	vowels = "AEIOUaeiou"
	for character in proverbs:
		if character not in vowels:
			file.write(character)
	
	file.close()
	
main()

	

