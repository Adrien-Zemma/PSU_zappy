import pygame

class Hud():
		def __init__(self, graphical):
			self._hasDraw = False
			self._fontsize = 25
			self._graph = graphical
			self._blocks = []
			self.buildBlock()
			self.drawBlock()

		def drawBlock(self):
			y = 0
			for el in self._blocks:
				el.draw(y, self._graph, self._graph._winSizeX)
				y += 1

		def buildBlock(self):
			for player in self._graph._playerList:
				self._blocks.append(
					self.Block(
						name=player._team,
						inv=player._inventory,
						level=player._level,
						team=player._team,
						magic=player._incanting,
						id=player._id
					)
				)

		class Block():
			def __init__(self, **kwargs):
				self.id = kwargs.get('id')
				self.team = kwargs.get('team')
				self.name = kwargs.get('name')
				self.inventory = kwargs.get('inv')
				self.level = kwargs.get('level')
				self.magic = kwargs.get('magic')

			def draw(self, y, graph, screenX):
				BLACK = (112, 112, 112)
				x = screenX - 360
				y = y * 110 + 10
				pygame.draw.rect(graph._window, BLACK, [x, y, 350, 100], 2)
				try:
					label = graph._font.render(str(self.level), 1, (255, 255, 255))
					graph._window.blit(label, (x + 10, y + 10))
				except:
					pass
				try:
					label = graph._font.render(str(self.id), 1, (255, 255, 255))
					graph._window.blit(label, (screenX - 30, y + 10))
				except:
					pass

				try:
					txt = ""
					for key, value in self.inventory.items():
						txt += (key[0] + ":" + str(value) + " ")
					label = graph._font.render(txt, 1, (0, 0, 0))
					graph._window.blit(label, (x + 5, y + 70))
				except:
					pass

				try:
					label = graph._font.render(self.team, 1, (255, 255, 255))
					graph._window.blit(label, (x + 120, y + 10))
				except:
					pass

				try:
					if self.magic:
						label = graph._font.render("magic", 1, (255, 255, 255))
						graph._window.blit(label, (x + 5, y + 40))
				except:
					pass
