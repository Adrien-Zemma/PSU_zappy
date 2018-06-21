import threading

from .IAServer import IAServer
from .incantationRequirements import incantationRequirements

class IA(threading.Thread):
	def __init__(self, team, port, ip):
		threading.Thread.__init__(self)
		self.server = IAServer(team, port, ip)

	def run(self):
		while True:
			ret = self.server.look()
			if ret[0]["food"] > 0:
				print("taking food!")
				self.server.take("food")
			ret = self.server.forward()
			if ret != "ok":
				print("Can't move forward")
				exit(84)
			else:
				print("Moving forward !")
