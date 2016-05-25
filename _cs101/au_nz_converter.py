"""	COMPSCI 101 S2: LECTURE 2 CHALLENGE
	Author: Cam Smith
"""

amount_to_convert = 500
nz_to_aus_rate = 0.95
# Calculations and assignment below
nz_dollars = amount_to_convert / nz_to_aus_rate
au_dollars = amount_to_convert * nz_to_aus_rate
# Printing of the results below
print("AUD $", amount_to_convert, " in NZD is $", nz_dollars, sep="")
print("NZD $", amount_to_convert, " in AUD is $", au_dollars, sep="")