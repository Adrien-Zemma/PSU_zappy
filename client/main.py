import argparse

from queue import Queue
from server.Server import Server
from server.Threads import ThreadRead, ThreadWrite

def main():
	serv = Server(args.port)
	serv.start_threads()
	print("Threads started")
	serv.get_map_size()
	print(serv.get_map())
	serv.join_threads()
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