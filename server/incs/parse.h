/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Parse Header file
*/

#ifndef PARSE_H_
	#define PARSE_H_

	#include <string.h>
	#include <sys/types.h>
	#include <sys/socket.h>
	#include <netdb.h>
	#include <stdlib.h>
	#include <time.h>
	#include <unistd.h>
	#include <netinet/in.h>
	#include <arpa/inet.h>
	#include <string.h>
	#include <stdio.h>
	#include <sys/types.h>
	#include <dirent.h>
	#include <sys/types.h>
	#include <sys/stat.h>
	#include <fcntl.h>
	#include <sys/types.h>
	#include <sys/wait.h>

typedef struct	s_parse
{
	int	port;
	int	width;
	int	height;
	char	**teams;
	int	max_client;
	int	freq;
}		t_parse;

t_parse	*parse_args(char **av);
int	check_arg(char *command);
void	free_tab(char **args);

extern const char	commands_name[6][64];

#endif /* !PARSE_H_ */
