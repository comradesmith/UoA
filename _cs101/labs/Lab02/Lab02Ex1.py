"""
Exercise 2.1
Author: Cam Smith, csmi928, 706899195
"""

def get_user_names():
	full_name = input("Enter your full name: ")
	full_name = full_name.strip()
	return full_name

user_name = get_user_names()
first_space = user_name.find(" ")
last_space = user_name.rfind(" ")
first_name = user_name[:first_space]
middle_name = user_name[first_space:last_space].strip()
last_name = user_name[last_space:].strip()
initials = first_name[0] + middle_name[0] + last_name[0]
print(initials.upper())
print(last_name[0].upper() + last_name[1:] + ", " + first_name[0].upper() + first_name[1:] + " " + middle_name[0].upper() + middle_name[1:])