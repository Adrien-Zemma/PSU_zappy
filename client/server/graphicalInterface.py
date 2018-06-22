import os
import sys
import random
import pygame
from .hud import *
from .minerals import Map
from .Commands import Commands
import threading
from .Server import Server
from .Threads import ThreadRead

class GraphicalInterface(Server, threading.Thread):
	def __init__(self, port=4242, ip="localhost"):
		super().__init__(port, ip)
		threading.Thread.__init__(self)
		self.readTh.start()
		self.buidCommande()
		self._sizeX = None
		self._sizeY = None
		self._mapContent = [[{}]]
		self.manageConnection()
		self.daemon = True
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
		self.builPlayerSprite()
		self.buildPlayer()

	def buidCommande(self):
		self._commands = Commands(commands={
			"pex": self.expultionCmd,
			"pbc": self.broadcastCmd,
			"pic": self.incantationStartCmd,
			"pie": self.incantationEndCmd,
			"pfk": self.Cmd,
			"pnw": self.connectionOfNewPlay,
			"pdr": self.resourceDropCmd,
			"pgt": self.resourcesCollectedCmd,
			"pdi": self.deathCmd,
			"enw": self.playerLaidEgg,
			"eht": self.eggHatchingCmd,
			"ebo": self.Cmd,
			"edi": self.eggDeathCmd,
			"seg": self.endGameCmd,
			"smg": self.incomingMessageCmd,
			"suc": self.unknowCommandCmd,
			"sbp": self.commandParamCmd
		})

	def Cmd(self, cmd):
		print(cmd)
		pass

	def playerLaidEgg(self, cmd):
		cmd = cmd.plit(' ')[1:]
		self._eggList.append(self.Egg(cmd[0], cmd[2], cmd[3]))

	def connectionOfNewPlay(self, cmd):
		pos = cmd.split(' ')[1:]
		try :
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
		except:
			pass

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
		self._items["cercle"] = pygame.image.load(os.path.abspath("assets/icon/cercle2.png")).convert_alpha()
		
	def builPlayerSprite(self):
		self._itemsPlayer = {
			"stand": {
				1: pygame.image.load(os.path.abspath("assets/perso/stand/north.png")).convert_alpha(),
				2: pygame.image.load(os.path.abspath("assets/perso/stand/east.png")).convert_alpha(),
				3: pygame.image.load(os.path.abspath("assets/perso/stand/south.png")).convert_alpha(),
				4: pygame.image.load(os.path.abspath("assets/perso/stand/west.png")).convert_alpha()
			},
			"move": {
				1: pygame.image.load(os.path.abspath("assets/perso/move/north.png")).convert_alpha(),
				2: pygame.image.load(os.path.abspath("assets/perso/move/east.png")).convert_alpha(),
				3: pygame.image.load(os.path.abspath("assets/perso/move/south.png")).convert_alpha(),
				4: pygame.image.load(os.path.abspath("assets/perso/move/west.png")).convert_alpha()
			}
		}

	def buildPlayer(self):
		nb = self.getAllId()
		if nb == None:
			return
		for item in nb:
			item = int(item)
			try:
				team = self.getPlayerTeam(item)
				pos = self.getPlayerPosition(item)
				inv = self.getPlayerBag(item)
				if (pos == None or inv == None):
					continue
				self._playerList.append(
					self.Player(
						team = team,
						x = int(pos[1]),
						y = int(pos[2]),
						id = item,
						inventory = inv,
						orient = int(pos[3])
					)
				)
			except:
				continue

	class Player():
		def __init__(self,**kwargs):
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
			self._isApplause = False
			self._isPushing = False

	class Egg():
		def __init__(self, name, x, y):
			self._id = name
			self._posX = 0
			self._posY = 0

	def manageConnection(self):
		cmd = self.readTh.get_command()
		if cmd == "WELCOME":
			self.write("GRAPHIC")
			cmd = self.readTh.get_command().split(' ')[1:]
			self._sizeX = int(cmd[0])
			self._sizeY = int(cmd[1])
			print("Frequence: ", self.readTh.get_command().split(' ')[1:])
			self._mapContent = self.getMap()
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
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					status = False
				if event.type == pygame.KEYDOWN:
					status = self.manageKeys(event)
			self._window.blit(self._background, (0, 0))
			cmd = self.readTh.get_command(True, 1.5)
			if cmd is not None:
				self._commands.parse(cmd)
			self._mapContent = self.getMap()
			self.updatePerso()
			self.drawMap()
			self.drawCaseContent()
			self.drawIcon()
			self.drawChara()
			Hud(self)
			pygame.display.update()
			self._clock.tick(60)
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
			if player._frame > 1:
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
			self.write("ppo #" + str(name))
			cmd = self.readTh.get_command()
			if (cmd == "ko"):
				return None
			cmd = cmd.split(' ')[1:]
		except:
			return None
		return cmd

	def getMapSize(self):
		self.write("msz")
		cmd = self.readTh.get_command().split(' ')[1:]
		return cmd

	def getNumberPlayer(self):
		self.write("gnp")
		tmp = self.readTh.get_command().split(' ')[1:]
		return tmp

	def getMap(self):
		m = []
		for y in range(self._sizeY):
			line = []
			for x in range(self._sizeX):
				line.append(self.getTile(x, y))
			m.append(line)
		return m

	def teamsName(self):
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

	def getPlayerTeam(self, name):
		self.write("gpt #" + str(name))
		cmd = self.readTh.get_command()
		return cmd

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

	def getTile(self, x:str, y:str):
		self.write("bct " + str(x) + " " + str(y))
		cmd = self.readTh.get_command().split(' ')[3:]
		try:
			return {
				"food": int(cmd[0]),
				"linemate": int(cmd[1]),
				"deraumere": int(cmd[2]),
				"sibur": int(cmd[3]),
				"mendiane": int(cmd[4]),
				"phiras": int(cmd[5]),
				"thystame": int(cmd[6])
			}
		except IndexError:
			print("Error while getting tile", file=sys.stderr)
			exit(84)

	def getPlayerLevel(self, name):
		self.write("plv #" + str(name))
		try:
			cmd = self.readTh.get_command().split(' ')[2:]
			return int(cmd[0])
		except:
			return None
		
	def getAllId(self):
		self.write("gai ")
		try:
			cmd = self.readTh.get_command().split(' ')[1:]
			return cmd
		except:
			return None
