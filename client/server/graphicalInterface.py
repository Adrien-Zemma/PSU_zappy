import os
import sys
import random
import pygame
from .Commands import Commands
import threading

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


class GraphicalInterface(Server, threading.Thread):
	def __init__(self, port=4242, ip="localhost"):
		super().__init__(port, ip)
		threading.Thread.__init__(self)
		self.readTh.start()
		self._sizeX = None
		self._sizeY = None
		self._mapContent = [[{}]]
		self.manageConnection()
		random.seed()
		pygame.init()
		self._clock = pygame.time.Clock()
		self._winSizeY = 1080
		self._winSizeX = 1920
		self._spriteSize = 100
		self._scale = 1
		self._maxItemPerCase = 100
		self._fontsize = 24
		self._playerList = []
		self._eggList = []
		self._son = pygame.mixer.music.load(os.path.abspath("assets/sound.wav"))
		self._son = pygame.mixer.music.set_volume(0.5)
		self._font = pygame.font.Font(os.path.abspath("assets/font/Android.ttf"), self._fontsize)
		self._spriteSize = self._spriteSize * self._scale
		self._map = Map(x = self._sizeX, y = self._sizeY, spriteSize = self._spriteSize, maxItem = self._maxItemPerCase)
		self.buildWindow()
		self.buildItem()
		self.buildPlayer()
		self._commands = Commands(commands= {
			"pex" : self.expultionCmd,
			"pbc" : self.broadcastCmd,
			"pic" : self.incantationStartCmd,
			"pie" : self.incantationEndCmd,
			"pfk" : self.Cmd,
			"pnw" : self.connectionOfNewPlay,
			"pdr" : self.resourceDropCmd,
			"pgt" : self.resourcesCollectedCmd,
			"pdi" : self.deathCmd,
			"enw" : self.playerLaidEgg,
			"eht" : self.eggHatchingCmd,
			"ebo" : self.Cmd,
			"edi" : self.eggDeathCmd,
			"seg" : self.endGameCmd,
			"smg" : self.incomingMessageCmd,
			"suc" : self.unknowCommandCmd,
			"sbp" : self.commandParamCmd
		})

	def Cmd(self, cmd):
		print(cmd)
		pass
	
	def playerLaidEgg(self, cmd):
		cmd = cmd.plit(' ')[1:]
		self._eggList.append(self.Egg(cmd[0], cmd[2], cmd[3]))

	def connectionOfNewPlay(self, cmd):
		pos = cmd.split(' ')[1:]
		self._playerList.append(
			self.Player(
				id = int(pos[0][1:]),
				x = int(pos[1]),
				y = int(pos[2]),
				orient = int(pos[3]),
				level = int(pos[4]),
				team = str(pos[5]),
				inventory = self.getPlayerBag(int(pos[0][1:])),
			)
		)

	def expultionCmd(self, cmd):
		try:
			name = cmd.split(' ')[1:]
			for player in self._playerList:
				if (player._id == name):
					player._isPushing = True
		except:
			pass

		pass

	def broadcastCmd(self, cmd):
		try:
			name = cmd.split(' ')[1:]
			for player in self._playerList:
				if (player._id == name):
					player._isApplause = True
		except:
			pass

	def incantationStartCmd(self, cmd):
		try:
			name = cmd.split(' ')[1:]
			for player in self._playerList:
				if (player._id == name):
					player._incanting = True
		except:
			pass

	def incantationEndCmd(self, cmd):
		try:
			name = cmd.split(' ')[1:]
			for player in self._playerList:
				if (player._id == name):
					player._incanting = False
		except:
			pass

	def eggStartCmd(self, cmd):
		print(cmd)
		pass
	def resourceDropCmd(self, cmd):
		print(cmd)
		pass
	def resourcesCollectedCmd(self, cmd):
		print(cmd)
		pass
	def deathCmd(self, cmd):
		try:
			name = cmd.split(' ')[1:]
			for player in self._playerList:
				if (player._id == name):
					player._isAlive = False
		except:
			pass
		
	def eggDeathCmd(self, cmd):
		print(cmd)
		pass
	def eggHatchingCmd(self, cmd):
		print(cmd)
		pass
	def playerConnectToEggCmd(self, cmd):
		print(cmd)
		pass
	def endGameCmd(self, cmd):
		print(cmd)
		pass
	def commandParamCmd(self, cmd):
		print(cmd)
		pass
	def unknowCommandCmd(self, cmd):
		print(cmd)
		pass
	def incomingMessageCmd(self, cmd):
		print(cmd)
		pass

	def buildWindow(self):
		self._window = pygame.display.set_mode((self._winSizeX, self._winSizeY))
		self._background = pygame.image.load(os.path.abspath("assets/back.jpg")).convert()
		self._window.blit(self._background, (0, 0))
		self._shiftX = self._winSizeX / 10 * 4.5
		self._shiftY = (self._winSizeY - (self._spriteSize * 2 * self._sizeY)) / 2 + self._spriteSize*2
		label = self._font.render("Loading" , 1, (255, 255, 255))
		self._window.blit(label, (self._winSizeX/2, self._winSizeY/2))

	def buildItem(self):
		self._items = {}
		self._items["case"] = pygame.image.load(os.path.abspath("assets/ground2.png")).convert_alpha()
		self._items["food"] = pygame.image.load(os.path.abspath("assets/items/food.png")).convert_alpha()
		self._items["linemate"] = pygame.image.load(os.path.abspath("assets/items/linemate.png")).convert_alpha()
		self._items["deraumere"] = pygame.image.load(os.path.abspath("assets/items/deraumere.png")).convert_alpha()
		self._items["sibur"] = pygame.image.load(os.path.abspath("assets/items/sibur.png")).convert_alpha()
		self._items["mendiane"] = pygame.image.load(os.path.abspath("assets/items/mendiane.png")).convert_alpha()
		self._items["phiras"] = pygame.image.load(os.path.abspath("assets/items/phiras.png")).convert_alpha()
		self._items["thystame"] = pygame.image.load(os.path.abspath("assets/items/thystame.png")).convert_alpha()
		self._items["applause"] = pygame.image.load(os.path.abspath("assets/icon/applause.png")).convert_alpha()
		self._items["fist"] = pygame.image.load(os.path.abspath("assets/icon/fist.png")).convert_alpha()
		self._itemsPlayer = {
			"stand": {
				1 : pygame.image.load(os.path.abspath("assets/perso/stand/north.png")).convert_alpha(),
				2 : pygame.image.load(os.path.abspath("assets/perso/stand/east.png")).convert_alpha(),
				3 : pygame.image.load(os.path.abspath("assets/perso/stand/south.png")).convert_alpha(),
				4 : pygame.image.load(os.path.abspath("assets/perso/stand/west.png")).convert_alpha()
			},
			"move":{
				1: pygame.image.load(os.path.abspath("assets/perso/move/north.png")).convert_alpha(),
				2: pygame.image.load(os.path.abspath("assets/perso/move/east.png")).convert_alpha(),
				3: pygame.image.load(os.path.abspath("assets/perso/move/south.png")).convert_alpha(),
				4: pygame.image.load(os.path.abspath("assets/perso/move/west.png")).convert_alpha()
			}
		}


	def buildPlayer(self):
		nb = int(self.get_number_player()[0])
		if nb == 0:
			return
		for item in range(nb):
			try:
				pos = self.getPlayerPosition(item + 1)
				inv = self.getPlayerBag(item + 1)
				self._playerList.append(
					self.Player(
                                            x = int(pos[1]),
                                            y = int(pos[2]),
                                            id = item + 1,
                                            inventory = inv,
                                            orient = int(pos[3])
					)
				)
			except:
				continue



	class Player():
		def __init__(self, **kwargs):
			self._id = kwargs.get('id')
			self._posX = kwargs.get('x')
			self._posY = kwargs.get('y')
			self._team = kwargs.get('team')
			self._level = kwargs.get('level')
			self._orientaton = kwargs.get('orient')
			self._inventory = kwargs.get('inventory')
			self._frame = 0
			self._oldposY = 0
			self._oldposX = 0
			self._isAlive = True
			self._spriteSizeX = 31
			self._spriteSizeY = 50
			self._incanting = False
			self._isApplause = True
			self._isPushing = False

	class Egg():
		def __init__(self, name, x, y):
			self._id = name
			self._posX = 0
			self._posY = 0

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
					self.Block (
						name = player._team,
						inv = player._inventory,
						level = int(player._level[0]),
						team = player._team
					)
				)

		class Block():
			def __init__(self, **kwargs):
				self.team = kwargs.get('team')
				self.name = kwargs.get('name')
				self.inventory = kwargs.get('inv')
				self.level = kwargs.get('level')

			def draw(self, y, graph, screenX):
				BLACK = (255,255,255)
				x = screenX - 360
				y = y * 110 + 10
				pygame.draw.rect(graph._window, BLACK, [x, y, 350, 100], 2)
				try:
					label = graph._font.render(str(self.level),1,(255, 255, 255))
					graph._window.blit(label, (x +10, y + 10))
				except:
					pass
				try:
					txt = ""
					for key, value in self.inventory.items():
						txt += (key[0] + ":" + str(value) + " ")
					label = graph._font.render(txt, 1, (0, 0, 0))
					graph._window.blit(label, (x + 5 , y + 70))
				except:
					pass
				try:
					label = graph._font.render(self.team , 1, (255, 255, 255))
					graph._window.blit(label, (x + 100, y + 30))
				except:
					pass

		def drawTeams(self):
			teams = self._graph.teams_name()
			tmp = ""
			for el in teams:
				tmp += (el + " ")
			label = self._font.render(tmp, 1, (255, 255, 255))
			self._graph._window.blit(label, ((self._graph._winSizeX / 2) - (len(tmp) / 2) ,100))


	def manageConnection(self):
		cmd = self.readTh.get_command()
		if cmd == "WELCOME":
			self.write("GRAPHIC")
			cmd = self.readTh.get_command().split(' ')[1:]
			self._sizeX = int(cmd[0])
			self._sizeY = int(cmd[1])
			print("Frequence: ", self.readTh.get_command().split(' ')[1:])
			m = []
			for _ in range(self._sizeY):
				line = []
				for _ in range(self._sizeX):
					cmd = self.readTh.get_command().split(' ')
					cmd = cmd[3:]
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
						print("Error while creating line from construct map manage connection", file=sys.stderr)
						exit(84)
				m.append(line)
			self._mapContent = m
			cmd = self.readTh.get_command()
			while cmd is not None:
				self.teams.append(cmd.split(' ')[1:][0])
				cmd = self.readTh.get_command(True, timeout=0.1)
			print("Teams: ", self.teams)

	def manageKeys(self, event):
		if event.key == pygame.K_i:
			pass
		elif event.key == pygame.K_ESCAPE:
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

	def run(self):
		status = True
		pygame.mixer.music.play()
		while status:
			cmd = self.readTh.get_command(False)
			if cmd is not None:
				self._commands.parse(cmd)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					status = False
				if event.type == pygame.KEYDOWN:
					status = self.manageKeys(event)
			self._window.blit(self._background, (0, 0))
			self.updatePerso()
			self.drawMap()
			self.drawCaseContent()
			self.drawChara()
			self.drawIcon()
			self.Hud(self)
			pygame.display.update()
			self._clock.tick(5)
		pygame.mixer.music.stop
		pygame.quit()
		self.readTh.join()

	def updatePerso(self):
		for player in self._playerList:
			try:
				cmd = self.getPlayerPosition(player._id)
				player._posX = int(cmd[1])
				player._posY = int(cmd[2])
				player._orientaton = int(cmd[3])
				player._inventory = self.getPlayerBag(player._id)
				player._level = self.getPlayerLevel(player._id)

			except:
				pass

	def drawIcon(self):
		for player in self._playerList:
			tmpX = (player._posX * self._spriteSize)
			tmpY = (player._posY * self._spriteSize)
			tmp2X = (tmpX - tmpY) + self._shiftX + self._spriteSize / 5 * 2
			tmp2Y = ((tmpX + tmpY) / 2) + self._shiftY + self._spriteSize / 5 * 2
			if player._isPushing:
				self._window.blit(self._items["fist"], (tmp2X, tmp2Y))
				player._isPushing = False
			elif player._incanting:
				self._window.blit(self._items["cercle"], (tmp2X, tmp2Y))
			elif player._isApplause:
				self._window.blit(self._items["applause"], (tmp2X, tmp2Y))
				player._isApplause = False

	def drawChara(self):
		self.drawEgg()
		self.drawPlayer()

	def drawEgg(self):
		for el in self._eggList:
			tmpX = (el.x * self._spriteSize)
			tmpY = (el.y * self._spriteSize)
			tmp2X = (tmpX - tmpY) + self._shiftX + self._spriteSize / 5 * 4
			tmp2Y = ((tmpX + tmpY) / 2) + self._shiftY + self._spriteSize / 5 * 4
			self._window.blit(self._items["egg"], (tmp2X, tmp2Y))

	def drawPlayer(self):
		for player in self._playerList:
			if not player._isAlive:
				continue
			tmpX = (player._posX * self._spriteSize)
			tmpY = (player._posY * self._spriteSize)
			tmp2X = (tmpX - tmpY) + self._shiftX + self._spriteSize / 5 * 4
			tmp2Y = ((tmpX + tmpY) / 2) + self._shiftY + self._spriteSize / 5 * 4
			if tmp2X == player._oldposX and tmp2Y == player._oldposY:
				self._window.blit(
					self._itemsPlayer["stand"][player._orientaton].subsurface(
						player._frame * player._spriteSizeX,
						0,
						player._spriteSizeX,
						player._spriteSizeY
					),
					(tmp2X, tmp2Y)

				)
			else:
				player._oldposX = tmp2X
				player._oldposY = tmp2Y
				self._window.blit(
					self._itemsPlayer["move"][player._orientaton].subsurface(
						player._frame * player._spriteSizeX,
						0,
						player._spriteSizeX,
						player._spriteSizeY
                                        ),
					(tmp2X, tmp2Y)
				)
			if player._frame > 2:
				player._frame = -1
			player._frame += 1



	def drawMap(self):
		for y in range(self._sizeY):
			for x in range(self._sizeX):
				try:
					self.drawCase(self._map.content[y][x], self._mapContent[y][x], x, y)
				except IndexError:
					print("Can't find index for ", y, x)
					exit(1)

	def drawCase(self, Tile, caseContent, x, y):
		tmpX = (x * self._spriteSize)
		tmpY = (y * self._spriteSize)
		tmp2X = (tmpX - tmpY) + self._shiftX
		tmp2Y = ((tmpX + tmpY) / 2) + self._shiftY
		self._window.blit(self._items["case"], (tmp2X, tmp2Y))


	def drawCaseContent(self):
		for y in range(self._sizeY):
			for x in range(self._sizeX):
				try:
					self.fillCase(self._map.content[y][x], self._mapContent[y][x])
				except IndexError:
					print("Can't find index for ", y, x)
					exit(1)



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

	def getPlayerPosition(self, name):
		try:
			self.write("ppo " + str(name))
			cmd = self.readTh.get_command().split(' ')[1:]
		except:
			return None
		return cmd

	def get_map_size(self):
        	self.write("msz")
        	cmd = self.readTh.get_command().split(' ')[1:]
        	return cmd

	def get_number_player(self):
		self.write("gnp")
		tmp = self.readTh.get_command().split(' ')[1:]
		return tmp

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
	
	def getPlayerBag(self, ident:int):
		self.write("pin #" + str(ident))
		cmd = self.readTh.get_command()
		try:
			cmd = cmd.split(' ')[4:]
			tab = {
				"food": int (cmd[0]),
				"linemate": int(cmd[1]),
				"deraumere": int(cmd[2]),
				"sibur": int(cmd[3]),
				"mendiane": int(cmd[4]),
				"phiras": int(cmd[5]),
				"thystame": int(cmd[6]),
			}
		except:
			return None
		return tab

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

	def getPlayerLevel(self, name):
		self.write("plv #" + str(name))
		try:
			cmd = self.readTh.get_command().split(' ')[1:]
			return cmd[1:]
		except:
			return None
		pass
