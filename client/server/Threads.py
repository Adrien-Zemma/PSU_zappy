import threading
import time
import socket

from .Server import Server

class ThreadRead(threading.Thread):
	"""
	A thread that will read on a socket
	"""
	def __init__(self, socket, queue):
		"""
		Constructor.
		@param socket socket to read
		@param queue queue synchronization commands
		"""
		threading.Thread.__init__(self)
		self.queue = queue
		self.socket = socket

	
	def _read(self):
		buff = ""
		serv = Server(8081)
		while True:
			data = self.socket.recv(1)
			if data:
				buff += data.decode('utf-8')
			else:
				serv.is_connected = False
				return None
			if buff.find('\n') != -1:
				buff = buff.replace('\n', '')
				break
		return buff
	
	def get_command(self):
		cmd = self.queue.get()
		self.queue.task_done()
		return cmd

	def run(self):
		"""
		Thread run method. Read command from server socket
		"""
		cmd = self._read()
		while cmd:
			self.queue.put(cmd)
			print("Put in list : [{}]".format(cmd))
			time.sleep(1)
			cmd = self._read()

class ThreadWrite(threading.Thread):
	"""
	A thread that will write on a socket
	"""
	def __init__(self, socket, queue):
		"""
		Constructor.
		@param socket socket to read
		@param queue queue synchronization commands
		"""
		threading.Thread.__init__(self)
		self.queue = queue
		self.socket = socket

	
	def __write(self, msg):
		if msg[-1:] != '\n':
			msg += "\n"
		totalsent = 0
		print("Hey!")
		while totalsent < len(msg):
			sent = self.socket.send(msg[totalsent:].encode("Utf8"))
			if sent == 0:
				raise RuntimeError("socket connection broken")
			totalsent += sent
	
	def write_command(self, cmd):
		self.queue.put(cmd)
		return cmd

	def get_command(self):
		cmd = self.queue.get()
		self.queue.task_done()
		return cmd

	def run(self):
		"""
		Thread run method. Read command from server socket
		"""
		while True:
			cmd = self.get_command()
			self.__write(cmd)