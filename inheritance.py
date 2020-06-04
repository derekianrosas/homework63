
#specialized version of classes
class User:
	def __init__(self, email, first_name, last_name):
		self.email = email
		self.first_name = first_name
		self.last_name = last_name
	def greeting(self):
		return f'Hi {self.first_name} {self.last_name}'

# IS THIS NEW ELEMENT  is it a type of one of the other classes that you already have, User is a strict high level class
class AdminUser(User):
	def active_users(self):
		return '500'


tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'HUdgens')

kristine = User('kristine@devcamp.com', 'Kristine', 'hudgens')

print(tiffany.active_users())
print(tiffany.greeting())
