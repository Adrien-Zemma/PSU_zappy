import os
import sys
import random
import pygame
import threading
from .tools.map import Map
from .Server import Server
from .tools.tools import Tools
from .Commands import Commands
from .tools.image import Images
from .Threads import ThreadRead
from .tools.window import Window
from .tools.player import Player
from .tools.mapressources import MapRessources

class GraphicalInterface(Server, threading.Thread):
	def __init__(self, port=4242, ip="localhost"):
		super().__init__(port, ip)
		threading.Thread.__init__(self)
		self.readTh.start()
		random.seed()
		self.manageConnection()
		self.daemon = True
		pygame.init()
		self._tools = Tools(self.write, self.readTh)
		self._window = Window(1080, 1920)
		self._window.setImages(Images())
		self.mapSize = self._tools.getMapSize()
		self._sizeX = self.mapSize[0]
		self._sizeY = self.mapSize[1]
		self._listMagic = []
		self._mapResources = MapRessources(
			x = self.mapSize[0],
			y = self.mapSize[1],
			sprite = self._window.getSpriteSize()
		)
		self._map = Map(
			x = self._sizeX,
			y = self._sizeY,
			tools = self._tools,
			set = self._mapResources
		)
		self._buildPlayer()
		self.buidCommande()

	def playerConnection(self, cmd):
		cmd = cmd.split(' ')
		self._players.append(
			Player(
				cmd[1][1:],
				self._tools
			)
		)


	def managePlayer(self, cmd):
		cmd = cmd.split(' ')
		for player in self._players:
			if (player.id != cmd[1]):
				continue
			if (cmd[0] == "pin"):
				player.setBag(cmd[4:])
			if (cmd[0] == "ppo"):
				player.setPose(cmd[2:])
			if (cmd[0] == "plv"):
				player.setLevel(cmd[2:])
			if (cmd[0] == "gpt"):
				player.setTeam(cmd[2:])
			if (cmd[0] == "pex"):
				player.pushing = True
			if (cmd[0] == "pbc"):
				player.speak = True
			if (cmd[0] == "pdi"):
				player.alive = False

	def manageMagic(self, cmd):
		cmd = cmd.split(' ')
		if cmd[0] == "pic":
			self._listMagic.append((cmd[1], cmd[2]))
		else:
			try:
				self._listMagic.remove((cmd[1], cmd[2]))
			except:
				pass
		pass

	def buidCommande(self):
		cmd = {
			"bct": self._map.addTile,
			"pnw": self.playerConnection,
			"gpt": self.managePlayer,
			"ppo": self.managePlayer,
			"plv": self.managePlayer,
			"pin": self.managePlayer,
			"pdi": self.managePlayer,
			"pbc": self.managePlayer,
			"pex": self.managePlayer,
			"pic": self.manageMagic,
			"pie": self.manageMagic
		}
		self._commands = Commands(commands = cmd)

	def manageConnection(self):
		cmd = self.readTh.get_command()
		if cmd == "WELCOME":
			self.write("GRAPHIC")
			cmd = self.readTh.get_command().split(' ')[1:]
			self._sizeX = int(cmd[0])
			self._sizeY = int(cmd[1])
			print("Frequence: ", self.readTh.get_command().split(' ')[1:])
			cmd = self.readTh.get_command()
			while cmd is not None:
				self.teams.append(cmd.split(' ')[1:][0])
				cmd = self.readTh.get_command(True, timeout=0.1)
			print("Teams: ", self.teams)

	def _buildPlayer(self):
		self._players = []
		ids = self._tools.getAllId()
		for el in ids:
			self._players.append(
				Player(el, self._tools)
			)

	def getUnexpectCommande(self):
		while True:
			cmd = self._tools.readTh.get_command(True, 0.1)
			if (cmd is not None):
				self._commands.parse(cmd)
			else:
				break

	def draw(self):
		self._window.drawBack()
		self._window.drawField(int(self._sizeX), int(self._sizeY))
		self._window.drawMap(self._map)
		self._window.drawMagic(self._listMagic)
		for player in self._players:
			self._window.drawPlayer(player)
		self._window.drawHud(self._players)
		pygame.display.update()
		self._window.clock.tick(60)

	def updateMap(self):
		self._tools.write("mct")

	def updatePlayer(self):
		for player in self._players:
			player.update()

	def run(self):
		deltaTime = 0
		time = pygame.time.get_ticks()
		while(True):
			if self._window.running(deltaTime) == False:
				return
			self.updateMap()
			self.updatePlayer()
			self.getUnexpectCommande()
			for player in self._players:
				print(player.team)
			self._map.update()
			self.draw()
			t = pygame.time.get_ticks()
			deltaTime = (t - time) / 1000
			time = t
