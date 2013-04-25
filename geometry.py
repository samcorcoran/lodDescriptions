from utils import iPrint
from utils import incWhitespace
from utils import decWhitespace
from utils import wsWrapper

import baseDescribable

import random

# temp import:
import creatures

class Cube (baseDescribable.Describable):
	def __init__(self):
		#iPrint("Initiating Cube...", True)
		wsWrapper(baseDescribable.Describable.__init__, [self])
		# Formed of six faces/sides
		totalSides = 6
		self.components["surface"] = [Surface() for i in range(totalSides)]
		 
# An area with attributes
class Surface (baseDescribable.Describable):
	def __init__(self):
		#iPrint("Initiating Surface...", True)
		wsWrapper(baseDescribable.Describable.__init__, [self])

                # Added colour features
                newColours = random.choice([[], ['red'], ['blue'], ['green'], ['yellow'], ['black']])
                self.addColours(newColours)

		# Test components
		# Formed of peasants
		totalUnits = 20
		self.components["peasants"] = [creatures.Peasant() for i in range(totalUnits)]
		

