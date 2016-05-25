"""
Lab 3 Ex 5
Author: Cameron Smith
upi: csmi928
"""

def main():
	items = get_number_of_items()
	boxes = calculate_boxes_needed(items)
	cost = calculate_cost(boxes)
	print_boxes_needed_and_cost(items, boxes, cost)

def get_number_of_items():
	number_of_items = int(input("Enter number of items: "))
	return number_of_items

def calculate_boxes_needed(items):
	boxes = items // 10
	items_left_over = items % 10
	if items_left_over > 0:
		boxes += 1
	return boxes

def calculate_cost(boxes):
	return 8 * min(boxes, 6) + 5 * max(boxes - 6, 0)

def print_boxes_needed_and_cost(items, boxes_needed, cost):
	print("Boxes needed: " + str(boxes_needed))
	print("Cost: $" + str(cost))
	
main()



	
