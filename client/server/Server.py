import socket

from queue import Queue
from .Threads import ThreadRead, ThreadWrite

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Server(metaclass=Singleton):
	def __init__(self, port, ip="127.0.0.1"):
		self._ip = "localhost"
		self._port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.is_connected = True
		try:
			self.sock.connect((self._ip, self._port))
		except socket.error as msg:
			print("Caught exception socket.error : %s" % msg)
			exit(84)
		self.readTh = ThreadRead(self.sock)
		self.writeTh = ThreadWrite(self.sock)
		print("Connection on {}".format(self._port))
		self.x = None
		self.y = None

	def __str__(self):
		return self._ip + ":" + str(self._port)
	
	def __write(self, msg):
		if msg[-1:] != '\n':
			msg += "\n"
		totalsent = 0
		while totalsent < len(msg):
			sent = self.sock.send(msg[totalsent:].encode("Utf8"))
			if sent == 0:
				raise RuntimeError("socket connection broken")
			totalsent += sent
	
	def start_threads(self):
		self.writeTh.start()
		self.readTh.start()

	def join_threads(self):
		self.readTh.join()
		self.writeTh.join()
	
	def get_map(self):
		m = []
		i = 0
		self.writeTh.write_command("mct")
		for i in range(self.y):
			line = []
			for j in range(self.x):
				cmd = self.readTh.get_command().split(' ')[3:]
				line.append(cmd)
			m.append(line)
		return m

	def get_map_size(self):
		self.writeTh.write_command("msz")
		cmd = self.readTh.get_command().split(' ')[1:]
		self.x = int(cmd[0])
		self.y = int(cmd[1])
		return cmd
	
	def teams_name(self):
		names = []
		self.writeTh.write_command("tna")
		cmd = self.readTh.get_command()
		while cmd is not None:
			names.append(cmd)
			cmd = self.readTh.get_command()
		return names