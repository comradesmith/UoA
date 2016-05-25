"""
Author: csmi928, Cameron Smith, 706899195
Date-written: August 2015
Lab 5 Exercise 5.1
Prints all the years which are leap years.
"""

def main():
	years = [2015, 1500, 1904, 1200, 2001, 2000, 1962, 2900, 1600, 1865, 2016, 1984, 1964]
	print_leap_years(years)
	
def print_leap_years(years_list):
	print("Leap Years")
	print("==========")
	print()
	for year in years_list:
		if year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0):
			print(year, end=" ")
	print()
	
	
main()