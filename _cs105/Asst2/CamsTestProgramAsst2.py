import Asst2
from Node import Node
from Stack import Stack
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
    
def make_chain(n):
    count = 1
    current = Node(1)
    first = current
    while count < n:
        count += 1
        current.set_next(Node(count))
        current = current.get_next()
    return first

def list_to_chain(my_list):
    index = 1
    current = Node(my_list[0])
    first = current
    while index < len(my_list):
        current.set_next(Node(my_list[index]))
        current = current.get_next()
        index += 1
    return first

def print_chain(first_node):
    if first_node == None:
        print('None', end='')
    current = first_node
    while current != None:
        print(current.get_data(), end =' ')
        current = current.get_next()
    print()

def test_q3(n):
    a = make_chain(n)
    print('Initial chain:\t\t', end=' ')
    print_chain(a)
    Asst2.back_to_front_chain(a)
    print('Back to front chain:\t', end=' ')
    print_chain(a)


def test_question_one():
    print('\n\n----------------------\n Testing Question One\n----------------------')
    print('Expected:  2 3 4 + *', '\nActual:', end='\t   ')
    print(Asst2.generate_postfix('2 * ( 3 + 4 )'))
    print()
    print('Expected:  2 4 6 < ^ 3 3 / 1 * -', '\nActual:', end='\t   ')
    print(Asst2.generate_postfix('2 ^ ( 4 < 6 ) - 3 / 3 * 1'))
    print()
    print('Expected:  7 2 8 4 2 / + 1 > ^ * 15 4 / -', '\nActual:', end='\t   ')
    print(Asst2.generate_postfix('7 * 2 ^ ( 8 + 4 / 2 > 1 ) - 15 / 4'))
    print()
    print('Expected:  6 7 6 + >', '\nActual:', end='\t   ')
    print(Asst2.generate_postfix('6 > 7 + 6'))
    print()
    print('Expected:  6 7 - 6 +', '\nActual:', end='\t   ')
    print(Asst2.generate_postfix('6 - 7 + 6'))
    print()
    print('Expected:  2 4 6 < ^ 3 3 / 1 * -', '\nActual:', end='\t   ')
    print(Asst2.generate_postfix('2 ^ ( 4 < 6 ) - 3 / 3 * 1'))
    print()
    
    print('Error Handling\n--------------')
    print('Expected:  imbalanced brackets', '\nActual:', end='\t   ')
    print(Asst2.generate_postfix('( 2 ^ ( 4 < 6 ) - 3 / 3 * 1'))
    print()
    print('Expected:  invalid symbol', '\nActual:', end='\t   ')
    print(Asst2.generate_postfix('2 ^ ( 4 < 6.6 ) - 3 / 3 * 1'))
    print()
    print('Expected:  too many operators', '\nActual:', end='\t   ')
    print(Asst2.generate_postfix('2 ^ + ( 4 < 6 ) - 3 / 3 * 1'))
    print()
    print('Expected:  too many operators', '\nActual:', end='\t   ')
    print(Asst2.generate_postfix('2 ^ + ( 4 * < 6 ) - 3 / 3 * 1'))
    print()
    print('Expected:  too few operators', '\nActual:', end='\t   ')
    print(Asst2.generate_postfix('2 ^ ( 4 < 6 ) - 3 3 * 1'))
    print()
    print('Expected:  too few operators', '\nActual:', end='\t   ')
    print(Asst2.generate_postfix('2 ^ ( 4 < 6 9 ) - 3 3 * 1'))

def test_question_two():
    print('\n\n----------------------\n Testing Question Two\n----------------------')
    zero = Asst2.generate_prime_chain(0)
    one = Asst2.generate_prime_chain(1)
    two = Asst2.generate_prime_chain(2)
    three = Asst2.generate_prime_chain(3)
    ten = Asst2.generate_prime_chain(10)
    twenty = Asst2.generate_prime_chain(20)

    print('prime chain of', 0,':\t', end = ' ')
    print_chain(zero)
    print('prime chain of', 1,':\t', end = ' ')
    print_chain(one)
    print('prime chain of', 2,':\t', end = ' ')
    print_chain(two)
    print('prime chain of', 3,':\t', end = ' ')
    print_chain(three)
    print('prime chain of', 10,':\t', end = ' ')
    print_chain(ten)
    print('prime chain of', 20,':\t', end = ' ')
    print_chain(twenty)

    print('\n  In depth, chain length 3\n  ----------------------')
    print('  Expected:  2 3 5 None')
    print('  Actual:', end='    ')
    print(three.get_data(), end = ' ')
    print(three.get_next().get_data(), end = ' ')
    print(three.get_next().get_next().get_data(), end = ' ')
    print(three.get_next().get_next().get_next())

def test_question_three():
    print('\n\n------------------------\n Testing Question Three\n------------------------')
    test_q3(1)
    print()
    test_q3(2)
    print()
    test_q3(3)
    print()
    test_q3(6)
    print()
    test_q3(12)
    print()

    a = list_to_chain(['ann','bob','cam'])
    print('Initial chain:\t\t', end=' ')
    print_chain(a)
    Asst2.back_to_front_chain(a)
    print('Back to front chain:\t', end=' ')
    print_chain(a)
    print()

    b = list_to_chain(['ann','bob','cam','dan','eve','flo','gus'])
    print('Initial chain:\t\t', end=' ')
    print_chain(b)
    Asst2.back_to_front_chain(b)
    print('Back to front chain:\t', end=' ')
    print_chain(b)

def test_question_four():
    print('\n\n-----------------------\n Testing Question Four\n-----------------------')
    nested_list = [10, [5, None, None], [15, [11, None, None], [22, None, None]]]
    my_tree = Asst2.create_tree_from_nested_list(nested_list)
    print('Nested list:\n', my_tree)

    flat_list = [None, 10, 5, 15, None, None, 11, 22]
    my_tree = Asst2.create_tree_from_flat_list(flat_list)
    print('Flat list:\n', my_tree)

def test_question_five():
    print('\n\n-----------------------\n Testing Question Five\n-----------------------')
    root = BinaryTree(1)
    print('expecting 1:', end='\t')
    print(Asst2.sum_tree(root))

    root.set_left(BinaryTree(2))
    print('expecting 3:', end='\t')
    print(Asst2.sum_tree(root))

    root.set_right(BinaryTree(3))
    print('expecting 6:', end='\t')
    print(Asst2.sum_tree(root))

    root.get_left().set_left(BinaryTree(4))
    print('expecting 10:', end='\t')
    print(Asst2.sum_tree(root))

    root.get_right().set_left(BinaryTree(5))
    print('expecting 15:', end='\t')
    print(Asst2.sum_tree(root))

    root.get_right().set_right(BinaryTree(6))
    print('expecting 21:', end='\t')
    print(Asst2.sum_tree(root))

    root.get_right().get_right().set_left(BinaryTree(7))
    print('expecting 28:', end='\t')
    print(Asst2.sum_tree(root))

    root = BinaryTree(10)
    root.set_left(BinaryTree(5))
    root.set_right(BinaryTree(15))
    root.get_right().set_left(BinaryTree(11))
    root.get_right().set_right(BinaryTree(22))
    print('expecting 63:', end='\t')
    print(Asst2.sum_tree(root))

def test_question_six():
    print('\n\n----------------------\n Testing Question Six\n----------------------')
    flat_node_list = [None, 55, 24, 72, 8, 51, None, 78, None, None, 25]
    bst = Asst2.create_tree_from_flat_list(flat_node_list)
    pre_order_nodes = Asst2.pre_order(bst)
    in_order_nodes = Asst2.in_order(bst)
    post_order_nodes = Asst2.post_order(bst)
    
    print('Pre-order \nExpecting: [55, 24, 8, 51, 25, 72, 78]\nActual:   ', pre_order_nodes)
    print('In-order  \nExpecting: [8, 24, 25, 51, 55, 72, 78]\nActual:   ', in_order_nodes)
    print('Post-order\nExpecting: [8, 25, 51, 24, 78, 72, 55]\nActual:   ', post_order_nodes)

def test_question_seven():
    print('\n\n------------------------\n Testing Question Seven\n------------------------')
    flat_node_list_1 = [None, 12, 6, 25, 3, 13]
    bst1 = Asst2.create_tree_from_flat_list(flat_node_list_1)
    print(Asst2.is_binary_search_tree(bst1))

    print()
    
    flat_node_list_2 = [None, 12, 6, 25, 3, 10]
    bst2 = Asst2.create_tree_from_flat_list(flat_node_list_2)
    print(Asst2.is_binary_search_tree(bst2))

    bst_1 =  Asst2.create_tree_from_nested_list([44,[12,[1, None, None],[13, None, [33, None, None]]],[88,[70,[63,[30,None, None],None],None],None]])
    print()
    print(bst_1)
    print('Expected: False\nActual:  ',Asst2.is_binary_search_tree(bst_1))



    bt_1 =  Asst2.create_tree_from_nested_list([44,[12,[1, None, None],[13, None, [55, None, None]]],[88,[70,[63,[30,None, None],None],None],None]])
    print()
    print(bt_1)
    print('Expected: False\nActual:  ',Asst2.is_binary_search_tree(bt_1))


def test_question_eight():
    print('\n\n------------------------\n Testing Question Eight\n------------------------')
    flat_node_list = [None, 55, 24, 72, 8, 51, None, 78, None, None, 25]
    bst = Asst2.create_tree_from_flat_list(flat_node_list)
    mark = 0
    out_of = 3
    
    insert = Asst2.insert_position_in_bst(bst, 54)
    expected = 'right of 51'
    print('Insert (54) =', insert)
    if insert == expected:
        mark +=1
    
    insert = Asst2.insert_position_in_bst(bst, 49)
    expected = 'right of 25'
    print('Insert (49) =', insert)
    if insert == expected:
        mark +=1
    
    insert = Asst2.insert_position_in_bst(bst, 75)
    expected = 'left of 78'
    print('Insert (75) =', insert)
    if insert == expected:
        mark +=1

    if mark == out_of:
        return 11

def test_question_nine():
    print('\n\n-----------------------\n Testing Question Nine\n-----------------------')
    print('\nLinear probing\n--------------')
    mark = 0
    out_of = 4
    
    values = [26, 54, 94, 17, 31, 77, 44, 51]
    linear = Asst2.hash_with_probing(values, 13, 'linear')
    expected = [26, 51, 54, 94, 17, 31, 44, None, None, None, None, None, 77]
    print('Expected: ', expected)
    print('Actual:\t  ', linear)
    if linear == expected:
        mark +=1

    print('\nQuadratic probing\n-----------------')
    values = [26, 54, 94, 17, 31, 77, 43, 25]
    quadratic = Asst2.hash_with_probing(values, 13, 'quadratic')
    expected = [26, None, 54, 94, 17, 31, None, None, 43, None, None, 25, 77]
    print('Expected: ', expected)
    print('Actual:\t  ', quadratic)
    if quadratic == expected:
        mark +=1
    
    print()
    values = [7, 9, 10, 9]
    quadratic = Asst2.hash_with_probing(values, 6, 'quadratic')
    expected = [9, 7, None, 9, 10, None]
    print('Expected: ', expected)
    print('Actual:\t  ', quadratic)
    if quadratic == expected:
        mark +=1
    
    values = [96, 20, 33, 10, 9001]
    quadratic = Asst2.hash_with_probing(values, 7, 'quadratic')
    expected = [9001, None, 33, 10, None, 96, 20]
    print('Expected: ', expected)
    print('Actual:\t  ', quadratic)
    if quadratic == expected:
        mark +=1

    if mark == out_of:
        return 11

scores = []

welcome_message()
scores += [test_question_one()]         #12
scores += [test_question_two()]         #11
scores += [test_question_three()]       #11
scores += [test_question_four()]        #11
scores += [test_question_five()]        #11
scores += [test_question_six()]         #11
scores += [test_question_seven()]       #11
scores += [test_question_eight()]       #11
scores += [test_question_nine()]        #11
                                        #89
print()
print('\n-------------\n Final Score\n-------------')
print(sum([x for x in scores if x]))
    
