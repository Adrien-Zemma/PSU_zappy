import os
import sys
import random
import pygame
from .Commands import Commands
import threading
from .Server import Server
from .Threads import ThreadRead
from .window import Window
from .mapressources import MapRessources
from .tools import Tools
from .image import Images
from .player import Player
from .map import Map

class GraphicalInterface(Server, threading.Thread):
	def __init__(self, port=4242, ip="localhost"):
		super().__init__(port, ip)
		threading.Thread.__init__(self)
		self.readTh.start()
		random.seed()
		self.buidCommande()
		self.manageConnection()
		self.daemon = True
		pygame.init()
		self._clock = pygame.time.Clock()
		self._tools = Tools(self.write, self.readTh)
		self._window = Window(1080, 1920)
		self._window.setImages(Images())
		self.mapSize = self._tools.getMapSize()
		self._sizeX = self.mapSize[0]
		self._sizeY = self.mapSize[1]
		self._mapResources = MapRessources(
			x=self.mapSize[0],
			y=self.mapSize[0],
			sprite=self._window.getSpriteSize()
		)
		self._map = Map(
			x=self._sizeX,
			y=self._sizeY,
			tools=self._tools,
			set=self._mapResources
		)
		self._buildPlayer()
		
	def buidCommande(self):
		self._commands = {}
	
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
		pass

	def draw(self):
		self._window.draw(None)
		self._window.draw(self._map)

	def run(self):
		while(self._window.running()):
			self.getUnexpectCommande()
			self._map.update()
			for player in self._players:
				player.update()
			self.draw()
		pass
