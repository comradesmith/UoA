"""
Lab 3 Ex 4
Author: Cameron Smith
upi: csmi928
"""

def main():
	formatted_date = format_date(12, 7, 15)
	print(formatted_date)
	formatted_date = format_date(1, 3, 0)
	print(formatted_date)
	
def format_date(day, month, year):
	day = "0" + str(day)
	month = "0" + str(month)
	year = "0" + str(year)
	result = day[-2:] + "/" + month[-2:] + "/" + year[-2:]
	return result
	
main()