"""
Lab 04 Ex 4.3
Works out the day name of the date entered by the user
"""

def main():
	date = get_date_from_user()
	day_number = determine_day_number(date)
	day_name = get_day_name(day_number)
	display_day_name(date, day_name)
	
def get_date_from_user():
	date = input("Enter a date in the form dd/mm/yyyy: ")
	return date
	
def determine_day_number(date):
	day = int(date[0:2])
	month = int(date[3:5])
	year = int(date[6:10])
	
	anchor = (14 - month) // 12
	y = year - anchor
	m = month + 12 * anchor - 2
	day_number = (day + y + y // 4 - y // 100 + y // 400 + (31 * m) // 12) % 7
	return day_number 

def get_day_name(day_number):
	if day_number == 0:
		return "Sunday"
	elif day_number == 1:
		return "Monday"
	elif day_number == 2:
		return "Tuesday"
	elif day_number == 3:
		return "Wednesday"
	elif day_number == 4:
		return "Thursday"
	elif day_number == 5:
		return "Friday"
	elif day_number == 6:
		return "Saturday"	
		
def display_day_name(date, day_name):
	print(date, "is a", day_name)

main()
	