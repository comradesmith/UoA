"""	COMPSCI 101 S2: ASSIGNMENT 1, QUESTION 2
	Author: Cam Smith, csmi928, 706899195
"""

completion_per_attempt = 0.6627
yards_per_attempt = 6.9219
touchdowns_per_attempt = 0.0486
interceptions_per_attempt = 0.0250

part_1 = (completion_per_attempt - 0.3) * 5
part_2 = (yards_per_attempt - 3) / 4
part_3 = touchdowns_per_attempt * 20
part_4 = 2.375 - (interceptions_per_attempt * 25)

passer_rating = ( (part_1 + part_2 + part_3 + part_4) / 6) * 100

print("The passer rating is", passer_rating)