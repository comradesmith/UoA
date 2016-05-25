"""                        """
		# print_str = ''
		# power = 0
		# power_str = ''
		# top_power = len(self.coefficients) - 1
		# coeffs = self.coefficients
		
		# pos = 0
		# while pos < len(self.coefficients):
			# power = top_power - pos
			
			# if pos == 0:
				# if coeffs[pos] < 0:
					# print_str += '-'
				# elif coeffs[pos] == 0:
					# print_str += '0'
			
			# if abs(coeffs[pos]) > 1 and pos < top_power:
				# print_str += str(abs(coeffs[pos]))
			# if pos == top_power and abs(coeffs[pos]) != 0:
				# print_str += str(abs(coeffs[pos]))
			
			# if coeffs[pos] != 0:
			
				# if power > 1:
					# print_str += 'x^'
				# elif power == 1:
					# print_str += 'x'
				
				# if top_power - pos > 1:
					# print_str += str(top_power - pos)
					
				# if pos < top_power:
					# if coeffs[pos] > 0:
						# print_str += ' + '
					# elif coeffs[pos] < 0:
						# print_str += ' - '
				
			
			# pos += 1
		#return print_str
		
		"""                                   """
		
		# for i in range(len(self.coefficients)):
			# power = len(self.coefficients) - (i + 1)
			# coefficient = self.coefficients[i]
			# exclusions = [0,1,-1]
			
			# if power not in exclusions:
				# power_str = 'x^' + str(power)
			# elif power == 0:
				# power_str = ''
			# elif power == 1 or power == -1:
				# power_str = 'x'
				
			# if coefficient not in exclusions:
				# print_str += str(coefficient) + power_str
			# elif coefficient == 1 or coefficient == -1:
				# print_str += power_str
			
			# if power > 0 and coefficient > 0:	
				# print_str += ' + '
			# elif power > 0 and coefficient < 0:
				# print_str += ' - '
		# return print_str