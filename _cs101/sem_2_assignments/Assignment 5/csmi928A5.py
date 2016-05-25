"""
	Cam Smith, csmi928, 706899195
	Compsci101 S2, A5: Draws a small tesselation graphic based on a text file
"""

from tkinter import *

# ------Draws one of the five different tiles.------
def draw_tile(a_canvas, tile_type, left, top, size):
	colours = ["yellow", "green", "blue", "deep sky blue", "purple", "red", "orange", "cyan"]
	# modify the starting position for the 3rd and 4th tile types
	if tile_type == 3:
		left = left - 2 * size
	elif tile_type == 4:
		left = left - 1 * size
	# define rows and columns to reduce repeated code
	
	a_col = left
	b_col = left + size
	c_col = left + 2 * size
	d_col = left + 3 * size
	
	a_row = top
	b_row = top + size
	c_row = top + 2 * size
	d_row = top + 3 * size
	
	
	if tile_type == 1:
		a_canvas.create_rectangle(a_col, a_row, b_col, c_row, fill= colours[tile_type], width=2, outline="grey")
		a_canvas.create_rectangle(b_col, b_row, c_col, d_row, fill= colours[tile_type], width=2, outline="grey")
		a_canvas.create_rectangle(c_col, c_row, d_col, d_row, fill= colours[tile_type], width=2, outline="grey")
		a_canvas.create_line(b_col, b_row + 1, b_col, c_row - 1, width=2, fill=colours[tile_type])
		a_canvas.create_line(c_col, c_row + 1, c_col, d_row - 1, width=2, fill=colours[tile_type])
	elif tile_type == 2:
		a_canvas.create_rectangle(a_col, a_row, c_col, b_row, fill= colours[tile_type], width=2, outline="grey")
		a_canvas.create_rectangle(b_col, b_row, d_col, c_row, fill= colours[tile_type], width=2, outline="grey")
		a_canvas.create_rectangle(c_col, c_row, d_col, d_row, fill= colours[tile_type], width=2, outline="grey")
		a_canvas.create_line(b_col + 1, b_row, c_col - 1, b_row, width=2, fill=colours[tile_type])
		a_canvas.create_line(c_col + 1, c_row, d_col - 1, c_row, width=2, fill=colours[tile_type])
	elif tile_type == 3:
		a_canvas.create_rectangle(c_col, a_row, d_col, b_row, fill= colours[tile_type], width=2, outline="grey")
		a_canvas.create_rectangle(b_col, b_row, d_col, c_row, fill= colours[tile_type], width=2, outline="grey")
		a_canvas.create_rectangle(a_col, c_row, c_col, d_row, fill= colours[tile_type], width=2, outline="grey")
		a_canvas.create_line(c_col + 1, b_row, d_col - 1, b_row, width=2, fill=colours[tile_type])
		a_canvas.create_line(b_col + 1, c_row, c_col - 1, c_row, width=2, fill=colours[tile_type])
	elif tile_type == 4:
		a_canvas.create_rectangle(b_col, a_row, d_col, b_row, fill= colours[tile_type], width=2, outline="grey")
		a_canvas.create_rectangle(a_col, b_row, c_col, c_row, fill= colours[tile_type], width=2, outline="grey")
		a_canvas.create_rectangle(a_col, c_row, b_col, d_row, fill= colours[tile_type], width=2, outline="grey")
		a_canvas.create_line(a_col + 1, c_row, b_col - 1, c_row, width=2, fill=colours[tile_type])
		a_canvas.create_line(b_col + 1, b_row, c_col - 1, b_row, width=2, fill=colours[tile_type])
	elif tile_type == 5:
		a_canvas.create_rectangle(a_col, a_row , b_col, b_row, fill= colours[tile_type], width=2, outline="grey")

# ------Process each symbol from a single line (string). ------
def process_single_line(a_canvas, line_of_pattern, left, top, size):
	for tile in line_of_pattern:
		if tile != "x":
			draw_tile(a_canvas, int(tile), left, top, size)
		left += size

# ------Organise the processing of the pattern. ------
def process_pattern(a_canvas, size):
	left = size
	top = size
	list_of_lines = get_list_of_pattern_lines("TileMap.txt")
	for line_string in list_of_lines:
		process_single_line(a_canvas, line_string, left, top, size)
		top += size

# ------Get the list of lines (strings) from the file. ------
def get_list_of_pattern_lines(filename):
	file_to_read = open(filename, "r")
	file_info = file_to_read.read()
	lines_list = file_info.split("\n")
	file_to_read.close()
	return lines_list

# ------Draws the five tiles on the right side of the canvas. ------

def draw_five_tiles(a_canvas, left, top, size):
	size = size * 3 // 4
	large_rect = (left, top, left + size * 11, top + size * 12)
	a_canvas.create_rectangle(large_rect, fill="Blue4", outline="SlateBlue1", width = 2)
	left_size_multiply = [0, 1, 6, 3, 7, 1]
	down_size_multiply = [0, 1, 1, 6, 6, 10]
	
	for tile_type in range(1, 6):
		left_value = left + size * left_size_multiply[tile_type]
		top_value = top + size * down_size_multiply[tile_type]
		draw_tile(a_canvas, tile_type, left_value, top_value, size)

# ------Draws the blue background grid lines of the given size. ------
def draw_grid(a_canvas, size, right_hand_side, bottom):
	for row in range(size, bottom, size):
		a_canvas.create_line(-1, row, right_hand_side + 1, row, fill="SlateBlue1")
	for col in range(size, right_hand_side, size):
		a_canvas.create_line(col, -1, col, bottom + 1, fill="SlateBlue1")

# ------main function. ------
def main():
	size = 20
	canvas_width = 700
	canvas_height = 340
	root = Tk()
	root.title("A5 - csmi928")
	geometry_string = str(canvas_width)+"x"+str(canvas_height)+"+10+20"
	root.geometry(geometry_string)
	a_canvas = Canvas(root)
	
	a_canvas.config(background="SlateBlue1") #Uncomment when you have finished
	a_canvas.pack(fill=BOTH, expand = True) #Canvas fills the whole window
	#Draw the light blue background grid lines
	draw_grid(a_canvas, size, canvas_width, canvas_height)
	
	process_pattern(a_canvas, size)
	draw_five_tiles(a_canvas, canvas_width - size * 3 // 4 * 12, size, size)
	
	root.mainloop()
	
main()