import Asst2
from Node import Node

from BinaryTree import BinaryTree

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
    
def test_question_one():
    print('\n====================\n Testing Question 1\n====================')
    infix1 = '2 * ( 3 + 4 )'
    expected1 = '2 3 4 + *'
    got1 = Asst2.generate_postfix(infix1)
    got2 = Asst2.generate_postfix('2 ^ ( 4 < 6 ) - 3 / 3 * 1')
    got3 = Asst2.generate_postfix('( 2 ^ ( 4 < 6 ) - 3 / 3 * 1')
    got4 = Asst2.generate_postfix('2 ^ ( 4 < 6.6 ) - 3 / 3 * 1')
    got5 = Asst2.generate_postfix('2 ^ + ( 4 < 6 ) - 3 / 3 * 1')
    got6 = Asst2.generate_postfix('2 ^ ( 4 < 6 ) - 3 3 * 1')
    got7 = Asst2.generate_postfix('7 * 2 ^ ( 8 + 4 / 2 > 1 ) - 15 / 4')
    got8 = Asst2.generate_postfix('6 > 7 + 6')
    got9 = Asst2.generate_postfix('6 - 7 + 6')
    got10 = Asst2.generate_postfix('2 ^ ( 4 < 6 ) - 3 / 3 * 1')

    
    print('Test 1\n', '  Expected =', expected1, '\n   Got      =', got1)
    print('Test 2\n', '  Expected =', '2 4 6 < ^ 3 3 / 1 * -', '\n   Got      =', got2)
    print('Test 3\n', '  Expected =', 'imbalanced brackets', '\n   Got      =', got3)
    print('Test 4\n', '  Expected =', 'invalid symbol', '\n   Got      =', got4)
    print('Test 5\n', '  Expected =', 'too many operators', '\n   Got      =', got5)
    print('Test 6\n', '  Expected =', 'too few operators', '\n   Got      =', got6)
    print('Test 7\n', '  Expected =', '7 2 8 4 2 / + 1 > ^ * 15 4 / -', '\n   Got      =', got7)
    print('Test 8\n', '  Expected =', '6 7 6 + >', '\n   Got      =', got8)
    print('Test 9\n', '  Expected =', '6 7 - 6 +', '\n   Got      =', got9)
    print('Test 10\n', '  Expected =', '2 4 6 < ^ 3 3 / 1 * -', '\n   Got      =', got10)

def test_question_two():
    print('\n====================\n Testing Question 2\n====================')

    my_primes = Asst2.generate_prime_chain(3)

    print('Test 1\n', '  Expected = 2 3 5 None', '\n   Got      =', end = ' ')
    print(my_primes.get_data(), end = ' ')
    print(my_primes.get_next().get_data(), end = ' ')
    print(my_primes.get_next().get_next().get_data(), end = ' ')
    print(my_primes.get_next().get_next().get_next())

    my_primes2 = Asst2.generate_prime_chain(6)

    print('Test 2\n', '  Expected = 2 3 5 7 11 13 None', '\n   Got      =', end = ' ')
    print(my_primes2.get_data(), end = ' ')
    print(my_primes2.get_next().get_data(), end = ' ')
    print(my_primes2.get_next().get_next().get_data(), end = ' ')
    print(my_primes2.get_next().get_next().get_next().get_data(), end = ' ')
    print(my_primes2.get_next().get_next().get_next().get_next().get_data(), end = ' ')
    print(my_primes2.get_next().get_next().get_next().get_next().get_next().get_data(), end = ' ')
    print(my_primes2.get_next().get_next().get_next().get_next().get_next().get_next())

def test_question_three():
    print('\n====================\n Testing Question 3\n====================')

    first_node = Node('ann')
    second_node = Node('bob')
    third_node = Node('cat')
    first_node.set_next(second_node)
    second_node.set_next(third_node)
    Asst2.back_to_front_chain(first_node)
    
    print('Test 1\n', '  Expected = ann cat bob None', '\n   Got      =', end = ' ')

    print(first_node.get_data(), end = ' ')
    print(first_node.get_next().get_data(), end = ' ')
    print(first_node.get_next().get_next().get_data(), end = ' ')
    print(first_node.get_next().get_next().get_next())

    first_node = Node(1)
    second_node = Node(2)
    third_node = Node(3)
    fourth_node = Node(4)
    fifth_node = Node(5)
    first_node.set_next(second_node)
    second_node.set_next(third_node)
    third_node.set_next(fourth_node)
    fourth_node.set_next(fifth_node)

    Asst2.back_to_front_chain(first_node)
    
    print('Test 2\n', '  Expected = 1 5 2 3 4 None', '\n   Got      =', end = ' ')

    print(first_node.get_data(), end = ' ')
    print(first_node.get_next().get_data(), end = ' ')
    print(first_node.get_next().get_next().get_data(), end = ' ')    
    print(first_node.get_next().get_next().get_next().get_data(), end = ' ')
    print(first_node.get_next().get_next().get_next().get_next().get_data(), end = ' ')
    print(first_node.get_next().get_next().get_next().get_next().get_next())

    first_node = Node(1)
    second_node = Node(2)

    first_node.set_next(second_node)

    Asst2.back_to_front_chain(first_node)
    
    print('Test 3\n', '  Expected = 1 2 None', '\n   Got      =', end = ' ')

    print(first_node.get_data(), end = ' ')
    print(first_node.get_next().get_data(), end = ' ')
    print(first_node.get_next().get_next())

def test_question_four():
    print('\n====================\n Testing Question 4\n====================')

    nested_list = [10, [5, None, None], [15, [11, None, None], [22, None, None]]]
    my_tree = Asst2.create_tree_from_nested_list(nested_list)
    print(my_tree) 

    print('Test 1\n', '  Expected = \n10\n(l)    5 \n(r)    15\n(l)        11 \n(r)        22', '\n   Got      =\n', my_tree)

def test_question_five():
    print('\n====================\n Testing Question 5\n====================')

    flat_list = [None, 10, 5, 15, None, None, 11, 22] 
    #my_tree = create_tree_from_flat_list(flat_list) 
    my_tree = [None, 10, 5, 15, None, None, 11, 22]
    a = BinaryTree(10)
    a.set_left(BinaryTree(5))
    a.set_right(BinaryTree(6))

    print(Asst2.sum_tree(a))
    #print('Sum of tree values =', Asst2.sum_tree(my_tree))

    #print('Test 1\n', '  Expected = 63', '\n   Got      =\n', Asst2.sum_tree(my_tree))

def test_question_six():
    print('\n====================\n Testing Question 6\n====================')

def test_question_seven():
    print('\n====================\n Testing Question 7\n====================')

def test_question_eight():
    print('\n====================\n Testing Question 8\n====================')

def test_question_nine():
    print('\n====================\n Testing Question 9\n====================')

    values = [26, 54, 94, 17, 31, 77, 44, 51] 
    linear = Asst2.hash_with_probing(values, 13, 'linear') 

    values = [26, 54, 94, 17, 31, 77, 43, 25] 
    quadratic = Asst2.hash_with_probing(values, 13, 'quadratic') 

    values = [96, 20, 33, 10, 9001]
    quadratic2 = Asst2.hash_with_probing(values, 7, 'quadratic')

    print('Test 1\n', '  Expected = [26, 51, 54, 94, 17, 31, 44, None, None, None, None, None, 77] ', '\n   Got      =', linear)
    print('Test 2\n', '  Expected = [26, None, 54, 94, 17, 31, None, None, 43, None, None, 25, 77] ', '\n   Got      =', quadratic)
    print('Test 3\n', '\n   Got      =', quadratic2)


welcome_message()
test_question_one()
test_question_two()
test_question_three()
#test_question_four()
test_question_five()
#test_question_six()
#test_question_seven()
#test_question_eight()
test_question_nine()











    
