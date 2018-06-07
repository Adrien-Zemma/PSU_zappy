import threading
import time
import socket
import queue

class ThreadRead(threading.Thread):
	"""
	A thread that will read on a socket
	"""
	def __init__(self, socket):
		"""
		Constructor.
		@param socket socket to read
		@param queue queue synchronization commands
		"""
		threading.Thread.__init__(self)
		self.queue = queue.Queue()
		self.socket = socket

	
	def _read(self):
		buff = ""
		while True:
			data = self.socket.recv(1)
			if data:
				buff += data.decode('utf-8')
			else:
				return None
			if buff.find('\n') != -1:
				buff = buff.replace('\n', '')
				break
		return buff
	
	def get_command(self, status: bool = True):
		try:
			data = self.queue.get(status)
			self.queue.task_done()
		except queue.Empty:
			data = None
		return data

	def run(self):
		"""
		Thread run method. Read command from server socket
		"""
		cmd = self._read()
		while cmd:
			self.queue.put(cmd)
			cmd = self._read()

class ThreadWrite(threading.Thread):
	"""
	A thread that will write on a socket
	"""
	def __init__(self, socket):
		"""
		Constructor.
		@param socket socket to read
		@param queue queue synchronization commands
		"""
		threading.Thread.__init__(self)
		self.queue = queue.Queue()
		self.socket = socket

	
	def __write(self, msg):
		if msg[-1:] != '\n':
			msg += "\n"
		totalsent = 0
		while totalsent < len(msg):
			sent = self.socket.send(msg[totalsent:].encode("Utf8"))
			if sent == 0:
				raise RuntimeError("socket connection broken")
			totalsent += sent
	
	def write_command(self, cmd):
		self.queue.put(cmd)

	def __get_command(self):
		cmd = self.queue.get()
		self.queue.task_done()
		return cmd

	def run(self):
		"""
		Thread run method. Read command from server socket
		"""
		while True:
			cmd = self.__get_command()
			self.__write(cmd)