import threading

from .IAServer import IAServer
from .incantationRequirements import incantationRequirements
from .utils import map
import os
import queue

class IA(threading.Thread):
	def __init__(self, team, port, ip):
		threading.Thread.__init__(self)
		self.server = IAServer(team, port, ip)
		self.daemon = True
		self.level = 1
		self.pos = [0, 0]
		self.dir = 0
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
			if self.checkIncantation() == True:
				self.incantation()
			self.level = self.server.level
			self.updateInventory()
			if self.inventory["food"] < 20 or self.findPlayer() == False:
				self.idle()
			self.lookAndTake()

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
			self.follow(int(begin[1]))
			return True
		return False

	def follow(self, direction):
		if direction <= 0 or direction > 8:
			return
		r = (self.server.mapSize[0] + self.server.mapSize[1]) / 4
		for i in range(r):
			ret = self.server.look()
			if ret[0]["food"] > 0:
				self.takeN("food", ret[0]["food"])
			if ret[0]["player"] >= 2:
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

	def checkIncantation(self):
		ret = self.server.look()
		if (self.inventory["linemate"] >= incantationRequirements[self.level - 1]["linemate"]
		and self.inventory["deraumere"] >= incantationRequirements[self.level - 1]["deraumere"]
		and self.inventory["sibur"] >= incantationRequirements[self.level - 1]["sibur"]
		and self.inventory["mendiane"] >= incantationRequirements[self.level - 1]["mendiane"]
		and self.inventory["phiras"] >= incantationRequirements[self.level - 1]["phiras"]
		and self.inventory["thystame"] >= incantationRequirements[self.level - 1]["thystame"]
		and self.inventory["food"] >= 15):
			return True
		return False

	def updateInventory(self):
		inventory = self.server.inventory()
		for k, i in inventory.items():
			self.inventory[k] = i

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
		if self.server.left() == "ok":
			self.dir = map(4, self.dir - 1)

	def right(self):
		if self.server.right() == "ok":
			self.dir = map(4, self.dir + 1)

	def lookAndTake(self):
		ret = self.server.look()
		if ret[0]["food"] > 0:
			self.takeN("food", ret[0]["food"])
		for k, _ in self.inventory.items():
			if k != "food":
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

	def incantation(self):
		ret = self.server.look()
		for k, _ in incantationRequirements[self.level - 1].items():
			if k != "player":
				for i in range(incantationRequirements[self.level - 1][k] - ret[0][k]):
					self.server.set(k)
		self.server.broadcast("Come here to get level " + str(self.level + 1) + "\n")
		if self.server.incantation() == "ko":
			if self.server.checkCmd(self.server.readTh.get_command()) == "ko":
				self.server.fork()
