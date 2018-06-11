import threading
import sys

from .Server import Server
from .Threads import ThreadRead

class GraphicalInterface(Server, threading.Thread):
	def __init__(self, port, ip="localhost"):
		super().__init__(port, ip)
		threading.Thread.__init__(self)
		self.readTh = ThreadRead(self._sock)
		self.readTh.start()
		self.manageConnection()
		self.x = None
		self.y = None

	def _write(self, msg):
		super(GraphicalInterface, self).write(msg)

	def manageConnection(self):
		cmd = self.readTh.get_command()
		if cmd == "WELCOME":
			print("Welcome from server")
			self._write("TEAM graphique")
			print("Team id:")
			print(self.readTh.get_command())
			print("Map size")
			cmd = self.readTh.get_command()
			print(cmd)
			self.x = cmd[0]
			self.y = cmd[1]
			print("Setted coords")

	def run(self):
		print("Hi UI")
		print("Map;")
		print(self.get_map())
		print("Teams:")
		print(self.teams_name())
		print(self.get_tile(0, 0))
		print(self.get_tile(1, 1))

	def get_map_size(self):
        	self._write("msz")
        	cmd = self.readTh.get_command().split(' ')[1:]
        	return cmd

	def get_map(self):
		m = []
		self._write("mct")
		for _ in range(self.y):
			line = []
			for _ in range(self.x):
				cmd = self.readTh.get_command().split(' ')[3:]
				try:
        	        		line.append({
        	                		"food": cmd[0],
        	                		"linemate": cmd[1],
        	                		"deraumere": cmd[2],
        	                		"sibur": cmd[3],
        	                		"mendiane": cmd[4],
        	                		"phiras": cmd[5],
        	                		"thystame": cmd[6],
        	        		})
				except IndexError:
					print("Error while creating line from construct map", file=sys.stderr)
					exit(84)
			m.append(line)
		return m

	def teams_name(self):
		names = []
		self._write("tna")
		cmd = self.readTh.get_command()
		while cmd is not None:
			try:
				names.append(cmd.split(' ')[1])
			except IndexError:
				print("Error while creating team names", file=sys.stderr)

			cmd = self.readTh.get_command()
		return names
	
	def get_tile(self, x:str, y:str):
		self._write("bct " + str(x) + " " + str(y))
		cmd = self.readTh.get_command().split(' ')[3:]
		try:
        	    	return {
				"food": cmd[0],
				"linemate": cmd[1],
				"deraumere": cmd[2],
				"sibur": cmd[3],
				"mendiane": cmd[4],
				"phiras": cmd[5],
				"thystame": cmd[6],
        		}
		except IndexError:
			print("Error while getting tile", file=sys.stderr)
			exit(84)