class Stack:
	
	def __init__(self):
		self.stack = []
	def is_empty(self):
		return len(self.stack) == 0
	def push(self, item):
		self.stack.append(item)
	def pop(self):
		return self.stack.pop()
	def peek(self):
		return self.stack[-1]
	def size(self):
		return len(self.stack)

def stack_test():
	s1 = Stack()
	s2 = Stack()
	
	for i in range(5):
		s1.push(i)
	
	while not s1.is_empty():
		s2.push(s1.pop())
	
	while not s2.is_empty():
		print(s2.pop())

def bracket_check(string):
	stack = Stack()
	open_brackets = ['(','[','<','{']
	closed_brackets = [')',']','>','}']
	for character in string:
		if character in open_brackets:
			stack.push(character)
		if character in closed_brackets:
			if stack.size() == 0:
				return 'Unbalanced'
			if open_brackets.index(stack.peek()) == closed_brackets.index(character):
				stack.pop()
			else:
				return 'Unbalanced'
	if not stack.is_empty():
		return 'Unbalanced'
	return 'Balanced'

string1 = '(<[{}]>)'
string2 = '(<[{}>])'
string3 = '({}([{}{[<><>]}(()[])]<[{()}][]>{[[<><>]]})<>)()'	
stack_test()
print()
print(bracket_check(string1))
print(bracket_check(string2))
print(bracket_check(string3))

	
class Cars:

    def __init__(self, colour, speed):

        self.__colour = colour
        self.__speed = speed

 

    def __repr__(self):
        return 'Cars({0}, {1})'.format(self.__colour, self.__speed)

 

x = Cars('Blue', 25)

print(x)