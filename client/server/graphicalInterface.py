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
		self.readTh.start()
		self.manageConnection()
		random.seed()
		self._winSizeY = 1080
		self._winSizeX = 1920
		self._sizeX = None
		self._sizeY = None
		self._spriteSize = 100
		self._scale = 1
		self._maxItemPerCase = 100
		self._map = [[{}]]
		self.buildWindow()
		self.buildItem()
		self._mapContent = self.get_map()
		self.buildMapItem()

	def manageConnection(self):
		cmd = self.readTh.get_command()
		if cmd == "WELCOME":
			self.write("team graphique")
			cmd = self.readTh.get_command().split(' ')
			self._sizeX = int(cmd[0])
			self._sizeY = int(cmd[1])
			print("Setted coords")

	def run(self):
		self.drawMap()
		pygame.display.flip()
		while True:
			pass

	def get_map_size(self):
        	self.write("msz")
        	cmd = self.readTh.get_command().split(' ')[1:]
        	return cmd

	def get_map(self):
		m = []
		self.write("mct")
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
	
	def buildMapItem(self):
		for y in range(self._sizeY):
			self._map.append([])
			for x in range(self._sizeX):
				self._map[y].append([])
				self._map[y][x] = {
					"linemate":[],
					"deraumere":[],
					"sibur":[],
					"mendiane":[],
					"phiras":[],
					"thystame":[],
					"food":[]
				}
			for key, _ in self._map[y][x].items():
				self._map[y][x][key] = self.buildCaseItem(key, x, y)
	
	def buildCaseItem(self, key, x, y):
		tmp = []
		for _ in range(self._maxItemPerCase):
			dic = {}
			dic["name"] = key
			dic["sprite"] = self._items[key]
			tmpX = (x * self._spriteSize * self._scale) + random.randint(0, (self._spriteSize * self._scale * 0.8) * self._scale) + self._spriteSize * self._scale
			tmpY = (y * self._spriteSize * self._scale) + random.randint(0, (self._spriteSize * self._scale * 0.8) * self._scale) 
			dic["x"] = tmpX - tmpY
			dic["y"] = (tmpX + tmpY) / 2
			tmp.append(dic)
		return tmp
	
	def buildWindow(self):
		self._window = pygame.display.set_mode((self._winSizeX, self._winSizeY))
		self._background = pygame.image.load("back.jpg").convert()
		self._window.blit(self._background, (0, 0))

		
		self._shiftX = self._winSizeX / 10 * 4.5
		self._shiftY = (self._winSizeY - (self._spriteSize * 2 * self._sizeY)) / 2 + self._spriteSize*2
		
	def buildItem(self):
		self._items = {}
		self._items["case"] = pygame.image.load("ground2.png").convert_alpha()
		self._items["food"] = pygame.image.load("items/food.png").convert_alpha()
		self._items["linemate"] =  pygame.image.load("items/linemate.png").convert_alpha()
		self._items["deraumere"] =  pygame.image.load("items/deraumere.png").convert_alpha()
		self._items["sibur"] =  pygame.image.load("items/sibur.png").convert_alpha()
		self._items["mendiane"] =  pygame.image.load("items/mendiane.png").convert_alpha()
		self._items["phiras"] =  pygame.image.load("items/phiras.png").convert_alpha()
		self._items["thystame"] =  pygame.image.load("items/thystame.png").convert_alpha()

	def drawMap(self):
		for y in range(self._sizeY):
			for x in range(self._sizeX):
				self.drawCase(self._map[y][x], self._mapContent[y][x], x, y)

	def drawCase(self, case, caseContent, x, y):
		tmpX = (x * self._spriteSize)
		tmpY = (y * self._spriteSize)
		tmp2X = (tmpX - tmpY) + self._shiftX
		tmp2Y = ((tmpX + tmpY) / 2) + self._shiftY
		self._window.blit(self._items["case"], (tmp2X, tmp2Y))
		self.fillCase(case, caseContent)

	def fillCase(self, case, caseContent):
		for key, value in caseContent.items():
			for unvalue in range(value):
				self._window.blit(
					case[key][unvalue]["sprite"],
					(case[key][unvalue]["x"] + self._shiftX,
					case[key][unvalue]["y"] + self._shiftY)
				)