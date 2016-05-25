import Asst2
import Node
import BinaryTree

def welcome_message():
    print('COMPSCI 105, Summer 2016')
    print('Final marks for Assignment Two\n')

## Marks for the 9 questions
asst_2_final_project_marks = [[], [], [], [], [], [], [], [], []]
asst_2_final_project_final = [12, 11, 11, 11, 11, 11, 11, 11, 11]

def print_marks(question):
    result = str(asst_2_final_project_marks[question-1].count(1)) + ' out of ' + str(len(asst_2_final_project_marks[question-1]))
    marks = asst_2_final_project_final[question-1] * (asst_2_final_project_marks[question-1].count(1) / len(asst_2_final_project_marks[question-1]))
    print('Mark for Question %s = %s ( %.2f out of %d marks )' % (question, result, marks, asst_2_final_project_final[question-1]))

def print_total_marks():
    correct = 0
    total = 0
    for i in range(len(asst_2_final_project_marks)):
        correct = correct + asst_2_final_project_final[i] * (asst_2_final_project_marks[i].count(1) / len(asst_2_final_project_marks[i]))
        total = total + asst_2_final_project_final[i]
    print('\nTotal mark for Assignment One = %.2f out of %d' % (correct, total))        
    print('\n<<<FINAL MARK FOR PROJECT>>> %.2f' % (correct))        
    
def formatted_test_result(question, expected, got):
    print('  Test Q' + str(question) + ' : ', end = '')
    if expected == got:
        print('  PASS :-)  ', got)
        asst_2_final_project_marks[question-1].append(1)
    else:
        print('  FAIL :-(')
        print('    - the expected output = ', expected)
        print('    - the actual output =   ', got)
        asst_2_final_project_marks[question-1].append(0)

def a2_is_prime(x):
    if x > 1:
        for i in range(2,x):
            if (x % i) == 0:
                return False
        return True       
    else:
        return False

def a2_generate_prime_chain(n):
    current_prime = 2
    a = Node.Node(current_prime)
    current = a
    count = 0
    while count < n-1:
        count += 1
        current_prime += 1
        while not a2_is_prime(current_prime):
            current_prime += 1
        temp = Node.Node(current_prime)
        current.set_next(temp)
        current = current.get_next()
    return a

def a2_create_tree_from_nested_list(node_list):
    if node_list:
        result = BinaryTree.BinaryTree(node_list[0])
        left = a2_create_tree_from_nested_list(node_list[1])
        right = a2_create_tree_from_nested_list(node_list[2])
        if left != None:
            result.set_left(left)
        if right != None:
            result.set_right(right)
        return result
    
def q1_test(infix, expected):
    try:
        result = Asst2.generate_postfix(infix)
    except:
        result = 'an exception occurred'
    formatted_test_result(1, expected, result)

def q2_test(n, expected):
    try:
        result = []
        c = Asst2.generate_prime_chain(n)
        while c != None:
            result.append(c.get_data())
            c = c.get_next()
    except:
        result = 'an exception occurred'
    formatted_test_result(2, expected, result)

def q3_test(n, expected):
    try:
        result = []
        c = a2_generate_prime_chain(n)
        Asst2.back_to_front_chain(c)
        while c != None:
            result.append(c.get_data())
            c = c.get_next()
    except:
        result = 'an exception occurred'
    formatted_test_result(3, expected, result)

## convert_tree_to_list() function from Binary Tree lecture (slide 35)
def convert_tree_to_list(t):
    if t == None:
        return None
    else:
        result = []
        result.append(t.get_data()) 
        result.append(convert_tree_to_list(t.get_left()))
        result.append(convert_tree_to_list(t.get_right()))
        return result

def q4_test_nested(flat_list, nested_list):
    try:
        t2 = Asst2.create_tree_from_nested_list(nested_list)
        result2 = convert_tree_to_list(t2)
    except:
        result2 = 'an exception occurred'
    formatted_test_result(4, nested_list, result2)

def q4_test_flat(flat_list, nested_list):
    try:
        t1 = Asst2.create_tree_from_flat_list(flat_list)
        result1 = convert_tree_to_list(t1)
    except:
        result1 = 'an exception occurred'
    formatted_test_result(4, nested_list, result1) #compare against correct nested list

def q5_test(nested_list, expected):
    try:
        t = a2_create_tree_from_nested_list(nested_list)
        result = Asst2.sum_tree(t)
    except:
        result = 'an exception occurred'
    formatted_test_result(5, expected, result)

def q6_test(nested_list, expected1, expected2, expected3):
    try:
        t = a2_create_tree_from_nested_list(nested_list)
        result1 = Asst2.pre_order(t)
        result2 = Asst2.in_order(t)
        result3 = Asst2.post_order(t)
    except:
        result1 = 'an exception occurred'
        result2 = 'an exception occurred'
        result3 = 'an exception occurred'
    formatted_test_result(6, expected1, result1)
    formatted_test_result(6, expected2, result2)
    formatted_test_result(6, expected3, result3)

def q7_test(nested_list, expected):
    try:
        t = a2_create_tree_from_nested_list(nested_list)
        result = Asst2.is_binary_search_tree(t)
    except:
        result = 'an exception occurred'
    formatted_test_result(7, expected, result)

def q8_test(nested_list, n, expected):
    try:
        t = a2_create_tree_from_nested_list(nested_list)
        result = Asst2.insert_position_in_bst(t, n)
    except:
        result = 'an exception occurred'
    formatted_test_result(8, expected, result)

def q9_test(keys, table_size, probe_type, expected):
    try:
        result = Asst2.hash_with_probing(keys, table_size, probe_type)
    except:
        result = 'an exception occurred'
    formatted_test_result(9, expected, result)

def test_question_one():
    print('\nTesting Question One\n--------------------')
    q1_test('2 ^ ( 4 < 6 ) - 3 / 3 * 1', '2 4 6 < ^ 3 3 / 1 * -')
    q1_test('( 1 + ( 1 + ( 1 + ( 1 + ( 1 + 1 ) ) ) ) * 2 )', '1 1 1 1 1 1 + + + + 2 * +')
    q1_test('555', '555')
    q1_test('6 > 7 + 6', '6 7 6 + >')
    q1_test('2 * ( 3 + 7 )', '2 3 7 + *')
    q1_test('7 * 2 ^ ( 8 + 4 / 2 > 1 ) - 15 / 4', '7 2 8 4 2 / + 1 > ^ * 15 4 / -')

    q1_test(') 555 (', 'imbalanced brackets')
    q1_test('7 * 2 ^ ( 8 + 4 / 2 > 1 ( - 15 / 4', 'imbalanced brackets')
    q1_test('( 6 > 7 + 6', 'imbalanced brackets')
    q1_test('2 ^ ( 4 < 6 ) - 3 / 3 * 1 )', 'imbalanced brackets')
    q1_test('2 * ( 3 + 7 ) (', 'imbalanced brackets')
    q1_test('( 1 + ( 1 ) + ( 1 + ( 1 + ( 1 + 1 ) ) ) ) * 2 )', 'imbalanced brackets')
    q1_test('555 (', 'imbalanced brackets')

    q1_test('x', 'invalid symbol')
    q1_test('6 ! 7 + 6', 'invalid symbol')
    q1_test('7 * 2 ^ ( 8.8 + 4 / 2 > 1 ) - 15 / 4', 'invalid symbol')
    q1_test('555 % 555', 'invalid symbol')
    q1_test('2 ^ ( 4 < 6.0 ) - 3 / 3 * 1', 'invalid symbol')
    q1_test('2 * ( 3 & 7 )', 'invalid symbol')
    q1_test('( 1 + ( 1 + ( 1 + ( 1 + ( 1 + 1 ) ) ) ) = 2 )', 'invalid symbol')

    q1_test('555 +', 'too many operators')
    q1_test('555 + 555 +', 'too many operators')
    q1_test('( 1 + ( 1 + ( * 1 + ( 1 + ( 1 + 1 ) ) ) ) * 2 )', 'too many operators')
    q1_test('7 * 2 ^ ( 8 + 4 / 2 > 1 ) + - 15 / 4', 'too many operators')
    q1_test('2 * ( + 7 )', 'too many operators')
    q1_test('6 > 7 + 6 ^', 'too many operators')
    q1_test('2 ^ ( 4 < 6 ) - / 3 * 1', 'too many operators')

    q1_test('7 * 2 ( 8 + 4 / 2 > 1 ) - 15 / 4', 'too few operators')
    q1_test('555 555', 'too few operators')
    q1_test('555 + 555 555', 'too few operators')
    q1_test('6 > 7 + 6 100', 'too few operators')
    q1_test('2 ^ ( 4 < 6 ) 5 - 3 / 3 * 1', 'too few operators')
    q1_test('2 * ( 3 10 + 7 )', 'too few operators')
    q1_test('( 1 + ( 1 + ( 1 + ( 1 + ( 1 + 1 ) ) ) ) 4 * 2 )', 'too few operators')

def test_question_two():
    print('\nTesting Question Two\n--------------------')
    q2_test(1, [2])
    q2_test(2, [2, 3])
    q2_test(4, [2, 3, 5, 7])
    q2_test(3, [2, 3, 5])
    q2_test(169, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009])
    q2_test(171, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019])
    q2_test(15, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
    q2_test(16, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53])
    q2_test(14, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43])
    q2_test(5, [2, 3, 5, 7, 11])
    q2_test(6, [2, 3, 5, 7, 11, 13])
    q2_test(7, [2, 3, 5, 7, 11, 13, 17])
    q2_test(8, [2, 3, 5, 7, 11, 13, 17, 19])
    q2_test(9, [2, 3, 5, 7, 11, 13, 17, 19, 23])
    q2_test(10, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

def test_question_three():
    print('\nTesting Question Three\n----------------------')
    q3_test(1, [2])
    q3_test(2, [2, 3])
    q3_test(3, [2, 5, 3])
    q3_test(169, [2, 1009, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997])
    q3_test(4, [2, 7, 3, 5])
    q3_test(5, [2, 11, 3, 5, 7])
    q3_test(6, [2, 13, 3, 5, 7, 11])
    q3_test(7, [2, 17, 3, 5, 7, 11, 13])
    q3_test(8, [2, 19, 3, 5, 7, 11, 13, 17])
    q3_test(9, [2, 23, 3, 5, 7, 11, 13, 17, 19])
    q3_test(10, [2, 29, 3, 5, 7, 11, 13, 17, 19, 23])
    q3_test(171, [2, 1019, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013])
    q3_test(15, [2, 47, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43])
    q3_test(16, [2, 53, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
    q3_test(14, [2, 43, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41])

def test_question_four():
    print('\nTesting Question Four\n---------------------')
    q4_test_nested([None, 10, 5], [10, [5, None, None], None])
    q4_test_flat([None, 10, 5], [10, [5, None, None], None])
    q4_test_nested([None, 10, 5, 15, None, None, 11, 22], [10, [5, None, None], [15, [11, None, None], [22, None, None]]])
    q4_test_flat([None, 10, 5, 15, None, None, 11, 22], [10, [5, None, None], [15, [11, None, None], [22, None, None]]])
    q4_test_nested([None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [1, [2, [4, [8, None, None], [9, None, None]], [5, [10, None, None], [11, None, None]]], [3, [6, [12, None, None], [13, None, None]], [7, [14, None, None], [15, None, None]]]])
    q4_test_flat([None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [1, [2, [4, [8, None, None], [9, None, None]], [5, [10, None, None], [11, None, None]]], [3, [6, [12, None, None], [13, None, None]], [7, [14, None, None], [15, None, None]]]])
    q4_test_nested([None, 1, 2, None, 4, 5, None, None, 8, 9, 10, 11], [1, [2, [4, [8, None, None], [9, None, None]], [5, [10, None, None], [11, None, None]]], None])
    q4_test_flat([None, 1, 2, None, 4, 5, None, None, 8, 9, 10, 11], [1, [2, [4, [8, None, None], [9, None, None]], [5, [10, None, None], [11, None, None]]], None])
    q4_test_nested([None, 1, None, 3, None, None, 6, 7, None, None, None, None, 12, None, 14, 15], [1, None, [3, [6, [12, None, None], None], [7, [14, None, None], [15, None, None]]]])
    q4_test_flat([None, 1, None, 3, None, None, 6, 7, None, None, None, None, 12, None, 14, 15], [1, None, [3, [6, [12, None, None], None], [7, [14, None, None], [15, None, None]]]])
    q4_test_nested([None, 1], [1, None, None])
    q4_test_flat([None, 1], [1, None, None])
    q4_test_nested([None, 1, 2], [1, [2, None, None], None])
    q4_test_flat([None, 1, 2], [1, [2, None, None], None])
    q4_test_nested([None, 1, None, 3], [1, None, [3, None, None]])
    q4_test_flat([None, 1, None, 3], [1, None, [3, None, None]])
    q4_test_nested([None, 1, 2, None, 4, None, None, None, 8, None, None, None, None, None, None, None, 16], [1, [2, [4, [8, [16, None, None], None], None], None], None])
    q4_test_flat([None, 1, 2, None, 4, None, None, None, 8, None, None, None, None, None, None, None, 16], [1, [2, [4, [8, [16, None, None], None], None], None], None])
    q4_test_nested([None, 1, None, 3, None, None, None, 7, None, None, None, None, None, None, None, 15], [1, None, [3, None, [7, None, [15, None, None]]]])
    q4_test_flat([None, 1, None, 3, None, None, None, 7, None, None, None, None, None, None, None, 15], [1, None, [3, None, [7, None, [15, None, None]]]])

def test_question_five():
    print('\nTesting Question Five\n---------------------')
    q5_test([10, [5, None, None], None], 15)
    q5_test([10, [5, None, None], [15, [11, None, None], [22, None, None]]], 63)
    q5_test([10, [50, None, None], None], 60)
    q5_test([10, [5, None, None], [15, [11, None, None], [21, None, None]]], 62)
    q5_test([1, [2, [4, [8, None, None], [9, None, None]], [5, [10, None, None], [11, None, None]]], [3, [6, [12, None, None], [13, None, None]], [7, [14, None, None], [15, None, None]]]], 120)
    q5_test([1, [2, [4, [8, None, None], [9, None, None]], [5, [10, None, None], [11, None, None]]], None], 50)
    q5_test([1, None, [3, [6, [12, None, None], None], [7, [14, None, None], [15, None, None]]]], 58)
    q5_test([1000, None, None], 1000)
    q5_test([1, [200, None, None], None], 201)
    q5_test([1, None, [33, None, None]], 34)
    q5_test([1, [2, [4, [8, [16, None, None], None], None], None], None], 31)
    q5_test([1, None, [3, None, [7, None, [15, None, None]]]], 26)
    q5_test([1000, None, [1000, None, None]], 2000)

def test_question_six():
    print('\nTesting Question Six\n--------------------')
    q6_test([10, [5, None, None], [15, [11, None, None], [22, None, None]]], [10, 5, 15, 11, 22], [5, 10, 11, 15, 22], [5, 11, 22, 15, 10])
    q6_test([10, [5, None, None], None], [10, 5], [5, 10], [5, 10])
    q6_test([10, [50, None, None], [51, None, None]], [10, 50, 51], [50, 10, 51], [50, 51, 10])
    q6_test([10, [5, None, None], [15, [11, None, None], [21, None, None]]], [10, 5, 15, 11, 21], [5, 10, 11, 15, 21], [5, 11, 21, 15, 10])
    q6_test([1, [2, [4, [8, None, None], [9, None, None]], [5, [10, None, None], [11, None, None]]], [3, [6, [12, None, None], [13, None, None]], [7, [14, None, None], [15, None, None]]]], [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15], [8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15], [8, 9, 4, 10, 11, 5, 2, 12, 13, 6, 14, 15, 7, 3, 1])
    q6_test([1, [2, [4, [8, [16, None, None], None], None], None], None], [1, 2, 4, 8, 16], [16, 8, 4, 2, 1], [16, 8, 4, 2, 1])
    q6_test([1, None, [3, [6, [12, None, None], None], [7, [14, None, None], [15, None, None]]]], [1, 3, 6, 12, 7, 14, 15], [1, 12, 6, 3, 14, 7, 15], [12, 6, 14, 15, 7, 3, 1])
    q6_test([1000, None, None], [1000], [1000], [1000])

def test_question_seven():
    print('\nTesting Question Seven\n----------------------')
    q7_test([10, [5, None, None], [15, [11, None, None], [22, None, None]]], True)
    q7_test([12, [6, [3, None, None], [13, None, None]], [25, None, None]], False)
    q7_test([2, [1, None, None], [3, None, None]], True)
    q7_test([2, None, [3, None, None]], True)
    q7_test([2, [1, None, None], None], True)
    q7_test([200, None, None], True)
    q7_test([2, [3, None, None], [1, None, None]], False)
    q7_test([2, None, [1, None, None]], False)
    q7_test([2, [3, None, None], None], False)
    q7_test([1, [2, [4, [8, None, None], [9, None, None]], [5, [10, None, None], [11, None, None]]], [3, [6, [12, None, None], [13, None, None]], [7, [14, None, None], [15, None, None]]]], False)
    q7_test([8, [4, [2, [1, None, None], [3, None, None]], [6, [5, None, None], [7, None, None]]], [12, [10, [9, None, None], [11, None, None]], [14, [13, None, None], [15, None, None]]]], True)
    q7_test([8, [4, [2, [1, None, None], [3, None, None]], [6, [5, None, None], [7, None, None]]], [12, [10, None, [11, None, None]], [14, [13, None, None], [15, None, None]]]], True)
    q7_test([8, [4, [2, [1, None, None], [3, None, None]], [6, [5, None, None], [7, None, None]]], [12, [10, [11, None, None], [9, None, None]], [14, [13, None, None], [15, None, None]]]], False)

def test_question_eight():
    print('\nTesting Question Eight\n----------------------')

    q8_test([80, [40, [20, [10, None, None], [30, None, None]], [60, [50, None, None], [70, None, None]]], [120, [100, [90, None, None], [110, None, None]], [140, [130, None, None], [150, None, None]]]], 5, 'left of 10')
    q8_test([80, [40, [20, [10, None, None], [30, None, None]], [60, [50, None, None], [70, None, None]]], [120, [100, [90, None, None], [110, None, None]], [140, [130, None, None], [150, None, None]]]], 15, 'right of 10')
    q8_test([80, [40, [20, [10, None, None], [30, None, None]], [60, [50, None, None], [70, None, None]]], [120, [100, [90, None, None], [110, None, None]], [140, [130, None, None], [150, None, None]]]], 25, 'left of 30')
    q8_test([80, [40, [20, [10, None, None], [30, None, None]], [60, [50, None, None], [70, None, None]]], [120, [100, [90, None, None], [110, None, None]], [140, [130, None, None], [150, None, None]]]], 35, 'right of 30')
    q8_test([80, [40, [20, [10, None, None], [30, None, None]], [60, [50, None, None], [70, None, None]]], [120, [100, [90, None, None], [110, None, None]], [140, [130, None, None], [150, None, None]]]], 45, 'left of 50')
    q8_test([80, [40, [20, [10, None, None], [30, None, None]], [60, [50, None, None], [70, None, None]]], [120, [100, [90, None, None], [110, None, None]], [140, [130, None, None], [150, None, None]]]], 55, 'right of 50')
    q8_test([80, [40, [20, [10, None, None], [30, None, None]], [60, [50, None, None], [70, None, None]]], [120, [100, [90, None, None], [110, None, None]], [140, [130, None, None], [150, None, None]]]], 65, 'left of 70')
    q8_test([80, [40, [20, [10, None, None], [30, None, None]], [60, [50, None, None], [70, None, None]]], [120, [100, [90, None, None], [110, None, None]], [140, [130, None, None], [150, None, None]]]], 75, 'right of 70')
    q8_test([80, [40, [20, [10, None, None], [30, None, None]], [60, [50, None, None], [70, None, None]]], [120, [100, [90, None, None], [110, None, None]], [140, [130, None, None], [150, None, None]]]], 85, 'left of 90')
    q8_test([80, [40, [20, [10, None, None], [30, None, None]], [60, [50, None, None], [70, None, None]]], [120, [100, [90, None, None], [110, None, None]], [140, [130, None, None], [150, None, None]]]], 95, 'right of 90')
    q8_test([80, [40, [20, [10, None, None], [30, None, None]], [60, [50, None, None], [70, None, None]]], [120, [100, [90, None, None], [110, None, None]], [140, [130, None, None], [150, None, None]]]], 105, 'left of 110')
    q8_test([80, [40, [20, [10, None, None], [30, None, None]], [60, [50, None, None], [70, None, None]]], [120, [100, [90, None, None], [110, None, None]], [140, [130, None, None], [150, None, None]]]], 115, 'right of 110')
    q8_test([80, [40, [20, [10, None, None], [30, None, None]], [60, [50, None, None], [70, None, None]]], [120, [100, [90, None, None], [110, None, None]], [140, [130, None, None], [150, None, None]]]], 125, 'left of 130')
    q8_test([80, [40, [20, [10, None, None], [30, None, None]], [60, [50, None, None], [70, None, None]]], [120, [100, [90, None, None], [110, None, None]], [140, [130, None, None], [150, None, None]]]], 135, 'right of 130')
    q8_test([80, [40, [20, [10, None, None], [30, None, None]], [60, [50, None, None], [70, None, None]]], [120, [100, [90, None, None], [110, None, None]], [140, [130, None, None], [150, None, None]]]], 145, 'left of 150')
    q8_test([80, [40, [20, [10, None, None], [30, None, None]], [60, [50, None, None], [70, None, None]]], [120, [100, [90, None, None], [110, None, None]], [140, [130, None, None], [150, None, None]]]], 155, 'right of 150')
    q8_test([10, [6, None, None], [15, [11, None, None], [22, None, None]]], 3, 'left of 6')
    q8_test([10, [5, None, None], [15, [12, None, None], [22, None, None]]], 13, 'right of 12')
    q8_test([12, [6, [3, None, None], [11, None, None]], [29, None, None]], 100, 'right of 29')
    q8_test([12, [6, [3, None, None], [10, None, None]], [25, None, None]], 9, 'left of 10')
    q8_test([100, None, None], 50, 'left of 100')
    q8_test([100, None, None], 150, 'right of 100')

def test_question_nine():
    print('\nTesting Question Nine\n---------------------')
    q9_test([26, 54, 94, 17, 31, 77, 44, 51], 13, 'linear', [26, 51, 54, 94, 17, 31, 44, None, None, None, None, None, 77])
    q9_test([26, 54, 94, 17, 31, 77, 43, 25], 13, 'quadratic', [26, None, 54, 94, 17, 31, None, None, 43, None, None, 25, 77])
    q9_test([26, 54, 94, 17, 31, 77, 44, 51], 11, 'linear', [77, 44, None, None, 26, None, 94, 17, 51, 31, 54])
    q9_test([26, 54, 94, 17, 31, 77, 43, 25], 11, 'quadratic', [77, 25, None, 43, 26, None, 94, 17, None, 31, 54])
    q9_test([2, 4, 8, 16, 32, 64, 128, 256], 13, 'linear', [None, None, 2, 16, 4, None, 32, None, 8, 256, None, 128, 64])
    q9_test([2, 4, 8, 16, 32, 64, 128, 256], 13, 'quadratic', [None, None, 2, 16, 4, None, 32, None, 8, 256, None, 128, 64])
    q9_test([2, 4, 8, 16, 32, 64, 128, 256], 11, 'linear', [None, None, 2, 256, 4, 16, None, 128, 8, 64, 32])
    q9_test([2, 4, 8, 16, 32, 64, 128, 256], 11, 'quadratic', [None, None, 2, 256, 4, 16, None, 128, 8, 64, 32])
    q9_test([11, 20, 35, 49, 52, 61, 71, 87, 94], 17, 'linear', [None, 35, 52, 20, 71, 87, None, None, None, 94, 61, 11, None, None, None, 49, None])
    q9_test([11, 20, 35, 49, 52, 61, 71, 87, 94], 17, 'quadratic', [None, 35, 52, 20, 71, None, 87, None, None, 94, 61, 11, None, None, None, 49, None])
    q9_test([11, 20, 35, 49, 52, 61, 71, 87, 94], 13, 'linear', [52, 87, None, 94, None, None, 71, 20, None, 35, 49, 11, 61])
    q9_test([11, 20, 35, 49, 52, 61, 71, 87, 94], 13, 'quadratic', [52, None, None, 94, None, 61, 71, 20, None, 35, 49, 11, 87])
    q9_test([11, 20, 35, 49, 52, 61, 71, 87, 94], 11, 'linear', [11, 94, 35, None, None, 49, 61, 71, 52, 20, 87])
    q9_test([11, 20, 35, 49, 52, 61, 71, 87, 94], 11, 'quadratic', [11, None, 35, 71, None, 49, 61, 94, 52, 20, 87])
    q9_test([4, 8, 14, 18, 24, 28, 35], 11, 'linear', [None, None, 24, 14, 4, 35, 28, 18, 8, None, None])
    q9_test([4, 8, 14, 18, 24, 28, 35], 11, 'quadratic', [35, None, 24, 14, 4, None, 28, 18, 8, None, None])
    q9_test([4, 14, 18, 24, 28, 35, 27, 50, 73], 23, 'linear', [None, 24, None, None, 4, 28, 27, 50, 73, None, None, None, 35, None, 14, None, None, None, 18, None, None, None, None])
    q9_test([4, 14, 18, 24, 28, 35, 27, 50, 73], 23, 'quadratic', [None, 24, None, None, 4, 28, None, None, 27, None, None, None, 35, 50, 14, None, None, None, 18, None, 73, None, None])
    q9_test([4, 14, 18, 24, 28, 35, 27, 52, 73], 17, 'linear', [None, 18, 35, 52, 4, 73, None, 24, None, None, 27, 28, None, None, 14, None, None])
    q9_test([4, 14, 18, 24, 28, 35, 27, 52, 73], 17, 'quadratic', [None, 18, 35, None, 4, 52, 73, 24, None, None, 27, 28, None, None, 14, None, None])
    
welcome_message()

test_question_one()
test_question_two()
test_question_three()
test_question_four()
test_question_five()
test_question_six()
test_question_seven()
test_question_eight()
test_question_nine()

print('\nMarks for Assignment Two:\n')

for i in range(1, 10):
    print_marks(i)

print_total_marks()

