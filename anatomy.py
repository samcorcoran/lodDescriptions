from utils import iPrint as iPrint
import baseDescribable

class Anatomic(baseDescribable.Describable):
	def __init__(self):
		baseDescribable.Describable.__init__(self)
		print("Initiating Anatomic...")

class Limb(Anatomic):
	def __init__(self):
		Anatomic.__init__(self)
		print("Initiating Limb...")

class Arm(Limb):
	# Formed of shoulders, upperArm, elbow, forearm, hand
	def __init__(self):
		Limb.__init__(self)
		print("Initiating Arm...")

class Hand(Limb):
	# Formed of wrist, palm, backOfHand and digits
	def __init__(self):
		Limb.__init__(self)
		print("Initiating Arm...")

class Leg(Limb):
	def __init__(self):
		Limb.__init__(self)
		print("Initiating Leg...")

class Head(Anatomic):
	# Formed of face and scalp
	def __init__(self):
		Anatomic.__init__(self)
		print("Initiating Head...")
		
class Neck(Anatomic):
	# Formed of throat and back of neck
	def __init__(self):
		Anatomic.__init__(self)
		print("Initiating Neck...")

class Back(Anatomic):
	def __init__(self):
		Anatomic.__init__(self)
		print("Initiating Back...")

class Torso(Anatomic):
	# Formed of a thorax, abdomen and back
	def __init__(self):
		Anatomic.__init__(self)
		print("Initiating Torso...")
