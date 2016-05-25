"""
Lab 04 Exercise 4.4
Displays a message about the entered weight based on the bmi

"""

def main():
	weight = get_weight_from_user()
	height = get_height_from_user()
	bmi = calculate_bmi(weight, height)
	display_bmi_message(bmi)
	
def get_weight_from_user():
	return float(input("Enter weight: "))
	
def get_height_from_user():
	return float(input("Enter height: "))

def calculate_bmi(weight, height):
	bmi = round(weight / height ** 2)
	return bmi

def display_bmi_message(bmi):
	print("bmi is ", bmi, ".", sep="")
	if bmi < 19:
		print("Weight may be too low.")
	elif bmi > 25:
		print("Weight may be too high.")
	else:
		print("This is a healthy weight.")
			
main()
	