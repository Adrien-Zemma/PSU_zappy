import threading

from .IAServer import IAServer

class IA(threading.Thread):
	def __init__(self, team, port, ip):
		threading.Thread.__init__(self)
		self.server = IAServer(team, port, ip)

	def run(self):
		while True:
			ret = self.server.forward()
			print(ret)
			if ret != "ok":
				print("Can't move forward")
				exit(84)
			else:
				print("Moving forward !")
