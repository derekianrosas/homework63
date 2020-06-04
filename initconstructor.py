#using class construction to set up blueprints for a function or as a function
class Tournament:
  def __init__(self, sign_up, character, tier):
    self.sign_up = sign_up
    self._character = character
    self.tier = tier
  
  def signupsheet(self):
    return f"Good luck {self.sign_up}!\n Your choice {self._character} is considered {self.tier} tier"
  @property
  def character(self):
  	return self._character
  @character.setter
  def character(self, character):
  	self._character = character
  
derek_signup = Tournament('Derek', 'Duckhunt', 'low')
print(derek_signup.signupsheet())
#print(derek_signup.character) #how to get certain data from a class
derek_signup.character = 'Little Mac' #how to set an attribute after its been established
print(derek_signup.character)

#property decorator where it can limit access for data
#depending on what you want people to see or overide