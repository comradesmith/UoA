from tkinter import * 
 
def draw_pattern_in_canvas(a_canvas): 
	grid_size = 50
	is_circle = True
	rows = 7
	columns = 10
	x_pos = 0
	y_pos = 0
	
	for row in range(rows):
		x_pos = 0
		for column in range(columns):
			if is_circle:
				a_canvas.create_oval(x_pos, y_pos, x_pos + grid_size, y_pos + grid_size, fill="red", width=2)
			elif not is_circle:
				a_canvas.create_rectangle(x_pos, y_pos, x_pos + grid_size, y_pos + grid_size, fill="green", width=2)
				a_canvas.create_line(x_pos + (grid_size/2), y_pos , x_pos+ (grid_size/2), y_pos + grid_size)
				a_canvas.create_line(x_pos, y_pos + (grid_size/2), x_pos + grid_size, y_pos + (grid_size/2))
			x_pos +=grid_size
			is_circle = not is_circle
		is_circle = not is_circle
		y_pos += grid_size	
	
def draw_grid(a_canvas):
	for row in range(50, 350, 50):
		a_canvas.create_line(-1, row, 501, row, fill = "lightblue")
	for column in range(50, 500, 50):
		a_canvas.create_line(column, -1, column, 351, fill = "lightblue")
		
def main(): 
	window = Tk()  
	window.title("Red and Green Pattern")  
	window.config(background = 'white')   
	window.geometry("500x350+10+20") 

	a_canvas = Canvas(window) 
	a_canvas.config(background = "white")   
	a_canvas.pack(fill = BOTH, expand = True) #Canvas fills the whole top level window 
	draw_grid(a_canvas)
	draw_pattern_in_canvas(a_canvas) 
	window.mainloop()   
 
main()