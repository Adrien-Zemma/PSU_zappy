import threading

from .IAServer import IAServer
from .incantationRequirements import incantationRequirements
from .utils import map
import queue
import sys

class IA(threading.Thread):
	def __init__(self, team, port, ip):
		threading.Thread.__init__(self)
		self.server = IAServer(team, port, ip)
		self.daemon = True
		self.level = 0
		self.pos = [0, 0]
		self.dir = 0
		self.look = self.server.look()
		self.state = "idle"
		self.inventory = {
			"food": 0,
			"linemate": 0,
			"deraumere": 0,
			"sibur": 0,
			"mendiane": 0,
			"phiras": 0,
			"thystame": 0
		}
		self.updateInventory()

	def run(self):
		while True:
			self.updateInventory()
			if self.state == "idle":
				self.idle()
				if self.inventory["food"] > 50 and self.checkIncantation() == True:
					self.state = "incanting"
			elif self.state == "incanting":
				if self.inventory["food"] < 10:
					self.state = "idle"
				self.incantation()
			if self.server.level != self.level:
				self.level = self.server.level
				self.state == "idle"
				print("Level " + str(self.level) + "!")

	def idle(self):
		if self.pos[0] == self.server.mapSize[0] - 1:
			self.left()
			self.forward()
			self.left()
		elif self.pos[0] == 0:
			self.right()
			self.forward()
			self.right()
		self.forward()

	def findPlayer(self):
		try:
			broadcast = self.server.broadcasts.get(True, 0.1)
			self.server.broadcasts.task_done()
		except queue.Empty:
			broadcast = None
		if broadcast is not None:
			begin = broadcast.split(' ')
			if len(begin) < 2:
				return False
			begin = begin[1].split(',')
			self.follow(int(begin[0]))
			return True
		return False

	def follow(self, direction):
		if direction <= 0 or direction > 8:
			return
		r = (self.server.mapSize[0] + self.server.mapSize[1]) / 4
		for i in range(int(r)):
			if self.look[0]["player"] >= 1:
				return
			if direction == 1:
				self.forward();
			elif direction == 2:
				self.forward()
				self.left()
				self.forward()
				self.right()
			elif direction == 3:
				self.left()
				self.forward()
				direction = 1
			elif direction == 4:
				self.left()
				self.forward()
				self.left()
				self.forward()
				direction = 8
			elif direction == 5:
				self.left()
				self.left()
				self.forward()
				direction = 1
			elif direction == 6:
				self.right()
				self.forward()
				self.right()
				self.forward()
				direction = 2
			elif direction == 7:
				self.right()
				self.forward()
				direction = 1
			elif direction == 8:
				self.forward()
				self.right()
				self.forward()
				self.left()

	def checkTileIncantation(self):
		if (self.look[0]["linemate"] >= incantationRequirements[self.level - 1]["linemate"]
		and self.look[0]["deraumere"] >= incantationRequirements[self.level - 1]["deraumere"]
		and self.look[0]["sibur"] >= incantationRequirements[self.level - 1]["sibur"]
		and self.look[0]["mendiane"] >= incantationRequirements[self.level - 1]["mendiane"]
		and self.look[0]["phiras"] >= incantationRequirements[self.level - 1]["phiras"]
		and self.look[0]["thystame"] >= incantationRequirements[self.level - 1]["thystame"]):
			return True
		return False

	def checkIncantation(self):
		if (self.inventory["linemate"] + self.look[0]["linemate"] >= incantationRequirements[self.level - 1]["linemate"]
		and self.inventory["deraumere"] + self.look[0]["deraumere"] >= incantationRequirements[self.level - 1]["deraumere"]
		and self.inventory["sibur"] + self.look[0]["sibur"] >= incantationRequirements[self.level - 1]["sibur"]
		and self.inventory["mendiane"] + self.look[0]["mendiane"] >= incantationRequirements[self.level - 1]["mendiane"]
		and self.inventory["phiras"] + self.look[0]["phiras"] >= incantationRequirements[self.level - 1]["phiras"]
		and self.inventory["thystame"] + self.look[0]["thystame"] >= incantationRequirements[self.level - 1]["thystame"]):
			return True
		return False

	def updateInventory(self):
		inventory = self.server.inventory()
		for k, i in inventory.items():
			try:
				self.inventory[k] = i
			except (KeyError):
				print("Key not in the dictionary", file=sys.stderr)

	def forward(self):
		cmd = self.server.forward()
		if cmd == "ko":
			return
		self.look = self.server.look()
		if self.look[0]["food"] > 0:
			self.takeN("food", self.look[0]["food"])
		if self.inventory["food"] > 20:
			self.lookAndTake()
		if self.dir == 0:
			self.pos[0] = map(self.server.mapSize[0], self.pos[0] - 1)
		elif self.dir == 1:
			self.pos[1] = map(self.server.mapSize[1], self.pos[1] + 1)
		elif self.dir == 2:
			self.pos[0] = map(self.server.mapSize[0], self.pos[0] + 1)
		elif self.dir == 3:
			self.pos[1] = map(self.server.mapSize[1], self.pos[1] - 1)

	def left(self):
		if self.server.left() == "ok":
			self.dir = map(4, self.dir - 1)

	def right(self):
		if self.server.right() == "ok":
			self.dir = map(4, self.dir + 1)

	def lookAndTake(self):
		if self.look[0]["food"] > 0:
			self.takeN("food", self.look[0]["food"])
		if self.checkTileIncantation() == True:
			return
		for k, _ in self.inventory.items():
			if k != "food":
				try:
					self.takeN(k, incantationRequirements[self.level - 1][k] - self.inventory[k])
				except (KeyError):
					print("Key not in the dictionary", file=sys.stderr)

	def takeN(self, object, n):
		if n < 0:
			return
		for i in range(n):
			ret = self.server.take(object)
			if ret == "ok":
				try:
					self.inventory[object] += 1
					self.look[0][object] -= 1
				except (KeyError):
					print("Key not in the dictionary", file=sys.stderr)
			else:
				return

	def incantation(self):
		try:
			if int(self.server.connectNbr()) > 0:
				self.server.fork()
		except (ValueError):
			pass
		if self.checkTileIncantation() == False and self.look[0]["player"] < incantationRequirements[self.level - 1]["player"]:
			if self.findPlayer() == False:
				self.idle()
				return
		self.look = self.server.look()
		if self.checkTileIncantation() == False:
			for k, _ in incantationRequirements[self.level - 1].items():
				if k != "player":
					for i in range(incantationRequirements[self.level - 1][k] - self.look[0][k]):
						self.server.set(k)
		if self.inventory["food"] < 20:
			self.lookAndTake()
			self.state = "idle"
		if incantationRequirements[self.level - 1]["player"] - self.look[0]["player"] > 0:
			self.server.broadcast("Come here to get level " + str(self.level + 1) + "\n")
		if self.server.incantation() == "ko":
			self.server.checkCmd(self.server.readTh.get_command())
