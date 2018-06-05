/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** server
*/

#ifndef SERVER_H_
	#define SERVER_H_

#include "parse.h"
#include "commands.h"
#include <string.h>

typedef struct command_s command_t;

typedef	struct client_s
{
	int	fd;
}	client_t;

typedef	struct server_s
{
	int	fd;
	int	*fds;
	int	nb_fd;
	command_t	**command;
	client_t	**clients;
	int	nb_client;
	t_parse	*parse;
}	server_t;

int	set_socket(t_parse *parse, server_t *server);
char	*getnextline(int fd);
int	start_server(t_parse *parse, server_t *server);
int	set_accept(server_t *server);
void	read_command(int c1, server_t *server);
#endif /* SERVER */

