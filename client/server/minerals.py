import random

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
			tmpX = (x * self.spriteSize) + random.randint(0,
                                                 (self.spriteSize * 0.8)) + self.spriteSize
			tmpY = (y * self.spriteSize) + random.randint(0, (self.spriteSize * 0.8))
			tmpIsoX = tmpX - tmpY
			tmpIsoY = (tmpX + tmpY) / 2
			self.coords.append((tmpIsoX, tmpIsoY))


class Tile():
	def __init__(self, maxItem, spriteSize, x, y):
		self.content = {
        	        "food": MaterialCoord(name="food", maxItem=maxItem, spriteSize=spriteSize, x=x, y=y),
        	        "sibur": MaterialCoord(name="sibur", maxItem=maxItem, spriteSize=spriteSize, x=x, y=y),
        	        "phiras": MaterialCoord(name="phiras", maxItem=maxItem, spriteSize=spriteSize, x=x, y=y),
        	        "thystame": MaterialCoord(name="thystame", maxItem=maxItem, spriteSize=spriteSize, x=x, y=y),
        	        "linemate": MaterialCoord(name="linemate", maxItem=maxItem, spriteSize=spriteSize, x=x, y=y),
        	        "mendiane": MaterialCoord(name="mendiane", maxItem=maxItem, spriteSize=spriteSize, x=x, y=y),
        	        "deraumere": MaterialCoord(name="deraumere", maxItem=maxItem, spriteSize=spriteSize, x=x, y=y),
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
