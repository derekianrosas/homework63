#multiple conditions in the prograsm
# username = ''
#email = 'jon@snow.com'
#password = 'thenorth'

#and operator
#if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
#	print('Access permitted')
#else:
#	print('You shall not pass!')

# and operator requires both statements to be true
# or operator is either or 

logged_in = True
standard_user = True

if logged_in and not standard_user:
	print('You can access the admin dashbpard')
else:
	print('You can only access the standard dashboard')