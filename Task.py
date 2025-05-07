class superhero :
	def __init__(self, name):
		self.name = name
	def setName(self, name):
		self.name = name
	def printName(self):
		print(self.name)

BatMan = superhero("BatMan")
BatMan.printName()
