from utils import iPrint
from utils import incWhitespace
from utils import decWhitespace
from utils import wsWrapper

import baseDescribable

class Cube (baseDescribable.Describable):
	def __init__(self):
		iPrint("Initiating Cube...", True)
		wsWrapper(baseDescribable.Describable.__init__, [self])
		# Formed of six faces/sides
		totalSides = 6
		self.components["surface"] = [Surface() for i in range(totalSides)]
		 
# An area with attributes
class Surface (baseDescribable.Describable):
	def __init__(self):
		iPrint("Initiating Surface...", True)
		wsWrapper(baseDescribable.Describable.__init__, [self])
		
		

