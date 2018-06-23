import sys
from .Server import Server

class IAServer(Server):
	def __init__(self, team, port, ip):
		super().__init__(port, ip)
		self.readTh.start()
		self.team = team
		self.teamId = None
		self.mapSize = None
		self.manageConnection()

	def manageConnection(self):
		cmd = self.readTh.get_command()
		if cmd == "WELCOME":
			self.write(self.team)
			self.teamId = self.readTh.get_command()
			if self.teamId == "ko":
				print("Invalid team name")
				exit(84)
			cmd = self.readTh.get_command().split(' ')
			self.mapSize = (int(cmd[0]), int(cmd[1]))

	def checkCmd(self:object, cmd:str):
		if cmd == "dead":
			exit(0)
		return cmd

	def forward(self:object):
		self.write("Forward")
		return self.checkCmd(self.readTh.get_command())

	def left(self:object):
		self.write("Left")
		return self.checkCmd(self.readTh.get_command())

	def right(self:object):
		self.write("Right")
		return self.checkCmd(self.readTh.get_command())

	def look(self:object):
		self.write("Look")
		ret = self.checkCmd(self.readTh.get_command())
		datas = list()
		ret = ret[1:-2]
		ret = "".join(ret.split())
		for tile in ret.split(','):
			datas.append({
				"food": tile.count("food"),
				"linemate": tile.count("linemate"),
				"deraumere": tile.count("deraumere"),
				"sibur": tile.count("sibur"),
				"mendiane": tile.count("mendiane"),
				"phiras": tile.count("phiras"),
				"thystame": tile.count("thystame"),
				"player": tile.count("player")
			})
		return datas

	def inventory(self:object):
		self.write("Inventory")
		ret = self.checkCmd(self.readTh.get_command())
		data = dict()
		ret = ret[1:-1]
		for tile in ret.split(','):
			cmd = tile.split(' ')
			try:
				if len(cmd) == 3:
					data[cmd[1]] = int(cmd[2])
				elif len(cmd) == 2:
					data[cmd[0]] = int(cmd[1])
			except (KeyError, IndexError):
				print("Error while recepting inventory", file=sys.stderr)
				exit(84)
		return data

	def broadcast(self:object, msg:str):
		self.write("Broadcast " + msg)
		return self.checkCmd(self.readTh.get_command())

	def connectNbr(self:object):
		self.write("Connect_nbr")
		ret = self.checkCmd(self.readTh.get_command())
		return ret

	def fork(self:object):
		self.write("Fork")
		return self.checkCmd(self.readTh.get_command())

	def eject(self:object):
		self.write("Eject")
		return self.checkCmd(self.readTh.get_command())

	def take(self:object, object:str):
		self.write("Take " + object)
		return self.checkCmd(self.readTh.get_command())

	def set(self:object, object:str):
		self.write("Set " + object)
		return self.checkCmd(self.readTh.get_command())

	def incantation(self:object):
		self.write("Incantation")
		return self.checkCmd(self.readTh.get_command())
