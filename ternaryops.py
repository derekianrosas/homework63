#you need to be careful with how you implement them, this adds complexity to code
#websapp needs authorization
role = 'admin'

#auth = 'can access' if role == 'admin' else 'cannot access'
#print(auth)
#reorganizes what a conditional does for us
if role == 'admin':
	auth = 'can access'
else:
	auth = 'cannot access'

print(auth)