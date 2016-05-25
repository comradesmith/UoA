"""
Author: csmi928, Cameron Smith, 706899195
Date-written: August 2015
Lab 5 Exercise 5.6
Produces a list of selling prices by applying a markup to a list of cost prices.
"""

def main():
	cost_price_list = [1.47, 2.35, 12.78, 3.56, 11.19, 9.26, 56.37]
	selling_price_list = apply_markup(cost_price_list, 20)
	print("Cost prices:    ", cost_price_list)
	print("Selling prices: ", selling_price_list)
	
	
def apply_markup(price_list, markup):
	marked_up_prices = []
	for price in price_list:
		price = price * (1 + markup / 100)
		price = round(price, 2)
		marked_up_prices = marked_up_prices + [price]
	return marked_up_prices
	
main()