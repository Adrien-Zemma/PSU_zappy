import threading
import time
import socket
import queue


class ThreadRead(threading.Thread):
	def __init__(self, socket):
		threading.Thread.__init__(self)
		self.queue = queue.Queue()
		self.socket = socket
		self.loop = True

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

	def get_command(self, status: bool = True, timeout: int = 0.1):
        	try:
        	    data = self.queue.get(status, timeout)
        	    self.queue.task_done()
        	except queue.Empty:
        	    data = None
        	return data

	def run(self):
		"""
		Thread run method. Read command from server socket
		"""
		cmd = self._read()
		while self.loop and cmd:
        		print("Putting [" + cmd + "] in queue")
        		self.queue.put(cmd)
        		cmd = self._read()
