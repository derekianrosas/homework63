def fizz_buzzer(max_num):
	fizz_buzz_container = []
	for num in range(1, max_num + 1):
		if num % 3 and num % 5:
			fizz_buzz_container.append('fizz buzz')
		elif num % 3:
			fizz_buzz_container.append('fizz')
		elif num % 5:
			fizz_buzz_container.append('buzz')
		return fizz_buzz_container

print(fizz_buzzer(100)) 





