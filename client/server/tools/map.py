import sys

class Map():
	def __init__(self, **kwargs):
		self.content = [[]]
		self.sizeX = int(kwargs.get('x'))
		self.sizeY = int(kwargs.get('y'))
		self._tools = kwargs.get('tools')
		self._set = kwargs.get('set')
		for y in range(self.sizeY):
			self.content.append([])
			for x in range(self.sizeX):
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
	
	def update(self):
		data = self._getMap()
		for y in range(self.sizeY):
			for x in range(self.sizeX):
				for key , value in data[y][x].items():
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
		m = []
		self._tools.write("mct")
		for y in range(self.sizeY):
			line = []
			for x in range(self.sizeX):
				line.append(self._getTile(x, y))
			m.append(line)
		return m
