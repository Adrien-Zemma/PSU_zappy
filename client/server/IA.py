import threading

from .Server import Server


class Ia(Server, threading.Thread):
	def __init__(self, team, port, ip="localhost"):
		super().__init__(port, ip)
		threading.Thread.__init__(self)
		self.readTh.start()
		self.team = team
		self.team_id = None
		self.map_size = None
		self.orientation = 0
		self.manageConnection()

	def manageConnection(self):
		cmd = self.readTh.get_command()
		if cmd == "WELCOME":
			self.write("team " + self.team)
			self.team_id = self.readTh.get_command()
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

	def run(self):
		print("Hi IA")
