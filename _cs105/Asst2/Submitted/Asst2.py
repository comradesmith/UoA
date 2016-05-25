"""
	Cam Smith, csmi928, 706899195
	Compsci105 SS, Asst2
	2016-02-09
"""

from Node import Node
from Stack import Stack
from BinaryTree import BinaryTree

"""        Q1        """
def is_balanced(string):
    stack = Stack()
    for character in string:
        if character == '(':
            stack.push(character)
        elif character == ')':
            if stack.is_empty():
                return False
            stack.pop()

    if stack.is_empty():
        return True
    return False

def valid_symbols(infix):
    infix = infix.split(' ')
    operators = '><-+/*^()'
    valid_bools = [x.isdigit() or x in operators for x in infix]
    return not False in valid_bools

def count_operators(infix):
    infix = infix.split(' ')
    valid_operators = '><-+/*^'
    operators_count = 0
    for i in infix:
        if i in valid_operators:
            operators_count += 1
    return operators_count

def count_operands(infix):
    infix_without_brackets = [x for x in infix.split(' ') if x not in '()']
    operands_count = len(infix_without_brackets) - count_operators(infix)
    return operands_count

def generate_postfix(infix):
    if not isinstance(infix, str):
        return 'invalid symbol'
    elif not valid_symbols(infix):
        return 'invalid symbol'
    elif not is_balanced(infix):
        return 'imbalanced brackets'
    elif count_operators(infix) >= count_operands(infix):
        return 'too many operators'
    elif count_operators(infix) < count_operands(infix) - 1:
        return 'too few operators'

    operators = {'<':1,'>':1,'+':2,'-':2,'*':3,'/':3,'^':4,'(':0,')':0}    
    result = ''
    stack = Stack()
    infix = infix.split(' ')

    for i in infix:
        if i.isdigit():
            result += i + ' '
        elif i == '(':
            stack.push(i)
        elif i in operators and not i in '()':
            if stack.is_empty():
                stack.push(i)
            else:
                while not stack.is_empty() and operators[stack.peek()] >= operators[i]:
                    result += stack.pop() + ' '
                stack.push(i)
        elif i == ')':
            while stack.peek() != '(':
                result += stack.pop() + ' '
            stack.pop()
    while not stack.is_empty():
        result += stack.pop() + ' '
                
    return result[:-1]

"""        Q2        """
def is_prime(n):
    if n < 2:
        return False

    if n == 4:
        return False

    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

def generate_prime_chain(n):
    if n == 0 or n == None:
        return None
    count = 1
    candidate = 3
    head = Node(2)
    current = head

    while count < n:
        if is_prime(candidate):
            prime_node = Node(candidate)
            current.set_next(prime_node)
            current = current.get_next()
            count += 1
        candidate += 1
    return head

"""        Q3        """
def back_to_front_chain(first_node):
    try:
        size = get_chain_size(first_node)
        if size < 3:
            return
        head = first_node
        current = first_node
        previous = None
        count = 1
            
        while current.get_next() != None:
                previous = current
                current = current.get_next()
                
        current.set_next(head.get_next())
        head.set_next(current)
        previous.set_next(None)
    except:
        return None

def get_chain_size(first_node):
    count = 1
    current = first_node

    while current.get_next() != None:
        current = current.get_next()
        count += 1
    return count


"""        Q4        """
def really_create_tree_from_flat_list(flat_list, pos):
    if pos >= len(flat_list):
        return None
    if flat_list[pos] == None:
        return None
    head = BinaryTree(flat_list[pos])
    head.set_left(really_create_tree_from_flat_list(flat_list, pos * 2))
    head.set_right(really_create_tree_from_flat_list(flat_list, pos * 2 + 1))
    return head

def create_tree_from_flat_list(flat_list):
    return really_create_tree_from_flat_list(flat_list, 1)
    
def create_tree_from_nested_list(nested_list):
    if nested_list == None:
        return None
    head = BinaryTree(nested_list[0])
    head.set_left(create_tree_from_nested_list(nested_list[1]))
    head.set_right(create_tree_from_nested_list(nested_list[2]))
    return head


"""        Q5        """
def sum_tree(node):
    if not(node.get_left() or node.get_right()):
        return node.get_data()

    elif node.get_left() and node.get_right():
        return node.get_data() + sum_tree(node.get_left()) + sum_tree(node.get_right())

    elif not node.get_left():
        return node.get_data() + sum_tree(node.get_right())

    elif not node.get_right():
        return node.get_data() + sum_tree(node.get_left())
    
"""        Q6        """
def pre_order_rec(result_list, tree):
    if tree:
        result_list += [tree.get_data()]
        pre_order_rec(result_list, tree.get_left())
        pre_order_rec(result_list, tree.get_right())
    return result_list

def in_order_rec(result_list, tree):
    if tree:
        in_order_rec(result_list, tree.get_left())
        result_list += [tree.get_data()]
        in_order_rec(result_list, tree.get_right())
    return result_list

def post_order_rec(result_list, tree):
    if tree:
        post_order_rec(result_list, tree.get_left())
        post_order_rec(result_list, tree.get_right())
        result_list += [tree.get_data()]
    return result_list

def pre_order(tree):
    return pre_order_rec([],tree)

def in_order(tree):
    return in_order_rec([],tree)

def post_order(tree):
    return post_order_rec([],tree)

"""        Q7        """
def get_max(tree):
    if tree == None:
        return 0
    return max(tree.get_data(), get_max(tree.get_left()), get_max(tree.get_right()))

def get_min(tree):
    if tree == None:
        return 0
    return min(tree.get_data(), get_min(tree.get_left()), get_min(tree.get_right()))

def is_binary_search_tree(tree):
    if tree:
        left_sub_tree = get_max(tree.get_left())
        right_sub_tree = get_min(tree.get_right())
        in_order = left_sub_tree < tree.get_data() and right_sub_tree < tree.get_data()
        return is_binary_search_tree(tree.get_left()) and is_binary_search_tree(tree.get_right()) and in_order
    else:
        return True

"""        Q8        """
def insert_position_in_bst(tree, value):
    if value < tree.get_data():
        if tree.get_left():
            return insert_position_in_bst(tree.get_left(), value)
        else:
            return 'left of ' + str(tree.get_data())
    elif value > tree.get_data():
        if tree.get_right():
            return insert_position_in_bst(tree.get_right(), value)
        else:
            return 'right of ' + str(tree.get_data())

"""        Q9        """
def hash_with_probing(keys, size, probe_type):
    table = []
    for i in range(size):
        table.append(None)
    
    if probe_type == 'linear':
        for i in keys:
            hash_linear(i, table)
    if probe_type == 'quadratic':
        for i in keys:
            hash_quadratic(i, table)
    return table

def hash_linear(key, values):
    size = len(values)
    index = key % size
    while values[index] != None:
        index = (index + 1) % size
    values[index] = key

def hash_quadratic(key, values):
    size = len(values)
    index = key % size
    quad = key % size
    probes = 1
    while values[quad] != None:
        quad = (index + probes**2) % size
        probes += 1
    values[quad] = key
