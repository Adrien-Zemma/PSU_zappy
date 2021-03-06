class Commands():
	def __init__(self, **args):
		if args is None:
			self.commands = {}
		else:
			self.commands = args.get("commands", {})
	def append(self, name: str, fnct):
		self.commands[name] =  fnct

	def parse(self, command: str):
		if self.commands is None or command == "" or command is None:
			return 1
		try:
			self.commands[command.split(' ')[0]](command)
		except KeyError:
			print("Can't found self.commands[{}]".format(command))
			return 1
		return 0
