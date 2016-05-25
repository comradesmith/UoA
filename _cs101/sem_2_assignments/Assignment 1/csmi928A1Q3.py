""" Compsci 101 S2; Assignment 1 Question 3
	Displays a 5 character long string as a parallelogram
	Author: Cam Smith, csmi928, 706899195
"""

word = "MARIA"

def display_border():
	print("*" * 9)
	print("*" * 9)
	
line_1 = " " * 6 + word[:1]
line_2 = " " * 5 + word[1:3]
line_3 = " " * 4 + word[1:4]
line_4 = " " * 3 + word[1:5]
line_5 = " " * 2 + word
line_6 = " " * 2 +word[1:]
line_7 = " " * 2 +word[2:]
line_8 = " " * 2 +word[3:]
line_9 = " " * 2 +word[4:]

display_border()
print(line_1)
print(line_2)
print(line_3)
print(line_4)
print(line_5)
print(line_6)
print(line_7)
print(line_8)
print(line_9)
display_border()
