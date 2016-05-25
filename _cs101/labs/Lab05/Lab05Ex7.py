"""
Author: csmi928, Cameron Smith, 706899195
Date-written: August 2015
Lab 5 Exercise 5.7
Reverses the order of the elements in a list.
"""

def main():
	original_list = [5, 9, 2.5, "Hello", True, 3, 40, "good"]
	reversed_list = get_reversed_list(original_list)
	print("Original list:", original_list)
	print("Reversed list:", reversed_list)

def get_reversed_list(the_list):
	reversed_list = []
	for item in the_list:
		reversed_list = [item] + reversed_list
	return reversed_list
			
main()