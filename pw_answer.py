password = 'a123456'
i = 3
while True:
	pwd = input('Please input password: ')
	if pwd == password:
		print('Password correct')
		break
	else:
		i = i - 1
		print('Password incorrect. You still can input ', i, ' times')
		if i == 0:
			break