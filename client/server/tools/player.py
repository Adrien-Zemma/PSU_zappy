import sys

class Player():
	def __init__(self, id, tools):
		self.id = id
		self._tools = tools
		self.x = 0
		self.y = 0
		self.o = 1

		self._getTeam()
		self._getPose()
		self._getBag()
		self._getLevel()
		self.oldX = 0
		self.oldY = 0
		self.frame = 0
		self.speak = False
		self.magic = False
		self.moving = False
		self.pushing = False

	def update(self):
		self._getTeam()
		self._getPose()
		self._getBag()
		self._getLevel()


	def _getTeam(self):
		self._tools.write("gpt #" + self.id)
	
	def setTeam(self, cmd):
		try:
			self.team = cmd[0]
		except:
			print("Error on buid Team", file=sys.stderr)

	def _getPose(self):
		self._tools.write("ppo #" + self.id)
		
	def setPose(self, cmd):
		try:
			self.x = int(cmd[0])
			self.y = int(cmd[1])
			self.o = int(cmd[2])
			if self.x != self.oldX or self.y != self.oldY:
				self.oldX = self.x
				self.oldY = self.y
				self.moving = True
			else:
				self.moving = False
		except:
			print("Error on buid Pos", file=sys.stderr)

	def _getBag(self):
		self._tools.write("pin #" + self.id)
		
	def setBag(self, cmd):
		try:
			self.bag = {
				"food": int(cmd[0]),
				"linemate": int(cmd[1]),
				"deraumere": int(cmd[2]),
				"sibur": int(cmd[3]),
				"mendiane": int(cmd[4]),
				"phiras": int(cmd[5]),
				"thystame": int(cmd[6]),
			}
		except:
			print("Error on buid Bag", file=sys.stderr)

	def _getLevel(self):
		self._tools.write("plv #" + self.id)
		
	def setLevel(self, cmd):
		try:
			self.level = int(cmd[0])
		except:
			print("Error on buid Level", file=sys.stderr)
