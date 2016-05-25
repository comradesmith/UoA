""" Lecture 7 excercise
	Author: Cam Smith
"""
from random import randrange

def function1(n1, n2, n3):
	result = n1 + n2 + n3 - min(n1, n2, n3)
	return result
	
def function2(w1, w2):
	w1_length = len(w1)
	w2_length = len(w2)
	return min(w1_length, w2_length)

def function3(word):
	result = word[-1] + word[0]
	return result.upper()
	
def required_boxes(items, box_size):
	first_division = items // box_size
	remainder = items % box_size
	boxes = first_division + min(remainder, 1)
	return boxes
	
def get_first_name():
	return input("Enter name: ")
	
def remove_random_letter(name):
	position = randrange(0, len(name))
	result = name[:position] + "_" + name[position + 1:]
	return result
	
print("1.",function1(1, 2, 3))
print("2.",function1(11, 12, 3))
print("3.",function1(6, 2, 5))
print()

print("1.",function2("Flibbertigibbet", "Rigmarole"))
print("2.",function2("Mollycoddle", "Malarky"))
print("3.",function2("Skullduggery", "Canoodle"))
print()

print("1.",function3("Crudivore"))
print("2.",function3("Ornery"))
print("3.",function3("Brouhaha"))
print()

print("1.","Boxes:", required_boxes(30, 16))
print("2.","Boxes:", required_boxes(30, 3))
print("3.","Boxes:", required_boxes(30, 10))
print()

first_name = get_first_name()
print("1.", remove_random_letter(first_name))
print("2.", remove_random_letter(first_name))
print("3.", remove_random_letter(first_name))
print()