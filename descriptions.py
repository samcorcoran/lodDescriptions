import utils
from utils import iPrint
from utils import wsWrapper
import baseDescribable
import geometry
import furniture
import anatomy
import creatures

global whitespace

iPrint("\nLet's Describe Something!\n", True)

print("Creating a cube...")
box = geometry.Cube()
box.setNoun("box")
box.addColours(["red", "orange"])
box.describe()
#wsWrapper(box.printComponentTree)

print("Creating a rabbit...")
rabbit = creatures.Creature()
rabbit.setNoun("rabbit")
rabbit.addColours(["brown"])
rabbit.describe()

print("Creating a humanoid...")
percy = creatures.Humanoid()
percy.setNoun("human")
percy.setName("percy")
percy.addColours(["pink"])
percy.describe()

# Sentence building tests
noun = "turkey"
tNum = 1
for tNum in range(0,12):
        print("There "+utils.isOrAre(tNum)+" "+utils.intToWord(tNum)+" "+utils.pluralise(noun, tNum)+" on my lawn.")
