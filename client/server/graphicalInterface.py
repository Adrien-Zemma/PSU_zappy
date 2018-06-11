import threading
import sys
import random
import pygame

from .Server import Server
from .Threads import ThreadRead
from pygame.locals import *


class GraphicalInterface(Server, threading.Thread):

	def __init__(self, port, ip="localhost"):
		super().__init__(port, ip)
		threading.Thread.__init__(self)
		self.readTh = ThreadRead(self._sock)
		self.readTh.start()
		random.seed()
		pygame.init()
		self._winSizeX = 1080
		self._winSizeY = 1920
		cmd = self.get_map_size()
		self._sizeX = int(cmd[0])
		self._sizeY = int(cmd[1])
		self._spriteSize = 100
		self._scale = 1
		self._map = [[[{}]]]
		self.buildWindow()
		self.buildItem()
		self._mapContent = [[{}]]
		self._mapContent = self.get_map()
		self.buildMapItem()

	def buildMapItem(self):
		for y in range(self._sizeY):
			self._map.append([])
			for x in range(self._sizeX):
				self._map[y].append([])
				self.buildCaseItem(self._mapContent[y][x], x, y)
	
	def buildCaseItem(self, case, x, y):
		tmp = []
		dic = {} 
		for key, value in case.items():
			for i in range(value):
				dic["name"] = key
				dic["sprite"] = self._items[key]
				dic["x"] = (x * self._spriteSize * self._scale) + random.randint(0, self._spriteSize * self._scale) + self._shiftX
				dic["y"] = (y * self._spriteSize * self._scale) + random.randint(0, self._spriteSize * self._scale) + self._shiftY
				self._map[y][x].append(dic)
				i = i
		return tmp
	
	def buildWindow(self):
		self._window = pygame.display.set_mode((self._winSizeY, self._winSizeX))
		self._background = pygame.image.load("back.jpg").convert()
		self._window.blit(self._background, (0, 0))
		self._shiftX = (self._winSizeY - (self._sizeX * self._spriteSize)) / 2
		self._shiftY = (self._winSizeX - (self._sizeY * self._spriteSize)) / 2
		
	def buildItem(self):
		self._items = {}
		self._items["case"] = pygame.image.load("case.jpg").convert()
		self._items["food"] = pygame.image.load("items/food.png").convert()
		self._items["linemate"] =  pygame.image.load("items/linemate.png").convert()
		self._items["deraumere"] =  pygame.image.load("items/deraumere.png").convert()
		self._items["sibur"] =  pygame.image.load("items/sibur.png").convert()
		self._items["mendiane"] =  pygame.image.load("items/mendiane.png").convert()
		self._items["phiras"] =  pygame.image.load("items/phiras.png").convert()
		self._items["thystame"] =  pygame.image.load("items/thystame.png").convert()

	def drawMap(self):
		for y in range(self._sizeY):
			for x in range(self._sizeX):
				self.drawCase(self._map[y][x], self._mapContent[y][x], x, y)

	def drawCase(self, case, caseContent, x, y):
		tmpX = (x * self._spriteSize) + self._shiftX
		tmpY = (y * self._spriteSize) + self._shiftY
		self._window.blit(self._items["case"], (tmpX, tmpY))
		self.fillCase(case, caseContent)

	def fillCase(self, case, caseContent):
		for key, value in caseContent:
			i = 0
			for el in case:
				if (i == value):
					break
				if (el["name"] == key):
					i = i + 1
					self._window.blit(el["sprite"], (el["x"], el["y"]))


	def _write(self, msg):
		super(GraphicalInterface, self).write(msg)

	def run(self):
		i = 0
		self.drawMap()
		pygame.display.flip()
		while (1):
			i = i + 1

	def get_map_size(self):
        	self._write("msz")
        	cmd = self.readTh.get_command().split(' ')[1:]
        	return cmd

	def get_map(self):
		m = []
		self._write("mct")
		for _ in range(self._sizeY):
			line = []
			for _ in range(self._sizeX):
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