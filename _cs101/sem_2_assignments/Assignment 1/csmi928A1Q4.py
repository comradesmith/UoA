""" Compsci 101 S2; Assignment 1 Question 4
	Encodes/decodes based on a 5 column columnar cipher
	fixed to messages of a length of 25 characters.
	Author: Cam Smith, csmi928, 706899195
"""

original_message = "Pagg rm rfomieugisanrn t!"
#Makes sure the message is 25 letters in length
message = original_message * 25
message = message[0:25]

encrypted_line_1 = message[0:5]
encrypted_line_2 = message[5:10]
encrypted_line_3 = message[10:15]
encrypted_line_4 = message[15:20]
encrypted_line_5 = message[20:25]

decrypted_line_1 = encrypted_line_1[0] + encrypted_line_2[0] + encrypted_line_3[0] + encrypted_line_4[0] + encrypted_line_5[0]
decrypted_line_2 = encrypted_line_1[1] + encrypted_line_2[1] + encrypted_line_3[1] + encrypted_line_4[1] + encrypted_line_5[1]
decrypted_line_3 = encrypted_line_1[2] + encrypted_line_2[2] + encrypted_line_3[2] + encrypted_line_4[2] + encrypted_line_5[2]
decrypted_line_4 = encrypted_line_1[3] + encrypted_line_2[3] + encrypted_line_3[3] + encrypted_line_4[3] + encrypted_line_5[3]
decrypted_line_5 = encrypted_line_1[4] + encrypted_line_2[4] + encrypted_line_3[4] + encrypted_line_4[4] + encrypted_line_5[4]

decrypted_message = decrypted_line_1 + decrypted_line_2 + decrypted_line_3 + decrypted_line_4 + decrypted_line_5

output_line_1 = "Original message: " + message
output_line_2 = "Encrypted message: " + decrypted_message
print(output_line_1)
print(output_line_2)