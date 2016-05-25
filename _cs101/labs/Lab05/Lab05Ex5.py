"""
Author: csmi928, Cameron Smith, 706899195
Date-written: August 2015
Lab 5 Exercise 5.5
Rounds a list of numbers to whole numbers.
"""

def main():
	numbers = [7.5, 8.5, 7.3, 3.7, 4.21, 5.25, 49.18]
	print("Original list of numbers:", numbers)
	round_to_whole_numbers(numbers)
	print("List of numbers is now:  ", numbers)
	
def round_to_whole_numbers(numbers_list):
	for i in range(len(numbers_list)):
		numbers_list[i] = round(numbers_list[i])

	
main()