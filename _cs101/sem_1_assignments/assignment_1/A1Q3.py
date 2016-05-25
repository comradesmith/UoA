"""	COMPSCI 101 S2: ASSIGNMENT 1, QUESTION 3
	Author: Cam Smith, csmi928, 706899195
"""

fahrenheit = 23
speed = 5

part_1 = 0.6215 * fahrenheit
part_2 = 35.75 * speed ** 0.16
part_3 = 0.4275 * fahrenheit * speed ** 0.16

temperature_wind_chill = 35.74 + part_1 - part_2 + part_3

print("The temperature in Fahrenheit is", fahrenheit)
print("The wind speed is", speed, "mph")
print("The wind chill index is", temperature_wind_chill)