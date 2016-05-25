""" Compsci 101 S2; Assignment 1 Question 1
	Calculates the difference between two times
	Author: Cam Smith, csmi928, 70689919
"""

def main():
	start = "06:55:55"
	end = "07:04:57"
	display_result(start, end)

def timestring_to_seconds(timestring):
	hours = int(timestring[0:2]) * 3600
	minutes = int(timestring[3:5]) * 60
	seconds = int(timestring[6:8])
	total_seconds = hours + minutes + seconds
	return total_seconds

def seconds_to_string(seconds):
	seconds_minus_hours = seconds % 3600
	seconds_remaining = "0" + str(seconds_minus_hours % 60)
	hours = "0" + str(seconds // 3600)
	minutes = "0" + str(seconds_minus_hours // 60)
	timestring = hours[-2:] + ":" + minutes[-2:] + ":" + seconds_remaining[-2:]
	return timestring

def get_difference(start_time, end_time):
	start_seconds = timestring_to_seconds(start_time)
	end_seconds = timestring_to_seconds(end_time)
	difference_seconds = end_seconds - start_seconds
	difference_string = seconds_to_string(difference_seconds)
	return difference_string

def display_result(start_time, end_time):
	difference = get_difference(start_time, end_time)
	line_1 = "Start time: " + start_time + "  End time: " + end_time
	line_2 = "Total time elapsed: " + str(difference)
	print(line_1)
	print(line_2)

main()