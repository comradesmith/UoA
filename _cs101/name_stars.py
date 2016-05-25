""" COMPSCI 101; LECTURE 4 CHALLENGE
	Given a string, print that with a header and footer of stars
	and with an even gap of spaces on each side
	Author: Cam Smith
"""

name = "Wabalaba Doop Doop"
spacing = 3

print(("*" * (len(name) + 2 * spacing)))
print(" " * spacing, name, " " * spacing, sep="")
print(("*" * (len(name) + 2 * spacing)))

name = "Wabalaba Doop Doop Bop Shoe Wee Dop"
spacing = 3

print(("*" * (len(name) + 2 * spacing)))
print(" " * spacing, name, " " * spacing, sep="")
print(("*" * (len(name) + 2 * spacing)))