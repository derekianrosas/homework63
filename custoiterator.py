#iteration is lists dictionaries and tuples they are iterable, you need to implement your own iterations sometimes
#create a new class
class Lineup:
	def __init__(self, players):
		self.players = players
	def __iter__(self):
		self.n = 0
		return self
	
	def __next__(self):
		if self.n < (len(self.players) - 1):
			player = self.players[self.n]
			self.n += 1
			return player
		elif self.n == (len(self.players) - 1):
			player = self.players[self.n]
			self.n = 0
			return player

roster = [
  'Duckhunt',
  'Little Mac',
  'Corin',
  'Snake',
  'Fox',
  'Bowser',
  'Mario',
  'Luigi',
  'Falco'
]


smash_roster = Lineup(roster)
process = iter(smash_roster)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))