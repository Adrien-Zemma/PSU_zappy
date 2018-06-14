import threading
import sys

from .Server import Server
from .Threads import ThreadRead

class GraphicalInterface(Server, threading.Thread):
	def __init__(self, port, ip="localhost"):
		super().__init__(port, ip)
		threading.Thread.__init__(self)
		self.readTh.start()
		self.x = None
		self.y = None
		self.manageConnection()

	def manageConnection(self):
		cmd = self.readTh.get_command()
		if cmd == "WELCOME":
			self.write("team graphique")
			cmd = self.readTh.get_command().split(' ')
			self.x = int(cmd[0])
			self.y = int(cmd[1])
			print("Setted coords")

	def run(self):
		print(self.get_map())
		self.readTh.loop = False
		self.readTh.join()

	def get_map_size(self):
        	self.write("msz")
        	cmd = self.readTh.get_command().split(' ')[1:]
        	return cmd

	def get_map(self):
		m = []
		print("Asking to write")
		self.write("mct")
		for _ in range(self.y):
			line = []
			for _ in range(self.x):
				cmd = self.readTh.get_command(True, None).split(' ')[3:]
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
		self.write("tna")
		cmd = self.readTh.get_command()
		while cmd is not None:
			try:
				names.append(cmd.split(' ')[1])
			except IndexError:
				print("Error while creating team names", file=sys.stderr)

			cmd = self.readTh.get_command()
		return names
	
	def get_tile(self, x:str, y:str):
		self.write("bct " + str(x) + " " + str(y))
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