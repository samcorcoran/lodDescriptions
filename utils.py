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
