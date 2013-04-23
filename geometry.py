from utils import iPrint as iPrint
from utils import incWhitespace
from utils import decWhitespace

import baseDescribable

class Cube (baseDescribable.Describable):
	def __init__(self):
		incWhitespace()
		iPrint("Initiating Cube...", True)
		baseDescribable.Describable.__init__(self)
		# Formed of six faces/sides
		totalSides = 6
		self.components["surface"] = [Surface() for i in range(totalSides)]
		decWhitespace()
		 
# An area with attributes
class Surface (baseDescribable.Describable):
	def __init__(self):
		incWhitespace()		
		iPrint("Initiating Surface...", True)
		baseDescribable.Describable.__init__(self)
		decWhitespace()
		
		

