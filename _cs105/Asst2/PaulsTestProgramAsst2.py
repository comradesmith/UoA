import Asst2
from Node import Node

def welcome_message():
    print('Welcome to COMPSCI 105 Assignment Two, Summer 2016.\n')
    print('You should write all of your test code in this file,')
    print('TestProgramAsst2.py.  The source file you actually')
    print('submit, Asst2.py, should only contain function')
    print('definitions (as described in the project document).')
    print('There should not be any top level program statements')
    print('in Asst2.py.\n')
    print('In this file you will see one suggested way for ')
    print('organising your test code - refer to the function')
    print('called test_question_one().  You could define similar')
    print('test functions for the other questions.\n')
    print('You should test your functions thoroughly.')

def display_message(result):
	if result == True:
		print("===================")
		print("    TEST PASSED    ")
		print("===================")
		print()
	if result == False:
		print("===================")
		print("    TEST FAILED    ")
		print("===================")
		print()
	
def manual_test():
	hold = input("Press any button to commence manual testing...")
	clear = "\n" * 100
	print(clear)
	print("----------------------")
	print("This is a manual test.")
	print("----------------------")
	print("\nSelect the number corresponding to the functions to test.\n")
	
	#Menu
	print("1. generate_postfix(infix): function")
	print("2. generate_prime_chain(n): function")
	print("3. back_to_front_chain(first_node): function")
	print("0. Exit")
	print("\n" * 5)
	
	print()
	user_input = input("Select function to test: ")
	
	#Selection1 def generate_postfix(infix):
	if user_input == "1":
		print()
		print("******************************************")
		print("def generate_postfix(infix): function test")
		print("******************************************")
		print()
		print("Select type of test.\n")
		print("1.Test input vs. expected.")
		print("2.test manual infix to postfix conversion.")
		print()
		user_selection = input("Select type of test: ")
		if user_selection == "1":
			print()
			print("=================================")
			infix_input = input("Input an infix expression to test: ")
			print("\nYour input =", infix_input)
			print()
			expected_output = input("Input an expected output expression: ")
			print()
			result = Asst2.generate_postfix(infix_input)
			print("Your input =", infix_input)
			print()
			print("Expected   =", "[" + expected_output + "]")
			print("Got        =", "[" + result + "]")
			display_message(expected_output == result)
			manual_test()
		if user_selection == "2":
			print()
			print("=================================")
			infix_input = input("Input an infix expression to convert: ")
			print()
			result = Asst2.generate_postfix(infix_input)
			print("Your input =", "[" + infix_input + "]")
			print("Got        =", "[" + result + "]")
			print()
			manual_test()
	
	#Selection2 def generate_prime_chain(n):
	if user_input == "2":
		print()
		print("******************************************")
		print("def generate_prime_chain(n): function test")
		print("******************************************")
		print()
		user_input_n = input("Enter n prime number: ")
		print()
		print("Your n prime number input =", user_input_n)
		prime_number_list = []
		number = 2
		while len(prime_number_list) < int(user_input_n):
			for i in range(2, number):
				if (number % i) == 0 and number != 2:
					break
			else:
				prime_number_list += [number]
			number += 1
		expected_string = ""
		for prime in prime_number_list:
			expected_string += str(prime) + " "
		expected_string += "None"
		print()
		print("Expected printed chain of nodes =", expected_string)
		n = int(user_input_n)
		my_primes = Asst2.generate_prime_chain(n)
		current = my_primes	
		string1 = ""
		string2 = ""
		count_test1 = 0
		while current != None:
			string1 += str(current) + " "	
			current = current.get_next()	
			count_test1 += 1 
		string1 += str(current)
		count_test2 = 0
		current = my_primes
		try:
			while True:
				string2 += str(current) + " "
				current = current.get_next()
				count_test2 += 1
		except:
			None
		string2 = string2.strip()	
		print("Hidden Test 1 =", string1)
		print("Hideen Test 2 =", string2)
		print()
		print("Expected number of nodes =", n)
		print("Hidden Test 1 =", count_test1)
		print("Hideen Test 2 =", count_test2)
		print()		
		if string1 == string2 and count_test1 == count_test2:
			display_message(True)
		else:
			display_message(False)
		manual_test()
		
	#Selection3 def back_to_front_chain(first_node):
	if user_input == "3":
		print("**************************************************")
		print("def back_to_front_chain(first_node): function test")
		print("**************************************************")
		print()
		user_selection = None
		first_time = True
		first_node = None
		current_chain = ""
		current = None
		node_count = 0
		while user_selection != "2":
			print()
			print("ACTION")
			print("=============================")
			print("Create a node.     [select 1:] ")
			print("Call the function. [select 2:] ")
			print("Exit to menu.      [select 0:] ")
			print("=============================")
			print()
			user_selection = input("Selection: ")
			print()
			
			if user_selection == "0":
				manual_test()
				
			if user_selection == "1":
				if first_time == True:
					print()
					user_node = input("String object to store: ")
					if len(user_node) == 0:
						raise ValueError("no input given")
					first_node = Node(user_node)
					current = first_node
					first_time = False
					current_chain += str(current) + " "
					node_count += 1
				else:
					user_node = input("String object to store: ")
					if len(user_node) == 0:
						raise ValueError("no input given")
					new_node = Node(user_node)
					prev_node = current
					current.set_next(new_node)
					current = new_node
					current_chain += str(prev_node.get_next()) + " "
					node_count += 1
																			
			if user_selection == "2":
				break
				
			
			print()
			print("----------------------------")
			print("Current chain: ", current_chain)
			print("Number of nodes stored: ", node_count)
			print("----------------------------")
		
		#Call to the back_to_front_chain(first_node): function
		before_convert = ""
		current = first_node
		before_chain_length = 0
		while current != None:
			before_convert += str(current) + " "
			current = current.get_next()
			before_chain_length += 1
		before_convert += str(current)
		result = ""
		current = first_node
		if before_chain_length < 3:
			Asst2.back_to_front_chain(first_node)
			while current != None:
				result += str(current) + " "
				current = current.get_next()
			result += str(current)
			result = result.strip()
			print("Nodes less than 3 expect no change.")
			print()
			print("Expected:      ", before_convert)
			print("After convert: ", result)
			display_message(before_convert == result)
			raise SystemExit
		print()
		print("Original chain =", "[" + before_convert + "]")
		print("Number of nodes in the chain: ", before_chain_length)
		print()
		Asst2.back_to_front_chain(first_node)
		after_convert = ""
		current = first_node
		after_chain_length = 0
		while current != None:
			after_convert += str(current) + " "
			current = current.get_next()
			after_chain_length += 1
		after_convert += str(current)
		expected_chain = before_convert.split()
		last = expected_chain.pop(len(expected_chain ) - 2)
		expected_chain.insert(1, last)
		expected = ""
		for item in expected_chain:
			expected += item + " "
		expected = expected.strip()
		print("Expected chain:", "[" + expected + "]")
		print()
		print("After convert chain =", "[" + after_convert + "]")
		print("Number of nodes in the chain: ", after_chain_length)
		print()

			

		display_message( expected == after_convert and before_chain_length == after_chain_length)
		
		
		
	
		
		

		
	
	
		
def test_question_one():
    print('\nTesting Question One\n--------------------')
	
	#Test1
    infix1 = '2 * ( 3 + 4 )'
    expected1 = '2 3 4 + *'
    got1 = Asst2.generate_postfix(infix1)		    
    print('Test 1\n','  Infix    =', infix1, '\n   Expected =', expected1, '\n   Got      =', got1)
    display_message(expected1 == got1)	
    print()
	
	#Test2
    infix2 = '7 * 2 ^ ( 8 + 4 / 2 > 1 ) - 15 / 4'
    expected2 = '7 2 8 4 2 / + 1 > ^ * 15 4 / -'
    got2 = Asst2.generate_postfix(infix2)		    
    print('Test 2\n','  Infix    =', infix2, '\n   Expected =', expected2, '\n   Got      =', got2)
    display_message(expected2 == got2)
    print()
	
	#Test3
    infix3 = '6 > 7 + 6'
    expected3 = '6 7 6 + >'
    got3 = Asst2.generate_postfix(infix3)		    
    print('Test 3\n','  Infix    =', infix3, '\n   Expected =', expected3, '\n   Got      =', got3)
    display_message(expected3 == got3)
    print()
	
	#Test4
    infix4 = '6 - 7 + 6'
    expected4 = '6 7 - 6 +'
    got4 = Asst2.generate_postfix(infix4)		    
    print('Test 4\n','  Infix    =', infix4, '\n   Expected =', expected4, '\n   Got      =', got4)
    display_message(expected4 == got4)
	
    #Test5
    infix5 = '2 ^ ( 4 < 6 ) - 3 / 3 * 1'
    expected5 = '2 4 6 < ^ 3 3 / 1 * -'
    got5 = Asst2.generate_postfix(infix5)		    
    print('Test 5\n','  Infix    =', infix5, '\n   Expected =', expected5, '\n   Got      =', got5)
    display_message(expected5 == got5)
	
    #Test6
    infix6 = '( 2 ^ ( 4 < 6 ) - 3 / 3 * 1'
    expected6 = 'imbalanced brackets'
    got6 = Asst2.generate_postfix(infix6)		    
    print('Test 6\n','  Infix    =', infix6, '\n   Expected =', expected6, '\n   Got      =', got6)
    display_message(expected6 == got6)
	
	#Test7
    infix7 = '2 ^ ( 4 < 6.6 ) - 3 / 3 * 1'
    expected7 = 'invalid symbol'
    got7 = Asst2.generate_postfix(infix7)		    
    print('Test 7\n','  Infix    =', infix7, '\n   Expected =', expected7, '\n   Got      =', got7)
    display_message(expected7 == got7)
	
	#Test8
    infix8 = '2 ^ + ( 4 < 6 ) - 3 / 3 * 1'
    expected8 = 'too many operators'
    got8 = Asst2.generate_postfix(infix8)		    
    print('Test 8\n','  Infix    =', infix8, '\n   Expected =', expected8, '\n   Got      =', got8)
    display_message(expected8 == got8)

    #Test9
    infix9 = '2 ^ ( 4 < 6 ) - 3 3 * 1'
    expected9 = 'too few operators'
    got9 = Asst2.generate_postfix(infix9)		    
    print('Test 9\n','  Infix    =', infix9, '\n   Expected =', expected9, '\n   Got      =', got9)
    display_message(expected9 == got9)


	
def test_question_two():
    print('\nTesting Question Two\n--------------------')
	
	#Test1
    print("Test 1\n")
    n = 3
    my_primes = Asst2.generate_prime_chain(n)
    current = my_primes	
    string1 = ""
    string2 = ""
    count_test1 = 0
    expected_string = "2 3 5 None"
    while current != None:
        string1 += str(current) + " "	
        current = current.get_next()	
        count_test1 += 1 
    string1 += str(current)
    count_test2 = 0
    current = my_primes
    try:
        while True:
            string2 += str(current) + " "
            current = current.get_next()
            count_test2 += 1
    except:
        None
    string2 = string2.strip()	
    print("Expected number of nodes =", n)
    print("Hidden Test 1 =", count_test1)
    print("Hideen Test 2 =", count_test2)
    print()
    print("Expected printed chain =", expected_string)
    print("Hidden Test 1 =", string1)
    print("Hideen Test 2 =", string2)
    if string1 == string2 and count_test1 == count_test2:
        display_message(True)
    else:
        display_message(False)

	#Test2
    print("Test 2\n")
    n = 5
    my_primes = Asst2.generate_prime_chain(n)
    current = my_primes	
    string1 = ""
    string2 = ""
    count_test1 = 0
    expected_string = "2 3 5 7 11 None"
    while current != None:
        string1 += str(current) + " "	
        current = current.get_next()	
        count_test1 += 1 
    string1 += str(current)
    count_test2 = 0
    current = my_primes
    try:
        while True:
            string2 += str(current) + " "
            current = current.get_next()
            count_test2 += 1
    except:
        None
    string2 = string2.strip()	
    print("Expected number of nodes =", n)
    print("Hidden Test 1 =", count_test1)
    print("Hideen Test 2 =", count_test2)
    print()
    print("Expected printed chain =", expected_string)
    print("Hidden Test 1 =", string1)
    print("Hideen Test 2 =", string2)
    if string1 == string2 and count_test1 == count_test2:
        display_message(True)
    else:
        display_message(False)	

		
	#Test3
    print("Test 3\n")
    n = 10
    my_primes = Asst2.generate_prime_chain(n)
    current = my_primes	
    string1 = ""
    string2 = ""
    count_test1 = 0
    expected_string = "2 3 5 7 11 13 17 19 23 None"
    while current != None:
        string1 += str(current) + " "	
        current = current.get_next()	
        count_test1 += 1 
    string1 += str(current)
    count_test2 = 0
    current = my_primes
    try:
        while True:
            string2 += str(current) + " "
            current = current.get_next()
            count_test2 += 1
    except:
        None
    string2 = string2.strip()	
    print("Expected number of nodes =", n)
    print("Hidden Test 1 =", count_test1)
    print("Hideen Test 2 =", count_test2)
    print()
    print("Expected printed chain =", expected_string)
    print("Hidden Test 1 =", string1)
    print("Hideen Test 2 =", string2)
    if string1 == string2 and count_test1 == count_test2:
        display_message(True)
    else:
        display_message(False)


def test_question_three():
	print('\nTesting Question Three\n--------------------')
	
	#Test1
	print("Test 1\n")
	first_node = Node("ann")
	second_node = Node("bob")
	third_node = Node("cat")
	first_node.set_next(second_node)
	second_node.set_next(third_node)
	expected_chain = "ann cat bob None"
	original_chain = ""
	original_chain += str(first_node) + " "
	original_chain += str(first_node.get_next()) + " "
	original_chain += str(first_node.get_next().get_next()) + " "
	original_chain += str(first_node.get_next().get_next().get_next())	
	Asst2.back_to_front_chain(first_node)
	new_chain = ""
	new_chain += str(first_node) + " "
	new_chain += str(first_node.get_next()) + " "
	new_chain += str(first_node.get_next().get_next()) + " "
	new_chain += str(first_node.get_next().get_next().get_next())
	print("Original chain = ", original_chain)
	print("Expected chain = ", expected_chain)
	print("New chain      = ", new_chain)
	display_message(expected_chain == new_chain)
	print()
	
def test_question_nine():
	print('\nTesting Question Four\n--------------------')
	print("4. hash_with_probing(): function")
	print()
	
	#Test1
	print("Test 1\n")
	values = [26, 54, 94, 17, 31, 77, 44, 51]
	linear = Asst2.hash_with_probing(values, 13, 'linear')
	expected = [26, 51, 54, 94, 17, 31, 44, None, None, None, None, None, 77]
	print("Expected =", expected)
	print("Got      =", linear)
	display_message(expected == linear)
	
	

print("<<This test code is written by Paul Tanchareon.>>")		
#welcome_message()
test_question_one()
test_question_two()
test_question_three()
test_question_nine()
manual_test()


    
