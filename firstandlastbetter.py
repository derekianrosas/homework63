def remove_first_and_last(unclean_list):
	for item in unclean_list:
		del unclean_list[0]
		del unclean_list[-1]
		print(unclean_list)

dirty_list = ['dirty', 'keep', 'me', 'destroy']
remove_first_and_last(dirty_list)
