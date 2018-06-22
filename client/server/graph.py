import pygame
import os
from .window import Window
from .mapressources import MapRessources
from .tools import Tools
from .image import Images
from .player import Player
from .map import Map

def write():
	pass

def readTh():
	pass

class Graphic():
	def __init__(self):
		self._tools = Tools(write, readTh)
		self._window = Window(1080, 1920, Images())
		self.mapSize = self._tools.getMapSize()
		self._sizeX = self.mapSize[0]
		self._sizeY = self.mapSize[1]
		self._mapResources = MapRessources(
			x = self.mapSize[0],
			y = self.mapSize[0],
			sprite = self._window.getSpriteSize()
		)
		self._map = Map(
			x = self._sizeX,
			y = self._sizeY,
			tools = self._tools,
			set = self._mapResources
		)
		self._buildPlayer()
	
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