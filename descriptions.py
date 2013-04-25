import utils
from utils import iPrint
from utils import wsWrapper
from utils import incWhitespace
from utils import decWhitespace
import baseDescribable
import geometry
import furniture
import anatomy

global whitespace

iPrint("\nLet's Describe Something!\n", True)

class Creature (baseDescribable.Describable):
	# Physical appearance
	## Anatomy
	# Moods
	def __init__(self):
		iPrint("Initiating Creature...", True)
		# Call init for superclass describable, therefore inheriting attributes
		wsWrapper(baseDescribable.Describable.__init__, [self])
		self.name = ""
		
	def setName(self, creatureName):
		self.Name = creatureName


class Humanoid (Creature):
	# Physical appearance
	## Anatomy
	# Moods
	# Props
	# Aspirations
	# Possessions
	def __init__(self):
		iPrint("Initiating humanoid...", True)
		wsWrapper(Creature.__init__, [self])

# A peasant who will be described
class Peasant (Humanoid):
	def __init__(self):
		iPrint("Initiating peasant...", True)
		wsWrapper(Humanoid.__init__, [self])
		

print("Creating a cube...")
box = geometry.Cube()
box.setNoun("box")
box.addColours(["red", "orange"])
box.describe()
wsWrapper(box.printComponentTree)

print("Creating a rabbit...")
rabbit = Creature()
rabbit.setNoun("rabbit")
rabbit.addColours(["brown"])
rabbit.describe()

print("Creating a humanoid...")
percy = Humanoid()
percy.setNoun("human")
percy.setName("percy")
percy.addColours(["pink"])
percy.describe()
