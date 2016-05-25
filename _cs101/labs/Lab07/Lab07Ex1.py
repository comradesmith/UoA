"""
Lab 7 Ex 1
Author:
This program calculates and prints the area and perimeter
of a rectangle.  The length and width are entered by the user.
Date: September, 2015
"""

def main(): 
	length, width = get_length_and_width()
	area, perimeter = calculate_area_and_perimeter(length, width) 
	print_area_and_perimeter(area, perimeter) 
	
def get_length_and_width():
	length = float(input("Enter length: "))
	width = float(input("Enter width: "))
	return length, width
	
def calculate_area_and_perimeter(length, width) :
	area = length * width
	perimeter = (length + width) * 2
	return (area, perimeter)

def print_area_and_perimeter(area, perimeter):
	print("Area of rectangle is:", round(area,1), "square cms.")
	print("Perimeter of rectangle is:", round(perimeter,1), "cms.")
	
main()    



