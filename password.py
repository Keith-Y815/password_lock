C_password = input('Please create your password: ')
number = 0
chance = 3
while number < 3:
	I_password = input('Please input your password: ')
	if I_password == C_password:
		print('Password correct')
		break
	elif I_password != C_password:
		number = number + 1
		print(number)
		print('Password incorrect, you still can input ', 3 - number, ' times')
