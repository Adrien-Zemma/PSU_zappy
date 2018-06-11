import pygame
import random
from pygame.locals import *

		

def getMap():
	return [[{"linemate":1, "deraumere":5, "sibur":2, "mendiane":1, "phiras":1, 'thystame':1},
		{"linemate":1, "deraumere":5, "sibur":2, "mendiane":1, "phiras":1, 'thystame':1}],
		[{"linemate":1, "deraumere":5, "sibur":2, "mendiane":1, "phiras":1, 'thystame':1},
		{"linemate":1, "deraumere":5, "sibur":2, "mendiane":1, "phiras":1, 'thystame':1}]]
class Drawer():
	def __init__(self, x, y):
		random.seed()
		pygame.init()
		self._winSizeX = 1080
		self._winSizeY = 1920
		self._sizeX = x
		self._sizeY = y
		self._spriteSize = 100
		self._scale = 1
		self._map = [[[{}]]]
		self.buildWindow()
		self.buildItem()
		self._mapContent = [[{}]]
		self._mapContent = getMap()
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
	
	def start(self):
		i = 0
		getMap()
		self.drawMap()
		pygame.display.flip()
		while (1):
			i = i + 1

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

if __name__ == '__main__':
	draw = Drawer(5, 5)
	draw.start()