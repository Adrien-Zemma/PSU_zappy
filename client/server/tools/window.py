import os
import pygame
from .map import Map
from .tools import Tools
from .image import Images
from .player import Player
from pygame import Surface

class Window():
	def __init__(self, sizeY, sizeX):
		self._winSizeY = sizeY
		self._winSizeX = sizeX
		self._fontsize = 24
		self._spriteSize = 100
		self.clock = pygame.time.Clock()
		self._son = pygame.mixer.music.load(os.path.abspath("assets/sound.wav"))
		self._son = pygame.mixer.music.set_volume(0.5)
		self._font = pygame.font.Font(os.path.abspath("assets/font/Android.ttf"), self._fontsize)
		self._window = pygame.display.set_mode((self._winSizeX, self._winSizeY))
		self._shiftX = self._winSizeX / 10 * 4.5
		self._shiftY = self._winSizeY / 10 * 4.5
		label = self._font.render("Loading...", 1, (255, 255, 255))
		self._window.blit(label, (self._winSizeX / 2, self._winSizeY / 2))

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
		return True		
	
	def _drawCase(self, case):
		for key, value in case.content.items():
			for pos in value:
				tmp2X = (pos[0] - pos[1]) + self._shiftX
				tmp2Y = ((pos[0] + pos[1]) / 2) + self._shiftY
				self._window.blit(
					self._sprite.get(key),
					(tmp2X, tmp2Y)
				)

	def drawField(self, sizeX, sizeY):
		for y in range(sizeY):
			for x in range(sizeX):
				tmpX = (x * self._spriteSize)
				tmpY = (y * self._spriteSize)
				tmp2X = (tmpX - tmpY) + self._shiftX
				tmp2Y = ((tmpX + tmpY) / 2) + self._shiftY
				self._window.blit(
					self._sprite.get("case"),
					(tmp2X, tmp2Y)
				)

	def drawMap(self, field):
		for line in field.content:
			for case in line:
				self._drawCase(case)

	def drawBack(self):
		self._window.blit(self._sprite.get("back"), (0, 0))
	
	def _drawPlayerMagic(self, toDraw, x, y):
		if toDraw.magic:
			self._window.blit(
				self._sprite.get("magic"),
				(x, y)
			)
	def _drawPlayerPos(self, toDraw, x, y):
		self._window.blit(
			self._sprite.getFrame(
				toDraw.moving,
				toDraw.o,
				toDraw.frame
			),
			(x, y)
		)

	def _drawPLayerIcon(self, toDraw, x, y):
		if toDraw.speak:
			self._window.blit(
				self._sprite.get("speak"),
				(x, y)
			)
		if toDraw.pushing:
			self._window.blit(
				self._sprite.get("pushing"),
				(x, y)
			)


	def drawPlayer(self, toDraw):
		if toDraw.frame > :
			toDraw.frame = -1
		toDraw.frame += 1
		tmpX = (toDraw.x * self._spriteSize)
		tmpY = (toDraw.y * self._spriteSize)
		tmp2X = (tmpX - tmpY) + self._shiftX + self._spriteSize / 5 * 4
		tmp2Y = ((tmpX + tmpY) / 2) + self._shiftY + self._spriteSize / 5 * 4
		self._drawPlayerMagic(toDraw, tmp2X, tmp2X)
		self._drawPlayerPos(toDraw, tmp2X, tmp2X)
		self._drawPLayerIcon(toDraw, tmp2X, tmp2X)
		