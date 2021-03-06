import socket

from queue import Queue
from .Threads import ThreadRead

class Server():

	def __init__(self, port, ip):
		self._ip = ip
		self._port = port
		self.teams = []
		self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connect()
		self.readTh = ThreadRead(self._sock)

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
