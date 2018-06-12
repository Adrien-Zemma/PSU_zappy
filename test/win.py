import pygame
import random
from pygame.locals import *

		

def getMap():
	return [[{"linemate":0, "deraumere":1, "sibur":1, "mendiane":1, "phiras":1, 'thystame':1, "food":1},
		{"linemate":1, "deraumere":1, "sibur":1, "mendiane":1, "phiras":1, 'thystame':1, "food":1}],
		[{"linemate":1, "deraumere":1, "sibur":1, "mendiane":1, "phiras":1, 'thystame':1, "food":1},
		{"linemate":1, "deraumere":1, "sibur":1, "mendiane":1, "phiras":1, 'thystame':1, "food":1}]]
class Drawer():
	def __init__(self, x, y):
		random.seed()
		self._winSizeX = 1080
		self._winSizeY = 1920
		self._sizeX = x
		self._sizeY = y
		self._spriteSize = 100
		self._scale = 1
		self._maxItemPerCase = 100
		self._map = [[{}]]
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
				self._map[y][x] = {
					"linemate":[],
					"deraumere":[],						"sibur":[],
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
			dic["x"] = (x * self._spriteSize * self._scale) + random.randint(0, (self._spriteSize * 0.7) * self._scale) + self._shiftX
			dic["y"] = (y * self._spriteSize * self._scale) + random.randint(0, (self._spriteSize * 0.7) * self._scale) + self._shiftY
			tmp.append(dic)
		return tmp
	
	def buildWindow(self):
		self._window = pygame.display.set_mode((self._winSizeY, self._winSizeX))
		self._background = pygame.image.load("back.jpg").convert()
		self._window.blit(self._background, (0, 0))
		self._shiftX = (self._winSizeY - (self._sizeX * self._spriteSize)) / 2
		self._shiftY = (self._winSizeX - (self._sizeY * self._spriteSize)) / 2
		
	def buildItem(self):
		self._items = {}
		self._items["case"] = pygame.image.load("ground.png").convert_alpha()
		self._items["food"] = pygame.image.load("items/food.png").convert_alpha()
		self._items["linemate"] =  pygame.image.load("items/linemate.png").convert_alpha()
		self._items["deraumere"] =  pygame.image.load("items/deraumere.png").convert_alpha()
		self._items["sibur"] =  pygame.image.load("items/sibur.png").convert_alpha()
		self._items["mendiane"] =  pygame.image.load("items/mendiane.png").convert_alpha()
		self._items["phiras"] =  pygame.image.load("items/phiras.png").convert_alpha()
		self._items["thystame"] =  pygame.image.load("items/thystame.png").convert_alpha()
	
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
				print(str(y) + " "+ str(x))
				self.drawCase(self._map[y][x], self._mapContent[y][x], x, y)

	def drawCase(self, case, caseContent, x, y):
		tmpX = (x * self._spriteSize) + self._shiftX
		tmpY = (y * self._spriteSize) + self._shiftY
		self._window.blit(self._items["case"], (tmpX, tmpY))
		self.fillCase(case, caseContent)

	def fillCase(self, case, caseContent):
		for key, value in caseContent.items():
			for unvalue in range(value):
				self._window.blit(
					case[key][unvalue]["sprite"],
					(case[key][unvalue]["x"],
					case[key][unvalue]["y"])
				)

if __name__ == '__main__':
	draw = Drawer(2, 2)
	draw.start()