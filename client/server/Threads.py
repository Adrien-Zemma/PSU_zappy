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
            data = self.queue.get(status, 0.1)
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
            print("Putting [" + cmd + "] in queue")
            self.queue.put(cmd)
            cmd = self._read()