import socket

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
		try:
			self.sock.connect((self._ip, self._port))
		except socket.error as msg:
			print("Caught exception socket.error : %s" % msg)
			exit(84)
		print("Connection on {}".format(self._port))

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
	
	def close(self):
		self.sock.close()
	
	def get_map_size(self):
		self.__write("msz")