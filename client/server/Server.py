import socket

from queue import Queue
from .Threads import ThreadRead


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Server(metaclass=Singleton):
	
	called = False

	def __init__(self, port, ip = "localhost"):
		self._ip = ip
		self._port = port
		if not Server.called:
			self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.connect()
			Server.called = True
	
	def connect(self):
        	try:
        	    self._sock.connect((self._ip, self._port))
        	except socket.error as msg:
        	    print("Caught exception socket.error : %s" % msg)
        	    exit(84)

	def write(self, msg):
        	if msg[-1:] != '\n':
        	    msg += "\n"
        	totalsent = 0
        	while totalsent < len(msg):
        	    sent = self._sock.send(msg[totalsent:].encode("Utf8"))
        	    if sent == 0:
        	        raise RuntimeError("socket connection broken")
        	    totalsent += sent

	def read(self):
        	buff = ""
        	while True:
        	    data = self._sock.recv(1)
        	    if data:
        	        buff += data.decode('utf-8')
        	    else:
        	        return None
        	    if buff.find('\n') != -1:
        	        buff = buff.replace('\n', '')
        	        break
        	return buff