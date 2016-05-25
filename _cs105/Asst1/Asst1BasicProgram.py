from Asst1 import Polynomial
from Asst1 import Course
from Asst1 import Student
from Asst1 import Area
        
def polynomials():
        
        print('\n=== Polynomials =============================')

        print('\n--- Printing -----------------------------')
        p1 = Polynomial([2,3,4])
        p2 = Polynomial([10,5,2,0,2])
        p3 = Polynomial([1,1,1,1,1])
        p4 = Polynomial([6,0,0,0])
        p5 = Polynomial([-2,3,-4])
        p6 = Polynomial([10,-5,-2,0,2])
        p7 = Polynomial([-1,-1,-1,-1,-1])
        p8 = Polynomial([1,0,-2])
        p9 = Polynomial([1])
        p10 = Polynomial([0])

        print('p1 =', p1)
        print('p2 =', p2)
        print('p3 =', p3)
        print('p4 =', p4)
        print('p5 =', p5)
        print('p6 =', p6)
        print('p7 =', p7)
        print('p8 =', p8)
        print('p9 =', p9)
        print('p10 =', p10)

        print('\n--- Evaluating -----------------------------')
        p1 = Polynomial([2,3,4])
        p2 = Polynomial([10,5,2,0,2])
        p3 = Polynomial([1,1,1,1,1])
        p4 = Polynomial([6,0,0,0])

        print('p1(4) =', p1.evaluate(4))
        print('p2(0) =', p2.evaluate(0))
        print('p3(-2) =', p3.evaluate(-2))
        print('p4(3) =', p4.evaluate(3))

        print('\n--- Degrees -----------------------------')
        p1 = Polynomial([2,3,4])
        p2 = Polynomial([10,5,2,0,2])
        p3 = Polynomial([1,1,1,1,1])
        p4 = Polynomial([6,0,0,0])

        print('Degree of p1 =', p1.get_degree())
        print('Degree of p2 =', p2.get_degree())
        print('Degree of p3 =', p3.get_degree())
        print('Degree of p4 =', p4.get_degree())

        print('\n--- Scaling -----------------------------')
        p1 = Polynomial([2,3,4])
        p2 = Polynomial([10,5,2,0,2])
        p3 = Polynomial([1,1,1,1,1])
        p4 = Polynomial([6,0,0,0])

        p1.scale(5)
        p2.scale(-5)
        p3.scale(5)
        p4.scale(5)

        print(p1)
        print(p2)
        print(p3)
        print(p4)

        print('\n--- Addition -----------------------------')
        p1 = Polynomial([2,3,4])
        p2 = Polynomial([10,5,2,0,2])
        p3 = Polynomial([1,1,1,1,1])
        p4 = Polynomial([6,0,0,0])

        sum1 = p1.add(p2)
        sum2 = p3.add(p4)

        print('sum1 =', sum1)
        print('sum2 =', sum2)
        
        print('\n--- Caution -----------------------------')
        print('\n--- NOTE: You should uncomment the code below to test')
        x2 = Polynomial([2,-3,0,4])
        y2 = Polynomial([-2,3,1,1])
        z2 = x2.add(y2)

        print('z2 =', z2)
        print('Degree of z2 =', z2.get_degree())

        my_list = [1,2,3]

        share1 = Polynomial(my_list)
        share2 = Polynomial(my_list)

        share1.scale(2)

        print('share1 =', share1)
        print('share2 =', share2)


def courses_and_students():
        
        print('\n=== Students =============================')

        print('\n--- Printing -----------------------------')
        s1 = Student('ann', '1234')
        s2 = Student('bob', '2345')
        s3 = Student('clare', '3456')
        s4 = Student('dave', '4567')

        print(s1)
        print(s2)
        print(s3)
        print(s4)

        print('\n--- ID numbers -----------------------------')
        print('ID of s1 =', s1.get_id_number())
        print('ID of s2 =', s2.get_id_number())
        print('ID of s3 =', s3.get_id_number())
        print('ID of s4 =', s4.get_id_number())

        print('\n--- Set marks -----------------------------')
        s1.set_marks(60, 75)
        s2.set_marks(30, 45)
        s3.set_marks(45, 75)
        s4.set_marks(80, 10)

        print(s1)
        print(s2)
        print(s3)
        print(s4)

        print('\n--- Passing? -----------------------------')
        print('With a practical pass requirement:')
        print('s1 passes?', s1.passes(True))
        print('s2 passes?', s2.passes(True))
        print('s3 passes?', s3.passes(True))
        print('s4 passes?', s4.passes(True))

        print('With no practical pass requirement:')
        print('s1 passes?', s1.passes(False))
        print('s2 passes?', s2.passes(False))
        print('s3 passes?', s3.passes(False))
        print('s4 passes?', s4.passes(False))


        print('\n=== Courses =============================')

        print('\n--- Printing -----------------------------')
        basket_weaving = Course('Basket weaving', True)
        print(basket_weaving)

        s1 = Student('ann', '1234')
        s2 = Student('bob', '2345')
        s3 = Student('clare', '3456')
        s4 = Student('dave', '4567')
        s5 = Student('edna', '5678')
        s6 = Student('frank', '6789')

        print('\n--- Adding students -----------------------------')
        basket_weaving.add_students([s1, s2, s3])
        print(basket_weaving)

        basket_weaving.add_students([s4, s5])
        print(basket_weaving)

        basket_weaving.add_students([s1, s2, s3, s4, s5, s6])
        print(basket_weaving)

        print('\n--- Class list -----------------------------')
        print(basket_weaving.class_list())

        print('\n--- Set marks -----------------------------')
        basket_weaving.set_marks('1234', 80, 90)
        basket_weaving.set_marks('2345', 10, 95)
        basket_weaving.set_marks('3456', 50, 50)
        basket_weaving.set_marks('4567', 48, 52)
        basket_weaving.set_marks('6789', 100, 49)

        print(basket_weaving.class_list())

        print('\n--- Passing IDs -----------------------------')
        print(basket_weaving.passing_ids())

        print('\n--- Pass requirement -----------------------------')
        basket_weaving.set_practical_requirement(False)
        print(basket_weaving.passing_ids())

def areas():

        print('\n=== Areas =============================')

        a = Area('hello world')
        b = Area('[a,b,c')
        print('a =', a)
        print('b =', b)

        c = Area('[1, 2, 3]')
        d = Area('["Hello", "World"]')
        print('c =', c)
        print('d =', d)

        e = Area('[1, 2, 3, {"area": 123, "weight": 1000}]')
        f = Area('["Hello", "World", {"area": 999}]')
        print('e =', e)
        print('f =', f)

        g = Area('[{"height": 100}, {"size": 123, "weight": 1000}]')
        h = Area('["Hello", "World", {"volume": 999}]')
        print('g =', g)
        print('h =', h)
    
        i = Area('[{"area": 100}, {"area": 123, "weight": 1000}]')
        j = Area('["Hello", "World", {"area": 999}, {"area": 1}]')
        k = Area('[{"area": -1000}, {"area": 999}, {"area": 1}]')
        print('i =', i)
        print('j =', j)
        print('k =', k)


import sys
def print_welcome():
        print('CS105 - Summer School 2016')
        print('Assignment One')
        print('\nHi there - welcome to the first assignment!  In this assignment you will be')
        print('defining several classes.')
        print('\nThis source file (Asst1BasicProgram.py) is a basic program that is designed')
        print('to be run alongside the Asst1.py source file which is the file that you will')
        print('submit for marking.  You are welcome to modify this source file, or to test')
        print('your class definitions in Asst1.py in some other way, but you will not be')
        print('submitting any of your test code.  You will only submit Asst1.py which is')
        print('the file that contains your class definitions.')
        print('\nPlease begin by carefully reading the Asst1.pdf document.  Your assignment')
        print('will be marked automatically, so it is *very* important that you follow the')
        print('instructions and particularly the precise output format that is required.')
        print('\nIMPORTANT: Please read the last page of the Asst1.pdf document.  This is')
        print('an individual assignment - you must write all of the source code yourself.')
        print('You must not copy any source code, or allow any of your source code to be')
        print('copied - this will be checked, so please heed this advice.  You are welcome')
        print('to discuss ideas or algorithms with others... just no source code.')
        if not input('\nDo you understand this... (y/n)? ').lower() == 'y':
                print('\nPlease re-read the last page of the assignment, or talk to Paul \nfor clarification!')
                sys.exit()
        print('\nOK, let''s get started!  Make sure the Asst1.py source file is in the same')
        print('directory as this program source file.  If this is the first time you are')
        print('running the program, you are going to see a lot of output with statements like')
        print('"Soon to be implemented!" and "None".  Once you start working on the Asst1.py ')
        print('source file, these will be replaced with the correct output, which you can ')
        print('check against the output in the Asst1.pdf document.  Good luck!')
        if not input('\nReady... (y/n)? ').lower() == 'y':
                print('\nNo worries, see you soon!')
                sys.exit()

## Display a welcome message
print(sys.version)
print_welcome()


## Use the classes required for this assignment
polynomials()
courses_and_students()
areas()

