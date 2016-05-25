def count_lines(filename):
	input_file = open(filename, "r")
	file_contents = input_file.read()
	input_file.close()
	file_contents = file_contents.split("\n")
	return len(file_contents)
	
def main():
	print(count_lines("text.txt"))
	
main()