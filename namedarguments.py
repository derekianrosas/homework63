#function that needs to take in a collection of data,
def greeting(*args):
	print('Hi ' + ' '.join(args)) #join joins collections and spits them out as strings

greeting('Tiffany', 'Derek')
greeting('Derek', 'Ian', 'Rosas')

#positional first and then collection argument
