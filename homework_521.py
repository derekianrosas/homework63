class VideoGameTournament:
	def __init__(self, criteria):
		self._criteria = criteria
		
	def successful_signup(self):
		raise NotImplementedError("You need to fill this thing out brother")

	def __str__(self):
		return f"Good Luck, you're going to need it"
	def __repr__(self):
		return f'This is a blank form'

	@property
	def criteria(self):
		return self._criteria
	

class ContestantCharacter(VideoGameTournament):
	def successful_signup(self):
		if {self.criteria} == 'Ganondorf':
			print('Wow you are lame, pick someone else')
		else:
			print("Okay, I'll let it slide this time")
		return f"So, you chose {self.criteria}? I guess that's a decent choice"


class ContestantTier(VideoGameTournament):
	def successful_signup(self):
		return f"They might be considered {self.criteria} Tier but don't let that discourage you"


completed_form = [
	ContestantCharacter('Duck Hunt'),
	ContestantTier('Low')
]

second_form = [
	ContestantCharacter('Little Mac'),
	ContestantTier('Garbage')
]

third_form = [
	ContestantCharacter('Ganondorf'),
	ContestantTier('Slow')
]


for form in completed_form:
	print(form.successful_signup())

for form in second_form:
	print(form.successful_signup())

for form in third_form:
	print(form.successful_signup())

