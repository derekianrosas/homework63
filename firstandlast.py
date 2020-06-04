def remove_first_and_last(list_to_clean):
	for items in list_to_clean:
		print(list_to_clean[1:-1])


dirt_list = ['remove', 'keep', 'me', 'destroy']
bigger_dirtier_list = ['remove', 'giant', 'dirty', 'nasty', 'remove']
remove_first_and_last(dirt_list)
remove_first_and_last(bigger_dirtier_list)
