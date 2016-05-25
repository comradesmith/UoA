"""
Exercise 2.2
Author: Cam Smith, csmi928, 706899195
"""
import random

first_number = random.randrange(75, 201)
last_number = random.randrange(75, 201)
print("Smallest random number generated was" , min(first_number, last_number))
print("Largest random number generated was" , max(first_number, last_number))
