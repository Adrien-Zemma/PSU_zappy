import sys

class Map():
	def __init__(self, **kwargs):
		self.content = [[]]
		self._trueMap = [[{}]]
		self.sizeX = int(kwargs.get('x'))
		self.sizeY = int(kwargs.get('y'))
		self._tools = kwargs.get('tools')
		self._set = kwargs.get('set')
		for y in range(self.sizeY):
			self.content.append([])
			self._trueMap.append([])
			for x in range(self.sizeX):
				self._trueMap[y].append({
					"food": 0,
					"linemate": 0,
					"deraumere": 0,
					"sibur": 0,
					"mendiane": 0,
					"phiras": 0,
					"thystame": 0,
				})
				self.content[y].append(
					self.Tile(x, y)
				)
	
	class Tile():
		def __init__(self, x, y):
			self.content = {
				"food": [],
				"linemate": [],
				"deraumere": [],
				"sibur": [],
				"mendiane": [],
				"phiras": [],
				"thystame":[]
			}
		def add(self, index, coord):
			self.content[index].append(coord)

		def clear(self):
			self.content = {
				"food": [],
				"linemate": [],
				"deraumere": [],
				"sibur": [],
				"mendiane": [],
				"phiras": [],
				"thystame": []
			}
	
	def update(self):
		for y in range(self.sizeY):
			for x in range(self.sizeX):
				self.content[y][x].clear()
				for key, value in self._trueMap[y][x].items():
					for item in range(value):
						self.content[y][x].add(
							key,
							self._set.get(
								x,
								y,
								key,
								item
							)
						)

	def _getTile(self, x: str, y: str):
		try:
			cmd = self._tools.readTh.get_command().split(' ')[3:]
			return {
				"food": int(cmd[0]),
				"linemate": int(cmd[1]),
				"deraumere": int(cmd[2]),
				"sibur": int(cmd[3]),
				"mendiane": int(cmd[4]),
				"phiras": int(cmd[5]),
				"thystame": int(cmd[6])
			}
		except:
			print("Error while getting tile", file = sys.stderr)

	def _getMap(self):
		self._tools.write("mct")

	def addTile(self, cmd):
		try:
			cmd = cmd.split(' ')[1:]
			x = int (cmd[0])
			y = int (cmd[1])
			cmd = cmd[2:]
			tmp = {
				"food": int(cmd[0]),
				"linemate": int(cmd[1]),
				"deraumere": int(cmd[2]),
				"sibur": int(cmd[3]),
				"mendiane": int(cmd[4]),
				"phiras": int(cmd[5]),
				"thystame": int(cmd[6])
			}
			self._trueMap[y][x] = tmp
		except:
			print("Error while getting tile", file = sys.stderr)
