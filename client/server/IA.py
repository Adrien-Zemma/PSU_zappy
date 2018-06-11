import threading

from .Server import Server


class Ia(Server, threading.Thread):
    def __init__(self, port, ip="localhost"):
        super().__init__(port, ip)
        threading.Thread.__init__(self)

    def run(self):
        print("Hi IA")
