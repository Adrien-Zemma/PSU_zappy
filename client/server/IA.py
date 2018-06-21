import threading

from .IAServer import IAServer

class IA(threading.Thread):
	def __init__(self, team, port, ip):
		threading.Thread.__init__(self)
		self.server = IAServer(team, port, ip)
		self._loop = True
	
	def stop(self: object):
		self._loop = False

	def run(self):
		while self._loop:
			ret = self.server.forward()
			print(ret)
			if ret != "ok":
				print("Can't move forward")
				exit(84)
			else:
				print("Moving forward !")
