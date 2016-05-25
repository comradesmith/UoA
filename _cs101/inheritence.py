"""	COMPSCI 101 S2: LECTURE 3 CHALLENGE
	Author: Cam Smith
"""

import random

total_inheritence = 1587654
administrator_percent = 0.0025
parents = 2
children = 3
relatives = 10

# divide inheritence into portions
# find and remove the administrators rate
number_of_portions = relatives + (children * 100) + (parents * 2 * 100)
administrators_share = (total_inheritence * administrator_percent) //1 # floor division to round off the cents
total_inheritence = total_inheritence - administrators_share
amount_per_portion = total_inheritence // number_of_portions

# determine amount of share for each type of inheritor
relatives_share = 1 * amount_per_portion
childrens_share = amount_per_portion * 100
parents_share = amount_per_portion * 2 * 100

# Total the money given out to find the administrators left overs
total_inheritence = total_inheritence - relatives_share * relatives
total_inheritence = total_inheritence - childrens_share * children
total_inheritence = total_inheritence - parents_share * parents

# Give the remainder to the administrator
administrators_share = administrators_share + total_inheritence

print("Relatives get $" , relatives_share , " each" , sep="")
print("Children get $" , childrens_share , " each" , sep="")
print("Parents get $" , parents_share , " each" , sep="")
print("Administrator gets $" , administrators_share , sep="")
#complete

#

#

#

#