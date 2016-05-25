"""
Lab 01 Ex 1.3
Author: Cam Smith
Date Written: July 2015

"""

import math

# Part (a)
total_pounds = 92
stones = total_pounds // 14
pounds = 92 % 14
print("There are", stones, "stones and", pounds, "pounds in", total_pounds, "pounds.")
print()
#Part (b)
height = 30
radius = 10
height_part = 2 * math.pi * height * radius
radius_part = 2 * math.pi * radius ** 2
surface_area = height_part + radius_part
print("Surface area of cylinder is", round(surface_area), "square cms.")
print()

#Part (c)
weight = 64.75
height = 1.63
bmi_result = weight / height ** 2
print("Peter's bmi is ", round(bmi_result, 1), ".", sep="")
print()
#Part (d)
years = 20
rate = 0.04
initial_investment = 3000
final_value = initial_investment * (1 + rate) ** years
print("Total value after ", years, " years would be $", round(final_value, 2), ".", sep="")
print()