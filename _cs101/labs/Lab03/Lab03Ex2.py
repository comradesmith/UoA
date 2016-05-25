"""
Lab 3 Ex 2
Author: Cameron Smith
upi: csmi928
"""

def main():
	anns_bmi = calculate_bmi(63.2, 1.64)
	print_bmi("Ann", anns_bmi)
	
	bretts_bmi = calculate_bmi(79.2, 1.75)
	print_bmi("Brett", bretts_bmi)
	
	johns_bmi = calculate_bmi(85.5, 2.2)
	print_bmi("John", johns_bmi)

def calculate_bmi(weight, height):
	bmi = weight / (height * height)
	return round(bmi, 1)

def print_bmi(name, bmi):
	print(name, "'s bmi is: ", bmi, ".", sep="")

	
main()

