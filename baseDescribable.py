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
		# A dictionary holding functions used in describing a the object
		self.descriptionFunctions = dict()
		self.addDescriptionFunctions()
		self.noun = str(type(self).__name__)
		self.colours = []
		self.materials = []
		self.components = dict()
		decWhitespace()
	
	def setNoun(self, objectName):
		self.noun = objectName
				
	# Prompts describable to adopt new colours
	def addColours(self, newColour):
		self.colours += newColour
	
	# Prompts describable to adopt new colours
	def addMaterials(self, newMaterial):
		self.material = newMaterial
	
	
	# Print a description of this 
	def describe(self, firstCall = True):
		# Begin a traversal through the sub-objects for this object
		if firstCall:
			iPrint("Describing self...", True)
		description = ""
		for func in descriptionFunctions:
			descrption += func()
		# Describe components 
		#iPrint("Total component types: " + str(len(self.components.keys())), True)
		for componentType, componentList in self.components.items():
			#print("Component '" + str(componentType) + "' has "+ str(len(componentList)) +" "+ str(type(componentList[0])) +" objects.")
			for component in componentList:
				description += component.describe()
				
		if firstCall:
			iPrint(description)
			iPrint("End of description \n")
		else:
			return description
		
	
	def initialDescription(self):
		description = "This is a "+self.noun
		
	
	# Puts the object's name into a string for sentence incorporation, if it exists
	def describeName(self):
		if not self.name:
			preVerbs = ['called', 'named']
			return random.choice(preVerbs) + " " + self.name 
		return ""
		
	def printComponentTree(self, firstCall = True):
		# If function was invoked on current object, print initial message
		if firstCall:
			print("\nPrinting '"+self.noun+"' component tree:")
		iPrint(type(self), True, "|", "-> ")
		for componentType, componentList in self.components.items():
			for component in componentList:
				# Pass False as argument to 
				wsWrapper(component.printComponentTree, [False])
		if firstCall:
			print("End of component tree.\n")
		# Reset any whitespace changes occuring here or lower in the tree


# A describle thing that was built by someone
class Construction(Describable):
	def __init__(self):
		Describable.__init__(self)
		iPrint("Initiating Construction...")
