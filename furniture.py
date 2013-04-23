from utils import iPrint as iPrint
from utils import incWhitespace
from utils import decWhitespace

import baseDescribable

class Seat (baseDescribable.Construction):
	def __init__(self):
		incWhitespace()
		iPrint("Initiating Seat...", True)
		baseDescribable.Construction.__init__(self)
		decWhitespace
	
class Chair (Seat):
	def __init__(self):		
		incWhitespace()
		iPrint("Initiating Chair...", True)
		Seat.__init__(self)
		decWhitespace()

class Stool (Seat):
	def __init__(self):		
		incWhitespace()
		iPrint("Initiating Stool...", True)
		Seat.__init__(self)
		decWhitespace()


class Bench (Seat):
	def __init__(self):
		incWhitespace()
		iPrint("Initiating Bench...", True)
		Seat.__init__(self)
		decWhitespace()


