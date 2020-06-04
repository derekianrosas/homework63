def greeting(name = 'Guest'):
	print(f'Hi {name}!')

greeting()
greeting("derek")

def some_function(collection = []):
	collection.append(1)
	print(id(collection))
	return collection


print(some_function())

#other part of program

print(some_function())