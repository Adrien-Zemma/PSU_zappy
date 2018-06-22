import threading

from .IAServer import IAServer
from .incantationRequirements import incantationRequirements

class IA(threading.Thread):
	def __init__(self, team, port, ip):
		threading.Thread.__init__(self)
		self.server = IAServer(team, port, ip)
		self.daemon = True
		self.level = 1
		self.inventory = {
			"linemate": 0,
			"deraumere": 0,
			"sibur": 0,
			"mendiane": 0,
			"phiras": 0,
			"thystame": 0
		}

	def run(self):
		while True:
			self.lookAndTake()
			self.server.forward()

	def lookAndTake(self):
		ret = self.server.look()
		if ret[0]["food"] > 0:
			self.takeN("food", ret[0]["food"])
		self.takeN("linemate", incantationRequirements[self.level - 1]["linemate"] - self.inventory["linemate"] - incantationRequirements[self.level - 1]["linemate"] - ret[0]["linemate"])
		#self.takeN("linemate", 5)

	def takeN(self, object, n):
		if n < 0:
			return
		for i in range(n):
			ret = self.server.take(object)
			if ret == "ko":
				return
