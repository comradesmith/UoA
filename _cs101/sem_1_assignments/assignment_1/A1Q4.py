"""	COMPSCI 101 S2: ASSIGNMENT 1, QUESTION 4
	Author: Cam Smith, csmi928, 706899195
"""

number = 932
number = str(number)
count = 0

for digit in range(len(number)):
	count = count + int(number[digit])

print("The sum of all digits is", count)