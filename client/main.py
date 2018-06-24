import argparse

from server.graphicalInterface import GraphicalInterface
from server.IA import IA
import signal
import sys

def main():
	ias = []
	for i in range(args.nbIA):
		ias.append(IA(args.name, args.port, args.machine))
	if args.graph:
		ui = GraphicalInterface(args.port, args.machine)
		ui.start()
	for ia in ias:
		ia.start()
	for ia in ias:
		ia.join()
	if args.graph:
		ui.join()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(add_help=False)
	parser.add_argument('-p', help="is the port number", nargs='?', default=4242, const=4242, type=int, dest='port')
	parser.add_argument('-n', help="is the name of the team", nargs='?', default="Team1", const="Team1", type=str, dest='name')
	parser.add_argument('-h', '--machine', help="is the name of the machine; localhost by default", nargs='?', default="localhost", const="localhost", type=str,
                        dest='machine')
	parser.add_argument('--no-graph', help="launch graphical window or not; true by default", action="store_false", dest='graph')
	parser.add_argument('--nb-ia', help="is the number of ia to launch; 1 by default", nargs='?', default=1, const=1, type=int, dest='nbIA')
	try:
        	args = parser.parse_args()
	except:
        	exit(84)
	main()
