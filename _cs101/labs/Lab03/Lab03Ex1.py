"""
Lab 3 Ex 1
Author: Cameron Smith
upi: csmi928
"""

def main():
	ounces = get_ounces_from_user()
	grams = convert_ounces_to_grams(ounces)
	print_conversion(ounces, grams)
	
def get_ounces_from_user():
	ounces = int(input("Enter ounces: "))
	return ounces
	
def convert_ounces_to_grams(ounces):
	grams = ounces * 28.3495231
	return round(grams)

def print_conversion(ounces, grams):
	print(ounces, "Ounces is equivalent to", grams, "grams") 
	
main()

