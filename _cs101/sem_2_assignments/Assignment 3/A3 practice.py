def count_character(filename):
	input_file = open(filename)
	input_data = input_file.read()
	print(input_data)
	
count_character('text.txt')