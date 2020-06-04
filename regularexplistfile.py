#how to use regular expressions give you the ability to match files
import fnmatch
from fnmatch import fnmatchcase
import os

def list_files():
	for file in os.listdir('.'):#short for list directory '.' stays in the same directory
		if fnmatch.fnmatch(file, "*.txt"):
			print("Text Files: ", file) #duplication necessary
		if fnmatch.fnmatch(file, "*.py"):
			print("Py Files: ", file)
#list_files()


players = [
	"Jose Altuve 2B",
	"Carlos Correa SS",
	"Alex Bregman 3B",
	"Scooter Gennett 2B"

]

second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]

print("Players that play second base: ", second_base_players)