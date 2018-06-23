class Tools():
	def __init__(self, write, read):
		self.write = write
		self.readTh = read

	def getMapSize(self):
		self.write("msz")
		cmd = self.readTh.get_command().split(' ')[1:]
		return cmd

	def getAllId(self):
		self.write("gai ")
		try:
			cmd = self.readTh.get_command().split(' ')[1:]
			return cmd
		except:
			return None
