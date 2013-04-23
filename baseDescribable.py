from utils import iPrint
from utils import wsWrapper
from utils import incWhitespace
from utils import decWhitespace

import utils

# A describable thing
class Describable(object):
	# Physical appearance
	## Structure
	def __init__(self):
		incWhitespace()
		iPrint("Initiating Describable...", True)
		self.name = "defaultObjectName"
		self.colours = []
		self.materials = []
		self.components = dict()
		decWhitespace()
	
	def setName(self, objectName):
		self.name = objectName
		
	# Prompts describable to adopt new colours
	def addColours(self, newColour):
		self.colours += newColour
	
	# Prompts describable to adopt new colours
	def addMaterials(self, newMaterial):
		self.material = newMaterial
	
	# Print a description of this 
	def describe(self):
		# Begin a traversal through the sub-objects for this object
		iPrint("Describing self...", True)

		iPrint("Total component types: " + str(len(self.components.keys())), True)
		for componentType, componentList in self.components.items():
			print("Component '" + str(componentType) + "' has "+ str(len(componentList)) +" "+ str(type(componentList[0])) +" objects.")
			for component in componentList:
				component.describe()
		iPrint("End of description \n")
		#whitespace = oldWhitespace
		
	def printComponentTree(self, firstCall = True):
		#global whitespace
		#oldWhitespace = utils.whitespace
		# If function was invoked on current object, print initial message
		if firstCall:
			print("\nPrinting '"+self.name+"' component tree:")
			#utils.whitespace += 1
		#utils.whitespace += 1
		iPrint(type(self), True, "|", "-> ")
		for componentType, componentList in self.components.items():
			for component in componentList:
				# Pass False as argument to 
				wsWrapper(component.printComponentTree, [False])
		if firstCall:
			print("End of component tree.\n")
		# Reset any whitespace changes occuring here or lower in the tree
		#utils.whitespace = oldWhitespace


# A describle thing that was built by someone
class Construction(Describable):
	def __init__(self):
		Describable.__init__(self)
		iPrint("Initiating Construction...")
