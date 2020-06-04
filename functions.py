def auth(email, password):
	if email == 'derek@rosas.com' and password == 'secret':
		print('Authorized')
	else:
		print('Not Authorized')

auth('derek@rosas.com', 'secret')

def counter(max_value):
	for num in range(1, max_value):
		print(num)

counter(501)