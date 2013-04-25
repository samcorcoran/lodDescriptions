from utils import iPrint
from utils import wsWrapper
from utils import incWhitespace
from utils import decWhitespace

import utils

import random
import string

# A describable thing
class Describable(object):
	# Physical appearance
	## Structure
	
	def __init__(self):
		incWhitespace()
		#iPrint("Initiating Describable...", True)
		# A dictionary holding functions used in describing a the object
		self.descriptionFunctions = dict()
		self.addDescriptionFunctions()
		self.noun = str(type(self).__name__)
		self.gender = "neuter"
		self.colours = []
		self.materials = []
		self.components = dict()
		decWhitespace()
	
	def setNoun(self, objectName):
		self.noun = objectName
				
	# Prompts describable to adopt new colours
	def addColours(self, newColours):
                if newColours:
                        self.colours += newColours
	
	# Prompts describable to adopt new colours
	def addMaterials(self, newMaterial):
		self.material = newMaterial

        def addDescriptionFunctions(self):
                self.descriptionFunctions['initialDescription'] = self.initialDescription
	
	# Print a description of this 
	def describe(self, masterObject=None, firstCall = True):
		# Begin a traversal through the sub-objects for this object
		if firstCall:
                        masterObject = self
			iPrint("Describing self...", True)
			
		description = ""

                # Iterate through registered 'describe' functions and call each
		#for key, func in self.descriptionFunctions.items():
		#	description += str(func()) + ". "
		
                if firstCall:
                        description += self.initialDescription() + ". "
                        description += self.describeComponentOverview(True, masterObject)
                else:
                        if len(self.colours) > 0:
                                description += " is "
                                description += utils.listToCommaString(self.colours) + ". "
                        else:
                                description += random.choice([" has no colour" , " is colourless"]) + ". "
		
		# Describe components 
		for componentType, componentList in self.components.items():
                        componentCounter = 0
			for component in componentList:
                                if len(componentList) < 10:
                                        componentCounter += 1
                                        description += "The " + utils.intToOrdinalWord(componentCounter)
                                        #description += self.describeComponentOverview(False, masterObject)

                                        description += component.describe(masterObject, False)

		if firstCall:
			iPrint(description)
			iPrint("End of description \n")
		else:
			return description
		
	
	def initialDescription(self):
                description = ""
		if self.noun:
                        description = "This is a "+self.noun
		return description

	# Puts the object's name into a string for sentence incorporation, if it exists
	def describeName(self):
		if not self.name:
			preVerbs = ['called', 'named']
			return random.choice(preVerbs) + " " + self.name 
		return ""
	
        def describeComponentOverview(self, doFullSentence, masterPronoun):
                description = ""
                # May only describe components if they exist
                if not len(self.components.keys()) == 0:
                        if doFullSentence:
                                # Begin with pronoun
                                description = utils.getPronoun(self.gender, 'subject') + " "
                        else:
                                # Full sentence not required
                                description += random.choice(", and ", ", which ")
                        # Describe possession
                        description += random.choice(["is made up of", "is composed of", "has"]) + " "
                        # Track components listed so last 
                        keyCount = 0
                        for key, value in self.components.items():
                                keyCount += 1
                                description += utils.intToWord(len(value)) + " " + utils.pluralise(str(type(value[0]).__name__), len(value))
                                if len(self.components.keys()) > 1 and keyCount+1 == len(self.components.keys()):
                                        # insert a connector before last component
                                        description += " and "
                                elif not keyCount == len(self.components.keys()):
                                        # comma separate components
                                        description += ", "
                                description += ". "
                        if doFullSentence:
                                description = string.capitalize(description)
                return description
                                
                
                
                
	def printComponentTree(self, firstCall = True):
		# If function was invoked on current object, print initial message
		if firstCall:
			print("\nPrinting '"+self.noun+"' component tree:")
		iPrint(type(self).__name__, True, "|", "-> ")
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
