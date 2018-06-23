import sys

class Player():
	def __init__(self, id, tools):
		self.id = id
		self._tools = tools
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
		self._tools.write("gai #" + self.id)
		cmd = self._tools.readTh.get_command()
		try:
			if (cmd != "ko"):
				cmd = cmd.split(' ')[1:]
			self.team = cmd[0]
		except:
			print("Error on buid Team", file = sys.stderr)

	def _getPose(self):
		self._tools.write("ppo #" + self.id)
		cmd = self._tools.readTh.get_command()
		try:
			if (cmd != "ko"):
				cmd = cmd.split(' ')[2:]
			self.x = int(cmd[0])
			self.y = int(cmd[1])
			self.o = int(cmd[2])
			if self.x != self.oldX or self.y != self.oldY:
				moving = True
			else:
				moving  = False
		except:
			print("Error on buid Pos", file=sys.stderr)

	def _getBag(self):
		self._tools.write("pin #" + self.id)
		cmd = self._tools.readTh.get_command()
		try:
			if (cmd != "ko"):
				cmd = cmd.split(' ')[4:]
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
		cmd = self._tools.readTh.get_command()
		try:
			if (cmd != "ko"):
				cmd = cmd.split(' ')[2:]
		
			self.level = int(cmd[0])
		except:
			print("Error on buid Level", file=sys.stderr)
