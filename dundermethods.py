

#double underscore is how python works with private and protected classes
#private methods
#str method, python looks for the defined class and returns whats inside/ the goal is to help you get some visibility 
class Invoice:
	def __init__(self, client, total):
		self.client = client
		self.total = total


	def __str__(self):
		return f'Invoice from {self.client} for {self.total}'
	def __repr__(self):
		return f'Invoice <value: client: {self.client}, total: {self.total}>'

inv = Invoice('google', 500)

print(str(inv))
print(repr(inv))
#string for nice output and repr true raw data in the class
