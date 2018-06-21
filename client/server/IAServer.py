
from .Server import Server

class IAServer(Server):
	def __init__(self, team, port, ip):
		super().__init__(port, ip)
		self.readTh.start()
		self.team = team
		self.team_id = None
		self.map_size = None
		self.orientation = 0
		self.manageConnection()

	def manageConnection(self):
		cmd = self.readTh.get_command()
		if cmd == "WELCOME":
			self.write(self.team)
			self.team_id = self.readTh.get_command()
			if self.team_id == "ko":
				print("Invalid team name")
				exit(84)
			cmd = self.readTh.get_command().split(' ')
			self.map_size = (cmd[0], cmd[1])
			print("Setted coords")
			print(self.map_size)

	def forward(self:object):
		self.write("Forward")
		print("Forward", flush=True)
		return self.readTh.get_command()

	def right(self:object):
		self.write("Right")
		return self.readTh.get_command()

	def left(self:object):
		self.write("Left")
		return self.readTh.get_command()

	def look(self:object):
		self.write("Look")
		ret = self.readTh.get_command()
		datas = list()
		ret = ret[1:-2]
		ret = "".join(ret.split())
		for tile in ret.split(','):
			datas.append({
				"linemate": tile.count("linemate"),
				"deraumere": tile.count("deraumere"),
				"sibur": tile.count("sibur"),
				"mendiane": tile.count("mendiane"),
				"phiras": tile.count("phiras"),
				"thystame": tile.count("thystame"),
				"player": tile.count("player")
			})
		print(datas, flush=True)
		return datas

	def inventory(self:object):
		self.write("Inventory")
		ret = self.readTh.get_command()
		return ret

	def broadcast(self:object, msg:str):
		self.write("Broadcast " + msg)
		return self.readTh.get_command()

	def connectNbr(self:object):
		self.write("Connect_nbr")
		ret = self.readTh.get_command()
		return ret

	def fork(self:object):
		self.write("Fork")
		return self.readTh.get_command()

	def eject(self:object):
		self.write("Eject")
		return self.readTh.get_command()

	def take(self:object, object:str):
		self.write("Take " + object)
		return self.readTh.get_command()

	def set(self:object, object:str):
		self.write("Set " + object)
		return self.readTh.get_command()

	def incantation(self:object):
		self.write("Incantation")
		return self.readTh.get_command()
