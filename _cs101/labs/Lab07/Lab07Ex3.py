"""
Lab 7 Ex 3
Author:
Date: February 2015
This program prints a list of famous couples.

"""

def main(): 
	couples = [("Adam", "Eve"), ("Samson", "Deliah"),
			("Antony", "Cleopatra"), ("Tarzan", "Jane"),("Robin Hood", "Maid Marian"), ("Lancelot", "Guinevere")]
	print_couples(couples)
	
def print_couples(couples):
	for couple in couples:
		print(couple[0], "and", couple[1])
main()    



