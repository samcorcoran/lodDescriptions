import random

# A global whitespace counter for facilitating hierarchical indenting
whitespace = 0

# Overload print function for auto-indenting
def iPrint(payload = "", doIndent = False, indentToken = " ", indentEndToken = " "):
	global whitespace
	output = ""
	if doIndent and whitespace > 0:
		# Indent using given tokens
		output = str(indentToken * (whitespace-1)) + str(indentEndToken)
	output += str(payload)
	print(output)

def incWhitespace():
	global whitespace
	whitespace += 1
	
def decWhitespace():
	global whitespace
	whitespace -= 1
	
# A wrapper function that lets a function be called, with a list of args, and whitespacing is handled automatically
def wsWrapper(func, args = []):
	incWhitespace()
	output = func(*args)
	decWhitespace()
	return output

# Converts numbers to their cardinal words
def intToWord(numeric):
	wordNumbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
	if numeric <= len(wordNumbers)-1:
		return wordNumbers[numeric]
	return random.choice(['lots of', 'many'])

# Converts numbers to their ordinal words
def intToOrdinalWord(numeric):
	wordNumbers = ['zero', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
	if numeric <= len(wordNumbers)-1:
		return wordNumbers[numeric]
	return random.choice(['lots of', 'many'])

def pluralise(word, count):
	if count > 1 or count == 0:
		word += 's'
	return word

def isOrAre(count):
	# Count indicates how many of the thing there is/are
	if count > 1 or count == 0:
		return 'are'
	return 'is'

# Uses a gender and form to determine the correct pronoun to be used
def getPronoun(gender = "neuter", form = "subject"):
	pronouns = dict()
	pronouns['masculine'] = {'subject':'he', 'object':'him', 'possessiveDeterminer':'his'}
	pronouns['feminine'] = {'subject':'she', 'object':'her', 'possessiveDeterminer':'her'}
	pronouns['neuter'] = {'subject':'it', 'object':'it', 'possessiveDeterminer':'its'}
	pronouns['epicene'] = {'subject':'they', 'object':'them', 'possessiveDeterminer':'their'}
	pronouns['plural'] = {'subject':'they', 'object':'them', 'possessiveDeterminer':'their'}
	
#	return random.choice(pronouns[gender][form])
	return pronouns[gender][form]
