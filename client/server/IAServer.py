
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

	def right(self:object):
		self.write("Right")

	def left(self:object):
		self.write("Left")
