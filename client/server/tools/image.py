import os
import pygame

class Images():
	def __init__(self):
		self._spriteSizeX = 31
		self._spriteSizeY = 50
		self._items = {}
		self._items["back"] = pygame.image.load(os.path.abspath("assets/back.jpg")).convert()
		self._items["case"] = pygame.image.load(os.path.abspath("assets/ground2.png")).convert_alpha()
		self._items["food"] = pygame.image.load(os.path.abspath("assets/items/food.png")).convert_alpha()
		self._items["linemate"] = pygame.image.load(os.path.abspath("assets/items/linemate.png")).convert_alpha()
		self._items["deraumere"] = pygame.image.load(os.path.abspath("assets/items/deraumere.png")).convert_alpha()
		self._items["sibur"] = pygame.image.load(os.path.abspath("assets/items/sibur.png")).convert_alpha()
		self._items["mendiane"] = pygame.image.load(os.path.abspath("assets/items/mendiane.png")).convert_alpha()
		self._items["phiras"] = pygame.image.load(os.path.abspath("assets/items/phiras.png")).convert_alpha()
		self._items["thystame"] = pygame.image.load(os.path.abspath("assets/items/thystame.png")).convert_alpha()
		self._items["speak"] = pygame.image.load(os.path.abspath("assets/icon/applause.png")).convert_alpha()
		self._items["pushing"] = pygame.image.load(os.path.abspath("assets/icon/fist.png")).convert_alpha()
		self._items["magic"] = pygame.image.load(os.path.abspath("assets/icon/cercle2.png")).convert_alpha()
		self._itemsPlayer = {
			False: {
				1: pygame.image.load(os.path.abspath("assets/perso/stand/north.png")).convert_alpha(),
				4: pygame.image.load(os.path.abspath("assets/perso/stand/east.png")).convert_alpha(),
				3: pygame.image.load(os.path.abspath("assets/perso/stand/south.png")).convert_alpha(),
				2: pygame.image.load(os.path.abspath("assets/perso/stand/west.png")).convert_alpha()
			},
			True: {
				1: pygame.image.load(os.path.abspath("assets/perso/move/north.png")).convert_alpha(),
				2: pygame.image.load(os.path.abspath("assets/perso/move/east.png")).convert_alpha(),
				3: pygame.image.load(os.path.abspath("assets/perso/move/south.png")).convert_alpha(),
				4: pygame.image.load(os.path.abspath("assets/perso/move/west.png")).convert_alpha()
			}
		}
	def get(self, name):
		return self._items[name]

	def getFrame(self, status, orientation, frame):
		return self._itemsPlayer[status][orientation].subsurface(
						frame * self._spriteSizeX,
						0,
						self._spriteSizeX,
						self._spriteSizeY
                                        )