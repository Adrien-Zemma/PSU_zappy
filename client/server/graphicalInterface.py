import threading
import sys
import random
import pygame

from .Server import Server
from .Threads import ThreadRead

class MaterialCoord():
	def __init__(self, **kwargs):
		try:
			self.name = kwargs.get('name')
			self.spriteSize = kwargs.get('spriteSize')
			self.maxItem = kwargs.get('maxItem')
			self.x = kwargs.get('x')
			self.y = kwargs.get('y')
		except KeyError:
			print("Cant find index for Tile")
		self.coords = []
		self.buildCoordOfItems(self.x, self.y)

	def buildCoordOfItems(self, x, y):
		for _ in range(self.maxItem):
			tmpX = (x * self.spriteSize) + random.randint(0, (self.spriteSize * 0.8)) + self.spriteSize
			tmpY = (y * self.spriteSize) + random.randint(0, (self.spriteSize * 0.8))
			tmpIsoX = tmpX - tmpY
			tmpIsoY = (tmpX + tmpY) / 2
			self.coords.append((tmpIsoX, tmpIsoY))

class Tile():
	def __init__(self, maxItem, spriteSize, x, y):
		self.content = {
        	        "food" : MaterialCoord(name = "food", maxItem = maxItem, spriteSize = spriteSize, x = x, y = y),
        	        "sibur": MaterialCoord(name = "sibur", maxItem = maxItem, spriteSize = spriteSize, x = x, y = y),
        	        "phiras": MaterialCoord(name = "phiras", maxItem = maxItem, spriteSize = spriteSize, x = x, y = y),
        	        "thystame": MaterialCoord(name = "thystame", maxItem = maxItem, spriteSize = spriteSize, x = x, y = y),
        	        "linemate": MaterialCoord(name = "linemate", maxItem = maxItem, spriteSize = spriteSize, x = x, y = y),
        	        "mendiane": MaterialCoord(name = "mendiane", maxItem = maxItem, spriteSize = spriteSize, x = x, y = y),
        	        "deraumere": MaterialCoord(name = "deraumere", maxItem = maxItem, spriteSize = spriteSize, x = x, y = y),
		}
		

class Map():
	def __init__(self, **kwargs):
		self.x = kwargs.get('x')
		self.y = kwargs.get('y')
		self.maxItem = kwargs.get('maxItem')
		self.spriteSize = kwargs.get('spriteSize')
		self.content = [[]]
		for y in range(self.y):
			self.content.append([])
			for x in range(self.x):
				self.content[y].append(Tile(self.maxItem, self.spriteSize, x, y))

class GraphicalInterface(Server, threading.Thread):

	def __init__(self, port, ip="localhost"):
		super().__init__(port, ip)
		threading.Thread.__init__(self)
		self.readTh.start()
		self._sizeX = None
		self._sizeY = None
		self.manageConnection()
		random.seed()
		self._winSizeY = 1080
		self._winSizeX = 1920
		self._spriteSize = 100
		self._scale = 1
		self._maxItemPerCase = 100
		self._spriteSize = self._spriteSize * self._scale
		self._mapContent = self.get_map()
		self._map = Map(x = self._sizeX, y = self._sizeY, spriteSize = self._spriteSize, maxItem = self._maxItemPerCase)
		self.buildWindow()
		self.buildItem()
		print (self._map)

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
        	                		"food": int(cmd[0]),
        	                		"linemate": int(cmd[1]),
        	                		"deraumere": int(cmd[2]),
        	                		"sibur": int(cmd[3]),
        	                		"mendiane": int(cmd[4]),
        	                		"phiras": int(cmd[5]),
        	                		"thystame": int(cmd[6]),
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
		print(self._mapContent)
		for y in range(self._sizeY):
			for x in range(self._sizeX):
				self.drawCase(self._map.content[y][x], self._mapContent[y][x], x, y)

	def drawCase(self, Tile, caseContent, x, y):
		tmpX = (x * self._spriteSize)
		tmpY = (y * self._spriteSize)
		tmp2X = (tmpX - tmpY) + self._shiftX
		tmp2Y = ((tmpX + tmpY) / 2) + self._shiftY
		self._window.blit(self._items["case"], (tmp2X, tmp2Y))
		self.fillCase(Tile, caseContent)

	def fillCase(self, Tile, caseContent):
		for key, value in caseContent.items():
			for unvalue in range(value):
				try:	
					self._window.blit(
						self._items[Tile.content[key].name],
						(Tile.content[key].coords[unvalue][0] + self._shiftX,
							Tile.content[key].coords[unvalue][1] + self._shiftY)
					)
				except IndexError:
					print("Can't find index at case[", key, "][", unvalue, "]")
					exit(0)
