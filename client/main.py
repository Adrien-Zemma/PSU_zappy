import argparse

from server.graphicalInterface import GraphicalInterface
from server.IA import IA


def main():
	ia = IA(args.name, args.port, args.machine)
	ui = GraphicalInterface(args.port)
	ui.start()
	ia.start()
	ia.join()
	ui.join()
	print("Main finished")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-p', help="is the port number", nargs='?', const=4242, type=int, dest='port')
    parser.add_argument('-n', help="is the name of the team", nargs='?', const="Team1", type=str, dest='name')
    parser.add_argument('-h', '--machine', help="is the name of the machine; localhost by default", nargs='?', const="localhost", type=str,
                        dest='machine')
    try:
        args = parser.parse_args()
    except:
        exit(84)
    main()
