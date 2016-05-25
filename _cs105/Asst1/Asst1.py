"""
	Cam Smith, csmi928, 706899195
	Compsci105 SS, Asst1
	2016-01-15
"""

## IMPORTANT: This source file is the only file to be submitted for marking.
## It should only contain four class definitions - no other program statements
## To test the four classes that you define in this source file, write your
## test code in the Asst1BasicProgram.py file and run the corresponding program.

## Question 1: The Polynomial class
class Polynomial:

	def __init__(self, coefficients):
		if len(coefficients) > 1:
			coefficients = ','.join(str(c) for c in coefficients)
			coefficients = coefficients.lstrip('0,')
			coefficients = [int(c) for c in coefficients.split(',')]
		self.coefficients = coefficients

	def __str__(self):
		result = ''
		powers = self.get_powers()
		coefficients = self.get_coefficients()
		if len(coefficients) == 1:
			return str(coefficients[0])
		for i in range(len(coefficients)):
			if coefficients[i] != 0 and powers[i] != 0:
				if i == 0 and coefficients[i] < 0:
					result += '-'
				if abs(coefficients[i]) > 1:
					result += str(abs(coefficients[i]))
				if powers[i] > 1:
					result += 'x^' + str(powers[i])
				elif powers[i] == 1:
					result += 'x'
			if powers[i] != 0:	
				if coefficients[i+1] > 0 :
					result += ' + '
				elif coefficients[i+1] < 0:
					result += ' - '
			if powers[i] == 0 and coefficients[i] != 0:
				result += str(abs(coefficients[i]))
		return result

	def scale(self, factor):
		coefficients = self.get_coefficients()
		new_coefficients = [old_coefficient * factor for old_coefficient in coefficients]
		self.set_coefficients(new_coefficients)
		
	def add(self, other):
		s_degree = self.get_degree()
		o_degree = other.get_degree()
		s_coefficients = self.get_coefficients()
		o_coefficients = other.get_coefficients()
		if s_degree > o_degree:
			o_coefficients = [0] * (s_degree - o_degree)  + o_coefficients
		elif o_degree > s_degree:
			s_coefficients = [0] * (o_degree - s_degree) + s_coefficients			
		new_coefficients = [s + o for s,o in zip(s_coefficients, o_coefficients)]
		return Polynomial(new_coefficients)
		
	def evaluate(self, x):
		sum = 0
		powers = self.get_powers()
		coefficients = self.get_coefficients()
		for i in range(len(powers)):
			sum += coefficients[i] * (x ** powers[i])
		return sum
	
	def get_coefficients(self):
		return self.coefficients
	
	def set_coefficients(self, coefficients):
		if len(coefficients) > 1 and sum(coefficients) != 0:
			coefficients = ','.join(str(c) for c in coefficients)
			coefficients = coefficients.lstrip('0,')
			coefficients = [int(c) for c in coefficients.split(',')]
			self.coefficients = coefficients
		else:
			self.coefficients = [coefficients[-1]]
		
	
	def get_powers(self):
		coefficients = self.get_coefficients()
		return [position - 1 for position in range(len(coefficients),0,-1)]
	
	def get_degree(self):
		degree = max(self.get_powers())
		return degree

## Question 2: The Student and Course classes
class Student:

	def __init__(self, name, id_number):
		self.name = name
		self.id = id_number
		self.p_mark = 0
		self.t_mark = 0

	def __str__(self):
		result = self.name + '_' + str(self.p_mark) + '_' + str(self.t_mark)
		return result

	def get_id_number(self):
		return self.id
	
	def set_marks(self, p, t):
		self.p_mark = p
		self.t_mark = t

	def passes(self, prac_requirement):
		average = (self.p_mark + self.t_mark) // 2
		if self.p_mark >= 50 and self.t_mark >= 50:
			return True
		elif average >= 50 and not prac_requirement:
			return True		
		else:
			return False

class Course:

	def __init__(self, name, practical_pass_requirement):
		self.name = name
		self.p_bool = practical_pass_requirement
		self.students = []

	def __str__(self):
		result = self.name + ' (' + str(len(self.students)) + ')'
		return result

	def set_practical_requirement(self, require):
		self.p_bool = require

	def add_students(self, new_students):
		for student in new_students:
			if student not in self.students:
				self.students.append(student)

	def set_marks(self, id_number, p, t):
		for student in self.students:
			if student.get_id_number() == id_number:
				student.set_marks(p, t)

	def passing_ids(self):
		pass_list = [student.get_id_number() for student in self.students if student.passes(self.p_bool)]
		return ' '.join(pass_list)

	def class_list(self):
		return ' '.join([str(student) for student in self.students])

		
## Question 3: The Area class
import json
class Area:

	def __init__(self, txt):
		self.data = []
		self.objects = []
		self.areas = []
		try:
			self.data = json.loads(txt)
		except:
			pass
		for element in self.data:
			if isinstance(element, dict):
				self.objects += [element]
		for object in self.objects:
			try:
				self.areas += [object['area']]
			except KeyError:
				pass

	def __str__(self):
		if len(self.data) == 0:
			return 'Invalid JSON'
		if len(self.areas) == 0:
			return 'No areas'
		return str(sum(self.areas))