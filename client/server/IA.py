import threading

from .IAServer import IAServer
from .incantationRequirements import incantationRequirements
from .utils import map

class IA(threading.Thread):
	def __init__(self, team, port, ip):
		threading.Thread.__init__(self)
		self.server = IAServer(team, port, ip)
		self.daemon = True
		self.level = 1
		self.pos = [0, 0]
		self.dir = 0
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
			self.inventory = self.server.inventory()
			self.lookAndTake()
			if self.pos[0] == self.server.mapSize[0] - 1:
				self.left()
				self.forward()
				self.left()
			elif self.pos[0] == 0:
				self.right()
				self.forward()
				self.right()
			self.forward()

	def forward(self):
		print("forward")
		cmd = self.server.forward()
		if cmd == "ko":
			return
		if self.dir == 0:
			self.pos[0] = map(self.server.mapSize[0], self.pos[0] - 1)
		elif self.dir == 1:
			self.pos[1] = map(self.server.mapSize[1], self.pos[1] + 1)
		elif self.dir == 2:
			self.pos[0] = map(self.server.mapSize[0], self.pos[0] + 1)
		elif self.dir == 3:
			self.pos[1] = map(self.server.mapSize[1], self.pos[1] - 1)

	def left(self):
		print("left")
		if self.server.left() == "ok":
			self.dir = map(4, self.dir - 1)

	def right(self):
		print("right")
		if self.server.right() == "ok":
			self.dir = map(4, self.dir + 1)

	def lookAndTake(self):
		ret = self.server.look()
		if ret[0]["food"] > 0:
			self.takeN("food", ret[0]["food"])
		for k, _ in self.inventory.items():
			self.takeN(k, incantationRequirements[self.level - 1][k] - self.inventory[k])

	def takeN(self, object, n):
		if n < 0:
			return
		for i in range(n):
			ret = self.server.take(object)
			if ret == "ok" and object != "food":
				self.inventory[object] += 1
			else:
				return
