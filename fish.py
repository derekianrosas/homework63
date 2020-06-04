# Parent class
class Fish: 
  def __init__(self, first_name,
                last_name="fish",
                skeleton="bone",
                eyelids="false"
                ) 
     self.first_name = first_name
    self.last_name = last_name
    self.skeleton = skeleton
    self.eyelids = eyelids

  def swim(self):
    print("Swim forwards")

  def swim_backwards(self):
    print("Swim backwards")


#Show inheritance. Has class methods from parent 
class Trout(Fish):
  pass

bob = Trout("Bob")
print(bob.first_name)
print(bob.last_name)
print(bob.first_name + " " + bob.last_name)
print(bob.eyelids)
bob.swim()


# Child class with its own class method
class Clownfish(Fish):
  def live_with_anemone(self):
    print("The clownfish is coexisting with sea anemone")

casey = Clownfish("Casey")
print(casey.first_name + " " + casey.last_name)
casey.swim()
casey.live_with_anemone()


# bob.live_with_anemone() #Will recieve a no attribute error as live_with_anemone() belongs to the Clownfish class and not to the Trout class. 
class Shark(Fish):
  #Override constructor and swim_backwards methods, but not swim method from parent. 
  def __init__(self, first_name, last_name="Shark",
               skeleton="cartilage", eyelids=True):
    self.first_name = first_name
    self.last_name = last_name
    self.skeleton = skeleton
    self.eyelids = eyelids

  def swim_backwards(self):
    print("The shark cannot swim backwards, but can sink backwards.")

sammy = Shark("Sammy")
print(sammy.first_name + " " + sammy.last_name)
sammy.swim()
sammy.swim_backwards()
print(sammy.eyelids)
print(sammy.skeleton)


# The super function
class NewTrout(Fish):
  def __init__(self, water = "freshwater"):
    self.water = water
    super().__init__(self)

terry = NewTrout()
# Initialize first name
terry.first_name = "Terry"
#Use parent __init__() through super()
print(terry.first_name + " " + terry.last_name)
print(terry.eyelids)
Use child __init__() override
print(terry.water)
Use parent swim() method
terry.swim()

# Multiple inheritance 
class Coral:
  def community(self):
    print("Coral lives in a community.")

class Anemone:
  def protect_clownfish(self):
    print("The anemone is protecting the clownfish.")

class CoralReef(Coral, Anemone):
  pass

# great_barrier has access to methods in both parent classes
great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clownfish()