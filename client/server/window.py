import os
import pygame
from .map import Map
from .tools import Tools
from .image import Images
from .player import Player
from .mapressources import MapRessources

class Window():
	def __init__(self, sizeX, sizeY):
		self._winSizeY = sizeY
		self._winSizeX = sizeX
		self._fontsize = 24
		self._spriteSize = 200
		self._son = pygame.mixer.music.load(os.path.abspath("assets/sound.wav"))
		self._son = pygame.mixer.music.set_volume(0.5)
		self._font = pygame.font.Font(os.path.abspath(
			"assets/font/Android.ttf"), self._fontsize)
		self._window = pygame.display.set_mode((self._winSizeX, self._winSizeY))
		self._background = pygame.image.load(
			os.path.abspath("assets/back.jpg")).convert()
		self._window.blit(self._background, (0, 0))
		self._shiftX = self._winSizeX / 10 * 4.5
		self._shiftY = self._winSizeY / 10 * 4.5
		label = self._font.render("Loading", 1, (255, 255, 255))
		self._window.blit(label, (self._winSizeX/2, self._winSizeY/2))

	def setImages(self, imgs):
		self._sprite = imgs
	
	def getSpriteSize(self):
		return self._spriteSize
	
	def manageKeys(self, event):
		if event.key == pygame.K_ESCAPE:
			return False
		elif event.key == pygame.K_UP:
			self._shiftY += 15
		elif event.key == pygame.K_DOWN:
			self._shiftY -= 15
		elif event.key == pygame.K_LEFT:
			self._shiftX += 15
		elif event.key == pygame.K_RIGHT:
			self._shiftX -= 15
		return True

	def running(self):
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return False
				if event.type == pygame.KEYDOWN:
					return self.manageKeys(event)
	
	def _drawMap(self):
		pass
	def _drawBack(self):
		pass
	def _drawPlayer(self):
		pass

	def draw(self, toDraw):
		if type(toDraw) == None:
			self._drawBack()
		if type(toDraw) == Map:
			self._drawMap()
		if type(toDraw) == Player:
			self._drawPlayer()
