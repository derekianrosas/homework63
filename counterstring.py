string = 'Hello there'
char_count = {}

for letter in string:
	if letter in char_count.keys():
	 char_count[letter] +=1
	else:
	 char_count[letter] = 1


print(char_count)