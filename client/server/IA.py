import threading

from .IAServer import IAServer

class IA(threading.Thread):
	def __init__(self, team, port, ip="localhost"):
		print(team, port, ip)
		threading.Thread.__init__(self)
		self.server = IAServer(team, port, ip)

	def run(self):
		print("Hi IA !")
