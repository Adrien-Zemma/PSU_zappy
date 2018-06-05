import argparse

from queue import Queue
from server.Server import Server
from server.Threads import ThreadRead, ThreadWrite

def dump_queue(q):
	print("Gonna parse q: ")
	for elem in list(q.queue):
		print("\t- " + elem)

def main():
	serv = Server(8081)
	th1 = ThreadRead(serv.sock, serv.queue_read)
	th2 = ThreadWrite(serv.sock, serv.queue_write)
	th1.start()
	th2.start()
	print("Threads started")
	while serv.is_connected:
		cmd = th1.get_command()
		print("From main : " + cmd)
		print("Send " + cmd + " to serv")
		th2.write_command(cmd)
		if cmd is None:
			th1.join()
			th2.join()
	print("Main finished")

if __name__ == '__main__':
	parser = argparse.ArgumentParser(add_help=False)
	parser.add_argument('-p', help="is the port number", type=int, dest='port')
	parser.add_argument('-n', help="is the name of the team", type=str, dest='name')
	parser.add_argument('-h', '--machine', help="is the name of the machine; localhost by default", type=str, dest='machine')
	try :
		args = parser.parse_args()
	except :
		exit(84)
	main()