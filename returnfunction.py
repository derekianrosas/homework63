#the difference between printing and returning something from a function
def full_name(first, last):
	return f'{first} {last}'

derek = full_name('Derek', 'Rosas')

def greeting(name):
	print(f'Hi {name}!')

greeting(derek)