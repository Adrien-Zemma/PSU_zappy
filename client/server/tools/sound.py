import os
import pygame
from pygame import *
class Sound():
	def __init__(self):
		pygame.mixer.init(44100, -16,2,2048)
		pygame.mixer.music.load(os.path.abspath("assets/sound.wav"))
		pygame.mixer.music.play()
		pygame.mixer.music.set_volume(0.5)
		self.playlist = {
			"magic" : pygame.mixer.Sound("assets/sounds/events/magic.wav"),
			"spaw"  : pygame.mixer.Sound("assets/sounds/spawn/0.wav"),
			"death" : pygame.mixer.Sound("assets/sounds/death/4.wav")
		}
	def play(self, sound):
		try:
			self.playlist[sound].play()
		except:
			pass

		