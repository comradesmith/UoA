"""
Lab 7 Ex 4
Author:
Date: February 2015
This program prints all the week days followed
by every second day in the week starting with Monday.

"""

def main(): 
	months_tuple = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
	winter_months = get_winter_months(months_tuple)
	alternate_months = get_alternate_months(months_tuple)
	print_summary(winter_months, alternate_months)
	
def get_winter_months(months_tuple):
	winter_months = months_tuple[5:8]
	return winter_months
	
def get_alternate_months(months_tuple):
	alternate_months = months_tuple[0::2]
	return alternate_months

def print_summary(winter_months, alternate_months):
	print("Winter months:", winter_months)
	print("Alternate months:", alternate_months)
	
main()    



