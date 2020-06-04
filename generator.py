class InfiniteLineup:
	def __init__(self, players):
		self.players = players

	def lineup(self):
		lineup_max = len(self.players)
		idx = 0

		while True:
			if idx < lineup_max:
				yield self.players[idx]
			else:
				idx = 0
				yield self.players[idx]

			idx += 1

	def __repr_(self):
		return f'<InfiniteLineup({self.players})'
	def __str__(self):
		return f'InfiniteLineup with players: {self.players}'


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

full_lineup = InfiniteLineup(roster)
roster_lineup = full_lineup.lineup()
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(next(roster_lineup))
print(repr(roster_lineup))
print(str(roster_lineup))