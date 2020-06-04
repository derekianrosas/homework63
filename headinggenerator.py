#working with string interpolation to create a function to have some kind of functionde
def heading_generator(title, heading_type):
	return f'<h{heading_type}>{title}</h{heading_type}>'
print(heading_generator('Greeting', '1'))
print(heading_generator('Dawgy', '2'))